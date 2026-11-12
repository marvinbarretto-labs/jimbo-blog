"""Synthetic light-trigger policy; no hardware or audio access."""

def play_times(samples):
    dark_since = None
    armed = False
    plays = []
    for time, light in samples:
        if light <= 30:
            if dark_since is None:
                dark_since = time
            if time - dark_since >= 5:
                armed = True
        else:
            dark_since = None
            if light >= 70 and armed:
                plays.append(time)
                armed = False
    return plays
