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
    """Sleeps in small chunks. If the front sensor trips mid-wait, lands immediately
    instead of finishing the countdown to the next cue. No thread needed, the check
    just happens between sleep chunks."""
    elapsed = 0
    while elapsed < duration:
        chunk = min(check_interval, duration - elapsed)
        time.sleep(chunk)
        elapsed += chunk
        if drone.get_front_range() < 20:  # cm, something is right in front of it
            print("Obstacle detected, landing early.")
            drone.land()
            drone.close()
            raise SystemExit
