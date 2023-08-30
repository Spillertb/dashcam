from io import BytesIO
import time
from picamera2 import Picamera2
from picamera2.encoders import H264Encoder
from picamera2.outputs import FfmpegOutput
from libcamera import controls

camera = Picamera2(
    resolution=(3280, 2464), framerate=15
)  # sensor_mode=3 only makes it worse
time.sleep(2)
cnt = 0
stream = BytesIO()
for _ in camera.capture_continuous(stream, burst=True, format="rgb"):
    stream.truncate()
    stream.seek(0)
    print(time.time())
    # DO NOTHING
    cnt += 1

    if cnt > 10:
        break

    camera.close()
