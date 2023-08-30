from picamera2 import Picamera2
import time

# Configure camera for 2028x1520 mode
camera = Picamera2()
config = camera.create_preview_configuration({"size": (2028, 1520)}, raw = camera.sensor_modes[2])
camera.configure(config)

# Start camera
camera.start()
time.sleep(1)

# Capture 100 frames and calculate FPS
startTime = time.time()
for i in range(100):
    camera.capture_array("raw")
print(1 / (time.time() - startTime) * 100)