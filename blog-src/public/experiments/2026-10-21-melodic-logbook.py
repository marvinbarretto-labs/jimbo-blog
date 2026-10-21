"""A toy score, not collectr data or a tested audio interface.
Run with Python 3. No dependencies; prints the two proposed mappings.
Question: can a count melody distinguish two different walks?
"""
import json

# Invented collections, with fixed motifs rather than inferred geography.
MOTIFS = {'ridge': ['C4', 'D4', 'G4'], 'valley': ['A3', 'E4', 'D4']}
SCALE = ['C4', 'D4', 'E4', 'G4', 'A4']


def render(actions, policy):
    logged = set()
    heard = []
    for verb, collection, item in actions:
        key = (collection, item)
        if verb == 'undo':
            logged.discard(key)
            continue  # correction is not a new achievement
        if key in logged:
            continue
        logged.add(key)
        heard.append(SCALE[(len(logged) - 1) % len(SCALE)]
                     if policy == 'count' else MOTIFS[collection])
    return heard


def walk(collection):
    return [('log', collection, str(i)) for i in range(3)]


def main():
    ridge, valley = walk('ridge'), walk('valley')
    count_r, count_v = render(ridge, 'count'), render(valley, 'count')
    place_r, place_v = render(ridge, 'motif'), render(valley, 'motif')
    assert count_r == count_v
    assert place_r != place_v
    assert render(ridge + [ridge[-1]], 'motif') == place_r
    assert render(ridge + [('undo', 'ridge', '2')], 'motif') == place_r
    assert render([], 'count') == []
    assert render(ridge + [('undo', 'ridge', '2'), ridge[-1]], 'motif') == place_r + [MOTIFS['ridge']]
    print(json.dumps({'count_ridge': count_r, 'count_valley': count_v,
                      'motif_ridge': place_r, 'motif_valley': place_v,
                      'checks': ['count collision', 'motif distinction', 'duplicate silent',
                                 'undo silent', 'empty silent', 're-log audible']}, indent=2))


if __name__ == '__main__':
    main()
