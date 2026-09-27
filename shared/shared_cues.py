# The part every group merges into. Defined once so all 15 drones are
# guaranteed to do exactly the same thing at exactly the same point in
# the show, instead of 15 hand-copied endings drifting apart after edits.

MERGE_TIME = 45.0  # seconds into the show when all three groups become one

# Times below are relative to MERGE_TIME, not the start of the show.
merge_cues = [
    (0.0,  "led_set", (255, 255, 255, 255)),
    (2.0,  "fade",    {"from": (255, 255, 255), "to": (255, 215, 0), "duration": 6}),
    (10.0, "rise",    {"height": 1.5, "power": 30}),
    (15.0, "breathe", {"color": (255, 215, 0), "duration": 15, "cycles": 3}),
    (38.0, "led_set", (255, 255, 255, 255)),
    (40.0, "land",    None),
]