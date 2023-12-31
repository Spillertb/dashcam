from picamera2 import Picamera2
from picamera2.encoders import H264Encoder
from picamera2.outputs import FfmpegOutput
from libcamera import controls
from hardware.camera import Camera
import os
import time


# class Camera:
#     def __init__(self, hdr=False, fast_focus=False) -> None:
#         self.hdr = hdr
#         self.fast_focus = fast_focus

#         self.camera = Picamera2()

#         self.sensor_modes = self.camera.sensor_modes

#         print(f"sensor modes: {self.sensor_modes}")

#         if hdr:
#             os.system("v4l2-ctl --set-ctrl wide_dynamic_range=1 -d /dev/v4l-subdev0")
#             print("Setting HDR to ON")

#         if fast_focus:
#             camera.set_controls(
#                 {
#                     "AfMode": controls.AfModeEnum.Continuous,
#                     "AfSpeed": controls.AfSpeedEnum.Fast,
#                 }
#             )

#         # let the camera warmup and stabalize brightness
#         time.sleep(1)

#     def start(self) -> None:
#         self.camera.start()

#     def stop(self) -> None:
#         self.camera.stop()
#         if self.hdr:
#             # this must be run after stopping the camera
#             print("Setting HDR to OFF")
#             os.system("v4l2-ctl --set-ctrl wide_dynamic_range=0 -d /dev/v4l-subdev0")

#     def capture_video(self, duration_seconds: int) -> None:
#         print("Stopping camera capture")
#         self.stop()

#         encoder = H264Encoder(10000000)
#         output = FfmpegOutput("test.mp4")

#         self.camera.start_recording(encoder, output)
#         time.sleep(duration_seconds)
#         self.camera.stop_recording()


if __name__ == "__main__":
    camera = Camera()
    # start_camera(camera)

    output = camera.capture()