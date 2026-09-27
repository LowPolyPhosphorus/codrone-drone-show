from codrone_edu.drone import *
import time
from show_lib import led_breathe, led_fade, led_spin, safe_sleep
from cues import cues

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

drone.close()