from shared_cues import merge_cues, MERGE_TIME

def build_cues(position):
    """position: 1 (front, closest to audience) through 5 (back wall)."""
    palette = [
        (128, 0, 255), (161, 0, 224), (194, 0, 193), (227, 0, 162), (255, 0, 128)
    ]
    from_color = palette[(position - 1) % len(palette)]
    to_color = (255, 0, 128)
    height = 0.6 + (position - 1) * 0.25

    intro = [
        (0.0,  "takeoff",  None),
        (2.0,  "led_set",  (*from_color, 255)),
        (5.0,  "fade",     {"from": from_color, "to": to_color, "duration": 15}),
        (20.0, "rise",     {"height": height, "power": 25}),
        (35.0, "hover",    5),
    ]
    return intro + [(MERGE_TIME + t, action, params) for (t, action, params) in merge_cues]