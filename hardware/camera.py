import numpy as np
from picamera2 import Picamera2
import time
import cv2
from PIL import Image

size = (1280, 720)

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
        self.camera.configure(self.config)

        self.camera.set_controls({"FrameRate": frame_rate})

        self.camera.start()
        time.sleep(1)

    def capture(self, frames: int = 100, output_path: str = "output_video.mp4"):
        # Initialize the video writer
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        video_out = cv2.VideoWriter(output_path, fourcc, frame_rate, size)

        start_time = time.time()
        prev_time = time.time()
        for i in range(frames):
            # buffers, metadata = self.camera.capture_buffers(["raw"])
            np_array = self.camera.capture_array()

            im = Image.fromarray(np_array).convert('RGB')
            im.save("test.jpeg")
            # pil_image = self.camera.helpers.make_image(
            #     buffers[0], self.config["raw"]
            # )

            # cv2_image = cv2.cvtColor(np.array(np_array), cv2.COLOR_RGB2BGR)

            # output_path = f"test.jpg"
            # cv2.imwrite(output_path, cv2_image)

            # video_out.write(cv2_image)

            curr_time = time.time()
            duration = curr_time - prev_time
            prev_time = curr_time
            print("image", i, round((duration) * 1000, 2), "ms")

        video_out.release()

        print("average fps", 1 / (time.time() - start_time) * frames)

        return output_path
