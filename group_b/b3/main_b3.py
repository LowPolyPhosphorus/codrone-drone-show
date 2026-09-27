# Drone B3 — Group B, cool spin, row 3

from codrone_edu.drone import *
import time, math

def led_breathe(drone, color, duration, cycles):
    r, g, b = color
    steps = 40
    step_time = duration / (steps * cycles)
    for _ in range(cycles):
        for i in range(steps):
            brightness = math.sin(i / steps * math.pi)
            drone.set_drone_LED(int(r * brightness), int(g * brightness), int(b * brightness), 255)
            time.sleep(step_time)

def led_fade(drone, from_color, to_color, duration):
    steps = 30
    step_time = duration / steps
    for i in range(steps):
        blend = [int(from_color[c] + (to_color[c] - from_color[c]) * i / steps) for c in range(3)]
        drone.set_drone_LED(*blend, 255)
        time.sleep(step_time)

def led_spin(drone, colors, hold, cycles):
    for _ in range(cycles):
        for color in colors:
            drone.set_drone_LED(*color)
            time.sleep(hold)

def safe_sleep(drone, duration, check_interval=0.2):
    """Sleeps in small chunks. If the front sensor trips mid-wait, lands immediately."""
    elapsed = 0
    while elapsed < duration:
        chunk = min(check_interval, duration - elapsed)
        time.sleep(chunk)
        elapsed += chunk
        if drone.get_front_range() < 20:
            print("Obstacle detected, landing early.")
            drone.land()
            drone.close()
            raise SystemExit

cues = [
    (0.0, 'takeoff', None),
    (2.4, 'spin_led', {'colors': [(0, 100, 255, 255), (0, 255, 200, 255)], 'hold': 0.4, 'cycles': 12}),
    (13.4, 'circle', {'speed': 50, 'direction': 1}),
    (20.4, 'circle', {'speed': 50, 'direction': -1}),
    (27.4, 'drift', {'direction': 'right', 'distance': 30, 'power': 25}),
    (33.4, 'drift', {'direction': 'left', 'distance': 30, 'power': 25}),
    (40.0, 'fade', {'from': (0, 100, 255), 'to': (0, 200, 255), 'duration': 10}),
    (53.0, 'rise', {'height': 0.4, 'power': 25}),
    (54.0, 'descend', {'height': 0.4, 'power': 25}),
    (60.0, 'hover', 5),
    (70.0, 'led_set', (255, 255, 255, 255)),
    (72.0, 'fade', {'from': (255, 255, 255), 'to': (255, 215, 0), 'duration': 6}),
    (80.0, 'rise', {'height': 1.5, 'power': 30}),
    (85.0, 'breathe', {'color': (255, 215, 0), 'duration': 15, 'cycles': 3}),
    (108.0, 'led_set', (255, 255, 255, 255)),
    (110.0, 'land', None),
]

drone = Drone()
drone.pair()

print("Ready. Countdown starting...")
for n in (3, 2, 1):
    print(n)
    time.sleep(1)
print("GO")

start_time = time.perf_counter()

for cue_time, action, params in cues:
    now = time.perf_counter() - start_time
    wait = cue_time - now
    if wait > 0:
        safe_sleep(drone, wait)

    if action == "takeoff":
        drone.takeoff()
    elif action == "land":
        drone.land()
    elif action == "hover":
        drone.hover(params)
    elif action == "led_set":
        drone.set_drone_LED(*params)
    elif action == "breathe":
        led_breathe(drone, params["color"], params["duration"], params["cycles"])
    elif action == "fade":
        led_fade(drone, params["from"], params["to"], params["duration"])
    elif action == "spin_led":
        led_spin(drone, params["colors"], params["hold"], params["cycles"])
    elif action == "rise":
        drone.move("up", params["height"], params["power"])
    elif action == "circle":
        drone.circle(params["speed"], params["direction"])
    elif action == "sway":
        drone.sway(params["speed"], params["seconds"], params["direction"])
    elif action == "turn":
        drone.turn_degree(params["degree"])
    elif action == "descend":
        drone.move("down", params["height"], params["power"])
    elif action == "drift":
        drone.move(params["direction"], params["distance"], params["power"])

drone.close()