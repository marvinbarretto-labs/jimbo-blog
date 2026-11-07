"""Toy festival route experiment. All places and times are invented.

Start at A at minute zero. Venues sit on a line, ten minutes apart.
Each has one twenty-minute set. Only complete sets count. At each stop,
wait for a future set, attend it, or pass through if its start was missed.
This fixed policy is not an itinerary optimiser or a street routing engine.
"""
from itertools import permutations
import json

POSITIONS = {'A': 0, 'B': 10, 'C': 20}
STARTS = {'A': 80, 'B': 50, 'C': 20}


def score(route):
    position = 0
    now = 0
    walk = 0
    attended = []
    for venue in route:
        leg = abs(POSITIONS[venue] - position)
        walk += leg
        now += leg
        position = POSITIONS[venue]
        if now <= STARTS[venue]:
            now = STARTS[venue] + 20
            attended.append(venue)
    return {'walk': walk, 'sets': attended, 'finish': now}


if __name__ == '__main__':
    rows = [{'route': list(route), **score(route)}
            for route in permutations(POSITIONS)]
    print(json.dumps({'synthetic': True, 'policy': 'attend every reachable full set in route order',
                      'routes': rows}, indent=2))
