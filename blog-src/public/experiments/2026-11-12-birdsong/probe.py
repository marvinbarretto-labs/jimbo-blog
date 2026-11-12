"""Run beside trigger.py. All times and light readings are invented.
Light is a unitless scale, not lux. No sensor, speaker or playback is used.
"""
from trigger import play_times

samples = [(0, 90), (1, 10), (2, 90), (10, 10), (15, 10),
           (16, 90), (17, 10), (18, 90), (30, 10), (35, 10), (36, 90)]
previous_bright = False
edges = []
for time, light in samples:
    bright = light >= 70
    if bright and not previous_bright:
        edges.append(time)
    previous_bright = bright

print("Invented samples (seconds, unitless brightness):", samples)
print("Rising-edge play requests:", edges)
print("Confirmed-dark play requests:", play_times(samples))
