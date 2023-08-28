from picamera2 import Picamera2
from picamera2.encoders import H264Encoder
from picamera2.outputs import FfmpegOutput
from libcamera import controls
import os
import time



FAST_FOCUS = False
HDR = True


def create_camera() -> Picamera2:
    camera = Picamera2()
    if HDR:
        os.system("v4l2-ctl --set-ctrl wide_dynamic_range=1 -d /dev/v4l-subdev0")
        print("Setting HDR to ON")

    if FAST_FOCUS:
        camera.set_controls(
            {
                "AfMode": controls.AfModeEnum.Continuous,
                "AfSpeed": controls.AfSpeedEnum.Fast,
            }
        )
    return camera


def start_camera(camera: Picamera2) -> None:
    camera.start()


def stop_camera(camera: Picamera2) -> None:
    camera.stop()

    if HDR:
        # this must be run after stopping the camera
        print("Setting HDR to OFF")
        os.system("v4l2-ctl --set-ctrl wide_dynamic_range=0 -d /dev/v4l-subdev0")


def capture_video(camera: Picamera2) -> None:
    video_config = camera.create_video_configuration()
    camera.configure(video_config)

    encoder = H264Encoder(10000000)
    output = FfmpegOutput("test.mp4")

    camera.start_recording(encoder, output)
    time.sleep(10)
    camera.stop_recording()


if __name__ == "__main__":
    camera = create_camera()
    # start_camera(camera)

    capture_video(camera)

    camera.start_and_capture_files("test{:d}.jpg", num_files=1)  # , delay=0.5)

    stop_camera(camera)
