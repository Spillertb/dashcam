from picamera2 import Picamera2
from libcamera import controls

# it is actually a `camera module 3`
picam2 = Picamera2()

picam2.set_controls({"AfMode": controls.AfModeEnum.Continuous})
# picam2.set_controls({"AfMode": controls.AfModeEnum.Continuous, "AfSpeed": controls.AfSpeedEnum.Fast})

picam2.start()

picam2.start_and_capture_files("fastfocus-test{:d}.jpg", num_files=3, delay=0.5)

picam2.stop()