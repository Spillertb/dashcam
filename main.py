from picamera2 import Picamera2
from libcamera import controls
import os

FAST_FOCUS = False
HDR = False


def create_camera() -> Picamera2:
    return Picamera2()


def start_camera(camera: Picamera2) -> None:
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
    else:
        camera.set_controls({"AfMode": controls.AfModeEnum.Continuous})

    camera.start()


def stop_camera(camera: Picamera2) -> None:
    camera.stop()

    if HDR:
        # this must be run after stopping the camera
        print("Setting HDR to OFF")
        os.system("v4l2-ctl --set-ctrl wide_dynamic_range=0 -d /dev/v4l-subdev0")


if __name__ == "__main__":
    camera = create_camera()
    start_camera(camera)

    camera.start_and_capture_files("test{:d}.jpg", num_files=1)  # , delay=0.5)

    stop_camera(camera)
