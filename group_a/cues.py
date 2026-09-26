cues = [
    (0.0,  "takeoff",  None),
    (1.0,  "led_set",  (255, 0, 0, 255)),
    (3.0,  "breathe",  {"color": (255, 0, 0), "duration": 6, "cycles": 2}),
    (10.0, "fade",     {"from": (255, 0, 0), "to": (0, 0, 255), "duration": 4}),
    (15.0, "hover",    3),
    (18.0, "rise",     {"height": 1.0, "power": 30}),
    (25.0, "spin_led", {"colors": [(255, 0, 0, 255), (0, 255, 0, 255), (0, 0, 255, 255)],
                         "hold": 0.3, "cycles": 4}),
    (40.0, "led_set",  (255, 255, 255, 255)),
    (85.0, "land",     None),
]
