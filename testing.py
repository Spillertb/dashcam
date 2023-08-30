from picamera2 import Picamera2
import time
from PIL import Image
import numpy as np

# Configure camera for 2028x1520 mode
camera = Picamera2()

print("sensor modes:", camera.sensor_modes)

config = camera.create_preview_configuration(main = {"size": (2304, 1296)})
camera.configure(config)

camera.set_controls({"FrameRate": 100})
# estimate 30 fps

# Start camera
camera.start()

time.sleep(1)

# Capture frames and calculate FPS
startTime = time.time()
frames = 500
prev_time = time.time()
for i in range(frames):
    array = camera.capture_array()
    
    img = Image.fromarray(np.uint8(array))
    img.save("original.png")


    curr_time = time.time()
    print("image", i, (curr_time-prev_time)*10)
    prev_time=curr_time

print(1 / (time.time() - startTime) * frames)