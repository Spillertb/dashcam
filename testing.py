from picamera2 import Picamera2
import time

# Configure camera for 2028x1520 mode
camera = Picamera2()
print(camera.sensor_modes)
config = camera.create_preview_configuration({"size": (2304, 1296)}, raw = camera.sensor_modes[2])
camera.configure(config)
camera.set_controls({"FrameRate": 100})

# Start camera
camera.start()
time.sleep(1)

# Capture 100 frames and calculate FPS
startTime = time.time()
frames = 50
for i in range(frames):
    camera.capture_array("raw")
print(1 / (time.time() - startTime) * frames)