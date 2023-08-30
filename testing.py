import multiprocessing
import threading
from picamera2 import Picamera2
import time
import cv2
import numpy as np



size = (2304, 1296)

# Configure camera for 2028x1520 mode
camera = Picamera2()
sensor_modes = camera.sensor_modes

print("sensor modes:", sensor_modes)

config = camera.create_preview_configuration(main={"size": size}, raw=sensor_modes[1])
camera.configure(config)

camera.set_controls({"FrameRate": 30})
# estimate 30 fps

# Start camera
camera.start()

time.sleep(1)

# Set up the camera and video parameters
frame_width = size[0]
frame_height = size[1]
fps = 30
output_path = "output_video.mp4"

# Initialize the video writer
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

def write_frames(frame_queue, process_id):
    while True:
        print("frame added")
        frame = frame_queue.get()
        if frame is None:
            break
        out.write(frame)


frame_queue = multiprocessing.Queue()

processes = []
num_processes = 4
for i in range(num_processes):
    process = multiprocessing.Process(target=write_frames, args=(frame_queue, i))
    process.start()
    processes.append(process)

# Capture frames and calculate FPS
startTime = time.time()
frames = 100
prev_time = time.time()
for i in range(frames):
    array = camera.capture_array()

    img = cv2.cvtColor(array, cv2.COLOR_RGB2BGR)

    # output_path = f"test.jpg"
    # cv2.imwrite(output_path, img)



    frame_queue.put(img)

    # out.write(img)

    curr_time = time.time()
    print("image", i, round((curr_time - prev_time) * 1000, 2), "ms")
    prev_time = curr_time

print("fps", 1 / (time.time() - startTime) * frames)

# Add None to the queue for each process to signal stopping
for _ in range(num_processes):
    frame_queue.put(None)

# Wait for all processes to finish
for process in processes:
    process.join()


out.release()
