from shared_cues import merge_cues, MERGE_TIME

def build_cues(position):
    """position: 1 (front, closest to audience) through 5 (back wall)."""
    delay = (position - 1) * 0.4          # ripple: each row starts a beat later
    height = 1.0 + (position - 1) * 0.3   # back rows fly higher, stay visible

    intro = [
        (0.0,        "takeoff",  None),
        (1.0 + delay, "led_set", (255, 60, 0, 255)),
        (3.0 + delay, "breathe", {"color": (255, 60, 0), "duration": 12, "cycles": 3}),
        (10.0,        "rise",    {"height": height, "power": 30}),
        (20.0 + delay, "fade",   {"from": (255, 60, 0), "to": (255, 0, 0), "duration": 8}),
        (35.0,        "hover",   5),
    ]
    return intro + [(MERGE_TIME + t, action, params) for (t, action, params) in merge_cues]