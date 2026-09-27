from shared_cues import merge_cues, MERGE_TIME

def build_cues(position):
    """position: 1 (front, closest to audience) through 5 (back wall)."""
    colors = [(0, 100, 255, 255), (0, 255, 200, 255)]
    start = (position - 1) % len(colors)
    rotated = colors[start:] + colors[:start]   # each row starts on a different color
    delay = (position - 1) * 0.2

    intro = [
        (0.0,          "takeoff",  None),
        (2.0 + delay,  "spin_led", {"colors": rotated, "hold": 0.4, "cycles": 12}),
        (25.0,         "fade",     {"from": (0, 100, 255), "to": (0, 200, 255), "duration": 10}),
        (35.0,         "hover",    5),
    ]
    return intro + [(MERGE_TIME + t, action, params) for (t, action, params) in merge_cues]