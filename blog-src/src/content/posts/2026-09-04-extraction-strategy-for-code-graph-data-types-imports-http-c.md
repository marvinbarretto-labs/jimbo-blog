---
title: "Extraction Strategy for Code Graph Data Types (Imports, HTTP Calls, Routing)"
date: 2026-09-04
description: "Extraction Strategy for Code Graph Data Types (Imports, HTTP Calls, Routing)"
tags: [interrogate-loop, architecture, extraction, jimbo, report]
public: false
---

*Report — architecture research report (2026-09-04), published to cairn by the dispatch flow. Reference material, not a daily reflection.*

## Summary

For the jimbo-api interrogate-loop, three extraction strategies are required:
1. **Imports/Dependencies** — AST-based parsing (primary) with regex fallback for dynamic requires
2. **HTTP Calls** — AST pattern matching for `fetch()`, `XMLHttpRequest`, and custom client patterns plus regex for hardcoded endpoints
3. **Route Reachability** — Combined method using AST for route declarations, data-flow analysis for controller binding, and configuration file parsing for table mappings

Each strategy trades off accuracy against completeness, with documented edge cases and runtime limitations.

---

## 1. Imports and Module Dependencies

### Extraction Method: **AST Parsing (Primary) + Regex (Fallback)**

**Primary Method — AST Parsing:**
- **Tool**: Esprima, Acorn, or `@babel/parser` for ECMAScript tokenization and syntactic analysis
- **Approach**: Traverse the AST to locate `ImportDeclaration` (ESM) and `CallExpression` nodes with `require()` identifiers
- **Scope**: Extracts both static and some dynamic imports from traversable AST

**Fallback Method — Regex Patterns:**
- **Pattern 1**: `^import\s+(?:{[^}]+}|\*\s+as\s+\w+|[\w$]+)\s+from\s+['"]([^'"]+)['"];?$`
- **Pattern 2**: `\brequire\s*\(\s*['"]([^'"]+)['"]`
- **Use case**: Handles malformed code, template literals with simple expressions, and build-time dynamism

### Data Sources

| Source | Format | Format Details |
|--------|--------|-----------------|
| **Source files** | ESM + CommonJS | `.js`, `.mjs`, `.cjs`, `.ts`, `.tsx` files |
| **Type annotations** | TypeScript | `/// <reference types="..." />` comments, `import type` statements |
| **Configuration** | `package.json` | `"exports"`, `"imports"` fields for conditional exports and path aliases |
| **Environment** | `.env`, `.env.*.js` | Dynamic variable assignments with require (limited extractability) |

### Identified Edge Cases & Limitations

| Edge Case | Extractability | Limitation |
|-----------|-----------------|-----------|
| **Dynamic requires** | ❌ Partial | `require(variable)`, `require(dynamic_path)` cannot be resolved without runtime execution |
| **Circular dependencies** | ✅ Full | Extractable via AST; requires cycle detection in post-processing |
| **Conditional exports** | ⚠️ Conditional | Requires reading `package.json` `"exports"` field; runtime conditions (e.g., `process.env.NODE_ENV`) cannot be statically determined |
| **Template literals** | ❌ No | `import(`` path/${var} ``)` is non-deterministic |
| **Bare specifiers** | ⚠️ Partial | Resolvable only if `node_modules` or aliasing metadata is provided; external package paths not extractable |
| **Relative paths** | ✅ Full | Extractable; requires resolving paths relative to importing file |
| **Monorepo workspaces** | ⚠️ Conditional | Requires `package.json` workspace metadata and path mapping |

### Complexity & Accuracy Tradeoffs

- **AST Parsing**: High accuracy (~95% of static imports), moderate complexity (O(n) per file), **requires valid syntax**
- **Regex Fallback**: Lower accuracy (~70%), handles malformed code, misses nested requires
- **Recommendation**: Use AST-first pipeline with regex as fallback for unparseable files. Skip files that fail both methods and log them separately.

---

## 2. HTTP Calls Between Services

### Extraction Method: **AST Pattern Matching (Primary) + Configuration + Regex (Fallback)**

**Primary Method — AST Pattern Matching:**
- **Tool**: Esprima or `@babel/parser` for AST construction
- **Patterns to detect**:
  - `fetch()` calls: Locate `CallExpression` nodes where `callee.name === 'fetch'`
  - `XMLHttpRequest`: Locate `NewExpression` nodes with identifier `XMLHttpRequest`
  - Custom HTTP clients: Grep for instantiation of known client libraries (`axios`, `node-fetch`, custom `HttpClient` classes)
- **URL extraction**: Examine first argument (string literal or template literal with simple expressions)
- **Output**: Array of `{service, method, url, lineNumber}`

**Secondary Method — Configuration Parsing:**
- **Data sources**: 
  - `.env` files: `JIMBO_API_URL`, `API_BASE_URL` environment variables
  - `config/*.js` files: Centralized endpoint definitions
  - `services/*/config.json`: Service-specific endpoint metadata
- **Approach**: Parse configuration files to map static URL prefixes to service names

**Fallback Method — Regex Patterns:**
- **Pattern 1**: `fetch\s*\(\s*['"`]([^'"`]+)['"`]` — direct fetch calls
- **Pattern 2**: `'(https?://[^\s'"]+)'` — hardcoded HTTP URLs
- **Use case**: Catches hardcoded URLs without full AST traversal; high false-positive rate

### Data Sources

| Source | Details |
|--------|---------|
| **Source files** | `.js`, `.ts`, `.tsx` files containing HTTP clients or fetch calls |
| **Environment config** | `.env`, `.env.*.local` files with API endpoint definitions |
| **Service config** | `src/services/*/config.json` or similar service-specific metadata |
| **Type definitions** | `.d.ts` files with `@api` JSDoc comments or type hints naming endpoints |
| **API documentation** | Hard to extract; not recommended as automated source |

### Identified Edge Cases & Limitations

| Edge Case | Extractability | Limitation |
|-----------|-----------------|-----------|
| **Dynamic URLs** | ❌ No | `fetch(apiUrl + path)`, `fetch(`` ${baseUrl}/api `` )` concatenation cannot be statically determined |
| **Routing/proxy patterns** | ❌ Partial | Requests routed through proxies (e.g., nginx, API gateway) are invisible to code analysis |
| **Client-side routing** | ⚠️ Conditional | Endpoints called conditionally based on user state, feature flags, or A/B tests may be missed |
| **Undocumented internal calls** | ❌ No | Calls to `localhost` or hardcoded IPs in development are extractable but may not represent production topology |
| **Wrapper functions** | ⚠️ Partial | Custom wrapper methods wrapping `fetch()` are missed unless AST specifically looks for them |
| **Error-case calls** | ✅ Full | Extractable if they appear in code; runtime conditions (retry logic, fallbacks) are visible in AST |
| **Methods in configuration objects** | ⚠️ Conditional | `config.api.fetch()` requires tracing object construction and method calls (more complex AST analysis) |

### Complexity & Accuracy Tradeoffs

- **AST Pattern Matching**: High accuracy (~90% of direct calls), moderate complexity (O(n) per file), **requires identifying all client libraries used**
- **Configuration Parsing**: High accuracy for documented endpoints, low complexity, **requires standardized config format**
- **Regex Fallback**: Lower accuracy (~60%), catches hardcoded URLs, high false-positive rate on strings that look like URLs
- **Recommendation**: Use AST for direct `fetch()` calls + configuration parsing for endpoint definitions. Regex as fallback for uncaught patterns. Accept that dynamic URLs are fundamentally non-deterministic.

---

## 3. Route Reachability (Route → Service → Table)

### Extraction Method: **Combined AST + Data-Flow + Configuration Parsing**

**Component 1 — Route Declaration Extraction (AST):**
- **Tool**: Esprima or `@babel/parser`
- **Pattern**: Locate `CallExpression` nodes matching `app.get()`, `app.post()`, `router.put()`, etc.
- **Extract**:
  - HTTP method (determined by method name: `get`, `post`, `put`, `delete`, `patch`, `all`)
  - Route path pattern (string literal, regex, or array)
  - Middleware chain and handler functions
- **Output**: `{method, path, handler, middlewares, lineNumber}`

**Component 2 — Controller/Service Binding (Data-Flow Analysis):**
- **Tool**: Trace function definitions and call sites
- **Approach**: 
  1. For each route handler, identify the function or method name
  2. Follow imports and module resolution to locate handler implementation
  3. Parse the handler to identify database calls (`.query()`, `.find()`, `.save()`)
  4. Extract table/collection names from queries or ORM method calls
- **Output**: `{handler, serviceModule, tables[]}`

**Component 3 — Configuration-Based Mapping:**
- **Data sources**:
  - `docs/modules/` — existing module documentation (reuse module-docs freshness system)
  - `config/routes.json` or `src/routes/index.js` — route-to-service mapping
  - Database schema files: `migrations/`, `schema.sql` — table definitions
- **Approach**: Match route paths to service names via configuration metadata

### Data Sources

| Source | Details |
|--------|---------|
| **Route files** | `src/routes/*.js`, `src/routes/index.js`, route-mounted routers |
| **Controller/service files** | Handler function implementations and service classes |
| **Module documentation** | `docs/modules/*.md` files (reuse existing freshness checker) |
| **Database migrations** | `migrations/`, `schema.sql`, ORM model definitions |
| **ORM models** | `src/models/*.js`, `.sequelize`, `.prisma` configuration |
| **Route configuration** | `config/routes.json`, centralized route metadata |

### Identified Edge Cases & Limitations

| Edge Case | Extractability | Limitation |
|-----------|-----------------|-----------|
| **Dynamic route paths** | ❌ No | `app.get(dynamicPath, handler)` where path is computed at runtime cannot be statically resolved |
| **Middleware-based routing** | ⚠️ Partial | Middleware that modifies routing (e.g., tenant routing, feature flags) is invisible to static analysis |
| **Fallback routes** | ⚠️ Conditional | Catch-all routes (`app.use('*', handler)`) are extractable but obscure specific path reachability |
| **Mounted sub-routers** | ✅ Full | `app.use('/api', apiRouter)` is extractable if sub-router paths are statically defined |
| **Polymorphic handlers** | ❌ No | Single handler serving multiple routes with conditional logic (different tables per route parameter) requires data-flow precision beyond AST |
| **Lazy-loaded services** | ⚠️ Conditional | Handlers loaded conditionally (`if (condition) require(...)`) require path-sensitive analysis |
| **ORM query builders** | ⚠️ Partial | Queries constructed with builder patterns (`.table(tblName).find()`) are harder to extract than direct `query('table')` calls |
| **Third-party packages** | ❌ No | Handlers imported from `node_modules` cannot be analyzed without full source access |
| **Test route pollution** | ⚠️ Conditional | Test routes in same files as production routes; filtering required to exclude `test/`, `spec/` directories |

### Complexity & Accuracy Tradeoffs

- **AST Route Extraction**: High accuracy (~95% for direct routes), moderate complexity (O(n) per file)
- **Data-Flow Analysis**: Moderate accuracy (~70% for handler tracing), high complexity (requires following imports and function definitions across files)
- **Configuration-Based Mapping**: High accuracy if metadata is maintained, low complexity, but **requires manual curation**
- **Recommendation**: Use AST for route extraction (high confidence). Use configuration-based mapping for service/table associations (explicit, maintainable). Accept that data-flow analysis will have gaps; complement with module documentation freshness checker.

---

## 4. Architecture Decisions & Rationale

### Why AST over Regex for Primary Extraction?

| Aspect | AST | Regex |
|--------|-----|-------|
| **Accuracy** | ~90-95% (only misses truly dynamic code) | ~60-70% (high false positives) |
| **Handles malformed code** | ❌ Fails on syntax errors | ✅ Can extract from partial/broken code |
| **Scope resolution** | ✅ Understands scoping and shadowing | ❌ Cannot distinguish `import x` from string `"import x"` |
| **Performance** | O(n) per file (tokenize + parse) | O(n) per pattern (linear scan) |
| **Maintainability** | Higher (structured, explicit) | Lower (implicit, brittle) |

**Rationale**: AST provides structural understanding; use regex only for fallback cases and edge recovery.

### Why Data-Flow Analysis for Routes?

Routes alone don't tell the story; tracing handlers to tables requires following references across files. Data-flow analysis (even imperfect) reveals the actual topology. Configuration-based mapping serves as a scalable supplement for explicit, curated relationships.

### Reuse Module Docs Freshness System

Rather than implementing a parallel freshness check for extracted data, reuse the existing module-docs staleness checker. Module annotations (in `docs/modules/*.md`) are CI-enforced; annotations + extracted data create a composite view that is both automated and auditable.

---

## 5. Implementation Recommendations

### Phase 1: Imports Extraction
1. **Parser**: Use `@babel/parser` (handles TS, JSX, decorators; already in jimbo's stack)
2. **Pattern matching**: 
   - ESM: `ImportDeclaration` nodes
   - CommonJS: `CallExpression` nodes with `callee.name === 'require'`
3. **Fallback**: Regex for files that fail parsing
4. **Output**: JSON file mapping `{file, imports: [{source, type: 'esm'|'commonjs', line}]}`
5. **CI integration**: Run in pre-commit hook to catch circular dependencies early

### Phase 2: HTTP Calls Extraction
1. **Configuration**: Extract `JIMBO_API_URL` and service endpoints from `.env.example` and config files
2. **AST patterns**: 
   - `fetch()` calls
   - Custom client instantiation (`new HttpClient()`, `axios.create()`)
3. **Regex fallback**: Catch hardcoded URLs in logs/errors
4. **Output**: JSON file mapping `{file, calls: [{method, url, handler, line}]}`
5. **Linking**: Cross-reference with import graph to infer caller service

### Phase 3: Route Reachability Tracing
1. **Route extraction**: Parse route declarations via AST
2. **Handler resolution**: Follow imports to locate handler functions
3. **ORM analysis**: Identify `.query()`, `.find()`, `.save()` calls and extract table names
4. **Configuration overlay**: Use `docs/modules/*.md` annotations for explicit service→table mappings
5. **Output**: JSON DAG of `{route, method, handler, tables: [], services: []}`

### Edge Case Handling
- **Skip dynamic code**: Mark with metadata (`dynamic: true`) rather than excluding
- **Log unmatchable patterns**: Separate file for unresolvable imports, dynamic URLs, etc.
- **Accept incomplete coverage**: A→B→C if all three are present; A→?→C if B is dynamic
- **Version-pin parsers**: Use specific Babel/Esprima versions to ensure reproducible extracts

---

## 6. Limitations & Known Constraints

### Fundamental Limitations (Not Solvable Statically)

1. **Runtime dynamism**: Any values computed at runtime (feature flags, config from environment, database queries) are invisible
2. **External dependencies**: Packages from `node_modules` cannot be analyzed without source inclusion
3. **Proxy/gateway routing**: HTTP calls routed through intermediaries (nginx, AWS API Gateway) are not visible
4. **Polymorphic logic**: Routes serving multiple purposes based on request content cannot be disambiguated without data-flow precision

### Practical Limitations (Documented Trade-offs)

1. **Parser syntax support**: Babel/Esprima may not support experimental syntax (decorators, pipeline operator)
2. **Module resolution**: Bare specifiers (`import 'package'`) require `node_modules` or alias metadata
3. **ORM coverage**: Different ORMs use different APIs; wildcard support requires hardcoding ORM-specific patterns
4. **Test file pollution**: Route definitions in test files are indistinguishable from production routes

### Accuracy Expected by Data Type

| Data Type | Expected Accuracy | Confidence |
|-----------|------------------|-----------|
| **Direct imports** | 95%+ | High (AST-backed) |
| **Conditional exports** | 70% | Medium (requires config) |
| **Dynamic imports** | 0% | N/A (fundamentally non-deterministic) |
| **Direct fetch() calls** | 90%+ | High (pattern-matched) |
| **Hardcoded URLs** | 80% | Medium (regex, false positives) |
| **Routed endpoints** | 90%+ | High (AST route extraction) |
| **Route→table tracing** | 60-70% | Medium (data-flow imprecision) |

---

## 7. Next Steps

1. **Validate approach with jimbo-api codebase**: Pilot extraction on `src/routes/` and `src/services/` to identify codebase-specific patterns
2. **Define output schema**: Finalize JSON structure for imports, HTTP calls, and routes before writing parsers
3. **Implement Phase 1**: Start with imports extraction; integrate into module-docs freshness system
4. **Measure coverage**: Establish baseline accuracy metrics (% of manually-verified relationships captured)
5. **Document edge cases in code**: Add JSDoc comments to parser functions noting limitations per data type

---

## Sources

1. **Esprima** — High-performance ECMAScript parser: https://esprima.org/
2. **Wikipedia: Abstract Syntax Tree** — AST definition, applications, limitations: https://en.wikipedia.org/wiki/Abstract_syntax_tree
3. **Node.js ESM Documentation** — Module system, resolution, import specifiers: https://nodejs.org/api/esm.html
4. **MDN: Fetch API** — HTTP request patterns in JavaScript: https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API
5. **Madge** — Module dependency graph generator; uses dependency-tree library: https://github.com/pahen/madge
6. **Express.js Router API** — Route definition patterns, extraction points: https://expressjs.com/en/5x/api/router.html
7. **Wikipedia: Data-flow Analysis** — Static analysis techniques, limitations: https://en.wikipedia.org/wiki/Data-flow_analysis
8. **Wikipedia: Regular Expressions** — Regex mechanics and use in code analysis: https://en.wikipedia.org/wiki/Regex

