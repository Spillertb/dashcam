import threading
from picamera2 import Picamera2
import time
import cv2
import numpy as np


def save_image_async(img, output_path):
    cv2.imwrite(output_path, img)
    print(f"Image saved to {output_path}")


# Configure camera for 2028x1520 mode
camera = Picamera2()

print("sensor modes:", camera.sensor_modes)

config = camera.create_preview_configuration(main={"size": (2304, 1296)})
camera.configure(config)

camera.set_controls({"FrameRate": 100})
# estimate 30 fps

# Start camera
camera.start()

time.sleep(1)


active_threads = []

# Capture frames and calculate FPS
startTime = time.time()
frames = 500
prev_time = time.time()
for i in range(frames):
    array = camera.capture_array()

    img = cv2.cvtColor(array, cv2.COLOR_RGB2BGR)

    output_path = f"output_image_{time.time()}.jpg"

    save_thread = threading.Thread(target=save_image_async, args=(img, output_path))
    save_thread.start()

    active_threads.append(save_thread)

    # Prune finished threads from the list
    active_threads = [t for t in active_threads if t.is_alive()]

    # Print the number of active threads
    print(f"Active threads: {len(active_threads)}")

    curr_time = time.time()
    print("image", i, (curr_time - prev_time) * 10)
    prev_time = curr_time

print(1 / (time.time() - startTime) * frames)
