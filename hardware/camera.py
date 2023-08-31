import numpy as np
from picamera2 import Picamera2
import time
import cv2


size = (2304, 1296)

frame_rate = 30


class Camera:
    camera: Picamera2 = None

    config = None

    def __init__(self):
        self.camera = Picamera2()
        sensor_modes = self.camera.sensor_modes

        self.config = self.camera.create_preview_configuration(
            main={"size": size}, raw=sensor_modes[1]
        )
        self.camera.configure(self.__format__config)

        self.camera.set_controls({"FrameRate": frame_rate})

        self.camera.start()
        time.sleep(1)

    def capture(self, frames: int = 100, output_path: str = "output_video.mp4"):
        # Initialize the video writer
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        out = cv2.VideoWriter(output_path, fourcc, frame_rate, size)

        # Capture frames and calculate FPS
        startTime = time.time()
        prev_time = time.time()
        for i in range(frames):
            buffers, metadata = self.camera.capture_buffers(["raw"])

            pil_image = self.cameracamera.helpers.make_image(
                buffers[0], self.config["raw"]
            )

            cv2_image = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)

            # output_path = f"test.jpg"
            # cv2.imwrite(output_path, cv2_image)

            out.write(cv2_image)

            curr_time = time.time()
            duration = curr_time - prev_time
            prev_time = curr_time
            print("image", i, round((duration) * 1000, 2), "ms")

        out.release()

        print("average fps", 1 / (time.time() - startTime) * frames)

        return output_path
