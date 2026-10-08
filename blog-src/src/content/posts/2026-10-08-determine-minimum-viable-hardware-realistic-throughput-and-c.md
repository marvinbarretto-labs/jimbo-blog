---
title: "Determine minimum viable hardware, realistic throughput, and cost to self-host Kimi K3, or the nearest achievable substitute"
date: 2026-10-08
description: "Determine minimum viable hardware, realistic throughput, and cost to self-host Kimi K3, or the nearest achievable substitute"
tags: [local-inference, report]
public: false
---

*Report — a research report (2026-10-08), published to cairn by the dispatch flow. Reference material, not a daily reflection.*

## Summary

**No.** K3's MXFP4 checkpoint is ~1,561 GB [1], so it needs an 8×B300 node (or 16×B200 / 2×8×H200) [1][2]. That is roughly £500k+ to buy, or £20k+/month to rent. Bought, it only beats OpenRouter above roughly 3–4 billion tokens/month sustained (my estimate). The one-person options are a 1-bit quant on a 2 TB-RAM server at **0.10 tok/s (measured)** [4], or paying OpenRouter. The largest substitute that genuinely fits one person's hardware is a ~750B-class MoE (e.g. GLM-5.2 4-bit) on a 512 GB Mac Studio, or Kimi K2.6 (1T/32B) on a multi-GPU box.

## From prior context

No prior-context notes were supplied. The vault note (note_9f232efd, "Determine minimum viable hardware…") states K3 is 2.8T total / 104B active, MXFP4, 1M context. It also says weights and licence are settled and must not be re-checked, and that the sibling RTX 3090 note gives ~87 tok/s on 32B models. I did not re-check weights or licence. The model card confirms 2.8T/104B, 93 layers, 896 experts with 16 routed, MXFP4 weights and MXFP8 activations, and a 1,048,576-token context [3].

## New findings

**1. The checkpoint is ~1.56 TB, not 1.4 TB or 594 GB.**
- Particula measured 1,560,936,091,448 bytes across 96 safetensors shards on 2026-07-28 [1].
- Some blogs claim 594 GB. That is Unsloth's 1-bit GGUF, not the native weights [5].
- The naive 2.8T × 4-bit figure of 1.4 TB is also wrong [1].
- Unsloth's Q4/Q8 GGUFs are 1,510/1,560 GB, consistent with this [5].

**2. Minimum viable GPU configurations (native MXFP4)** [1][2]

| Config | HBM | Fits? |
|---|---|---|
| 8×H200 | 1,128 GB | No, 433 GB short |
| 8×B200 | ~1,440 GB | No [2] |
| 8×B300 (288 GB each) | 2,304 GB | Yes, ~628 GB free |
| 2 nodes × 8×H200 | 2,256 GB | Yes, ~582 GB free |
| 16×B200 | ~2,880 GB | Yes [2] |

- Native MXFP4 execution needs Blackwell or MI350-class hardware. H100/H200 can load the weights but dequantise at runtime [2].
- Moonshot recommends 64+ accelerators for production [2].
- ecorpit claims 8×B200 is the practical minimum [6]. That conflicts with the measured size, so I discount it.
- KV cache is small: 13.5 KiB/token at FP8, ~13.5 GiB for a full 1M-token sequence [1]. Weights dominate.

**3. Throughput.**
- **Measured by the vLLM team, batch size 1, Blackwell** [1]:
  - TP8: 111 tok/s.
  - TP16: 118 tok/s.
  - With speculative decoding: 331 and 370 tok/s respectively. The 3× gain is a coding figure; creative writing gets much less [1].
- No multi-user throughput figure has been published [1]. ecorpit's break-even needs ~814 tok/s sustained to match API price [6]. That is a derived number, not a measurement.
- **Measured, CPU offload** [4]:
  - Rig: 4×A100-40GB plus 2 TB RAM, 2×EPYC 7542, UD-IQ1_S (594 GB) with `--cpu-moe`.
  - Prompt processing: ~6–13 tok/s.
  - **Generation: 0.10 tok/s.** A 500-token answer would take about 1h23m (derived).
  - GPUs sat at 0–1% utilisation; the limit is RAM bandwidth. Only that one quant was tested.
- **Unsloth's figure for B200s:** ~20 tok/s generation [5]. This is vendor-quoted and not reproduced by the other source [4].
- **No measured figure exists** for a Mac Studio, NVMe offload, or a consumer GPU plus RAM. Anything quoted there is estimate. Blog claims of "a few tok/s" on a 24 GB GPU have no data behind them.
- **Quality of the 1-bit quant:** perplexity 2.58 and ~79% top-1 agreement with the original [5]. Other community 1-bit quants are far worse [5].
- **Software:** llama.cpp support was still in a dedicated PR at release [2]. Ollama's `kimi-k3:cloud` just proxies to Moonshot [2].

**4. Cost (UK individual).**
- **Purchase:**
  - One HGX B300 NVL8 server (Supermicro) is listed in the EU at €710–740k plus VAT, with one page showing €859k [7].
  - A DGX B300 was quoted at $646,878 [7]. B200-class was ~$500k at launch [7].
  - Order of magnitude is **£550–750k incl. VAT**. This is my conversion; get a quote.
- **Power (estimate, not sourced):** about 14 kW for an 8×B300 node, so ~10,000 kWh/month. At ~£0.27/kWh that is ~£2.8k/month, before cooling. Facilities are not realistic at home: it needs three-phase supply, a rack, and liquid or heavy air cooling.
- **Rent:**
  - 8×B200 is ~$13.1k/month at spot or 36-month reserved, ~$32k at mid-market on-demand, and up to $55–83k on hyperscalers [6].
  - B300 from $3.83/GPU-hr is the cheapest listed [7]. The page does not say whether that is per GPU or per node; I assume per GPU, giving ~£18k/month.
- **Mac Studio M5 Ultra 512 GB:**
  - Late-October launch, no UK price yet. US entry M5 Ultra is $5,500 and 512 GB is expected well above $10k [8].
  - It cannot hold even the 594 GB 1-bit quant. 512 GB is under its 610 GB minimum [5][9].

**5. OpenRouter comparison.**
- K3 is **$2.80–3.00 in / $14–15 out per M tokens**. Sources disagree between $2.80/$14 and $3/$15 [10][2], so check the live page.
- A 3:1 input-heavy blend at $3/$15 is ~$6/M.
- Break-even versus a rented node is ~0.9–2.2B tokens/month (reserved) up to 2–5B (on-demand), by ecorpit's table [6].
- Break-even versus buying: ~£20k/month all-in (my estimate: £600k over 3 years ≈ £17k, plus power ≈ £2.8k) equals ~$26k. At $6/M that is **~4B tokens/month**, around 1,500 tok/s sustained 24/7 (my calculation).
- A single individual's usage is typically orders of magnitude below that. 100M tokens/month costs ~$600 on OpenRouter.

**6. Largest genuinely self-hostable substitute.**
- **Kimi K2.6** (1T total, 32B active, native INT4, 256K context, Modified MIT) [11]:
  - It fits an A100/H100 node [2].
  - OpenRouter lists it at ~$0.95/$4.00 [11].
  - Checkpoint size not confirmed; check the model card.
  - That is a ~£100k+ multi-GPU box, so still not a hobby purchase.
- **Single-person tier:**
  - GLM-5.2 (743B MoE) 4-bit fits entirely in a 512 GB Mac Studio (peak 421 GB on an M3 Ultra) [12].
  - No tok/s published for it. Comparable DeepSeek R1 4-bit on the same class ran at 20.3 tok/s (measured) [12].
  - Kimi K2 Thinking needed four Mac Studios (1.5 TB) for ~28 tok/s [12].
- **How far short of K3:**
  - K3 has 2.8T params versus 743B–1T, and a 1M context versus 256K.
  - K3's self-reported GPQA Diamond is 93.5 and Terminal-Bench 2.1 is 88.3 [3]. I did not find like-for-like benchmarks for the substitutes, so the capability gap is unquantified.
  - Compared with the sibling baseline, a used RTX 3090 handles ~32B dense models at ~87 tok/s (vault note). That is ~30× fewer parameters than K3.

## Comparison

| Option | Hardware | Tok/s | Status | Cost |
|---|---|---|---|---|
| K3 native, vLLM | 8×B300 | 111 (331 spec-dec) b=1 | Measured by vLLM team [1] | £550–750k buy; ~£18k+/mo rent |
| K3 1-bit, CPU-MoE | 4×A100 + 2 TB RAM | 0.10 | Measured [4] | £10–20k+ (my estimate) |
| K3 1-bit, B200s | B200s | ~20 | Vendor-quoted [5] | Datacentre |
| K3 on Mac, NVMe, or 3090 | – | none | **Not measured** | – |
| K3 via OpenRouter | none | n/a | – | $2.80–3 in / $14–15 out per M |
| K2.6 self-host | A100/H100 node | not found | – | ~$1–3/hr/GPU [2] |
| 750B-class 4-bit | 512 GB Mac | ~20 (similar model) | Measured on a different model [12] | £10k+ |

## Recommendation

**Verdict: NO. One individual cannot feasibly self-host Kimi K3.**
- Pay for K3 through OpenRouter or Moonshot. Do not buy hardware for it. Self-hosting only wins above ~4B tokens/month with high utilisation, and that is a team or company scale.
- Pin the live OpenRouter price before budgeting, because sources conflict [10][2].
- For the local-inference epic, set the self-host line at a **512 GB-class unified-memory machine running a ~750B 4-bit MoE (GLM-5.2-class)**, or a rented A100/H100 node for K2.6. Consider this only if the use case needs privacy or fixed cost. K2.6 on OpenRouter at ~$1/$4 is cheap enough that it rarely pays [11].
- Wait for the Apple UK price (late October) and for a measured tok/s on GLM-5.2 or K2.6 before buying anything. Both numbers are missing today.
- Caveat: most of these sources are secondary blogs. The measured-versus-estimated labels above are the honest state of the evidence.

## Sources

1. Particula, "Self-Host Kimi K3: GPU Sizing for 1,561 GB of Weights" – measured checkpoint size, vLLM tok/s, KV cache: https://particula.tech/blog/self-host-kimi-k3-gpu-sizing-mxfp4-vllm
2. Thunder Compute, "How to Run Kimi K3": https://www.thundercompute.com/blog/kimi-k3
3. Hugging Face model card, moonshotai/Kimi-K3: https://huggingface.co/moonshotai/Kimi-K3
4. ComputingForGeeks, "Run Kimi K3 Locally: Real Speed Tested" – 0.10 tok/s measured: https://computingforgeeks.com/run-kimi-k3-locally/
5. Unsloth, "Kimi K3 – How to Run Locally" – GGUF sizes, perplexity, minimum memory: https://unsloth.ai/docs/models/kimi-k3
6. ecorpit, "Self-hosting Kimi K3: GPU cost and the API break-even": https://ecorpit.com/kimi-k3-self-host-gpu-cost-api-break-even-2026/
7. Hardware prices: Servermall (https://servermall.com/sets/nvidia-hgx-servers/); GPUPerHour (https://gpuperhour.com/blog/nvidia-dgx-explained); ComputePrices (https://computeprices.com/providers/vast/gpus/hgx-b300); Novita B200 (https://blogs.novita.ai/b200-price-why-so-high-and-whats-the-smarter-solution/)
8. MacRumors, "Mac Studio With M5 Ultra and 512GB RAM Launching in October": https://macrumors.com/2026/08/25/mac-studio-m5-ultra-512gb-ram-october
9. Pinggy, 512 GB M5 Ultra self-hosting: https://pinggy.io/blog/self_hosting_llms_on_512gb_m5_ultra_mac_studio/
10. DeepInfra, "Kimi K3 pricing providers cost": https://deepinfra.com/blog/kimi-k3-pricing-providers-cost
11. Kimi K2.6 pricing/architecture: https://computeprices.com/providers/openrouter/models/kimi-k2-6 and https://frankx.ai/blog/kimi-k2-analysis-2026
12. Local Mac benchmarks: https://www.implicator.ai/apple-mac-studio-m5-ultra-prompt-processing.md and https://apple.slashdot.org/story/25/03/25/2054214/deepseek-v3-now-runs-at-20-tokens-per-second-on-mac-studio

