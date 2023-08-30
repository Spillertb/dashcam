import threading
from picamera2 import Picamera2
import time
import cv2
import numpy as np


# Configure camera for 2028x1520 mode
camera = Picamera2()
sensor_modes = camera.sensor_modes

print("sensor modes:", sensor_modes)

config = camera.create_preview_configuration(main={"size": (2304, 1296)})
camera.configure(config)

camera.set_controls({"FrameRate": 30})
# estimate 30 fps

# Start camera
camera.start()

time.sleep(1)


active_threads = []

# Capture frames and calculate FPS
startTime = time.time()
frames = 100
prev_time = time.time()
for i in range(frames):
    array = camera.capture_array()

    img = cv2.cvtColor(array, cv2.COLOR_RGB2BGR)

    output_path = f"test.jpg"
    cv2.imwrite(output_path, img)
    
    curr_time = time.time()
    print("image", i, round((curr_time - prev_time) * 1000, 2), "ms")
    prev_time = curr_time

print("fps", 1 / (time.time() - startTime) * frames)
