from picamera2 import Picamera2
import time

# Configure camera for 2028x1520 mode
camera = Picamera2()

print("sensor modes:", camera.sensor_modes)

config = camera.create_preview_configuration(main = {"size": (2304, 1296)}, raw = camera.sensor_modes[1])
camera.configure(config)
camera.set_controls({"FrameRate": 100})

# Start camera
camera.start()

# 
time.sleep(1)

# Capture frames and calculate FPS
startTime = time.time()
frames = 50
for i in range(frames):
    array = camera.capture_array()
print(1 / (time.time() - startTime) * frames)