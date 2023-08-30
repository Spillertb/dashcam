import threading
from picamera2 import Picamera2
import time
import cv2
import numpy as np
import multiprocessing
import queue

def save_image_async(img, output_path):
    cv2.imwrite(output_path, img)
    print(f"Image saved to {output_path}")


def process_image(image_data):
    img = cv2.cvtColor(image_data, cv2.COLOR_RGB2BGR)
    return img

def save_image(img, output_path):
    cv2.imwrite(output_path, img)
    print(f"Image saved to {output_path}")

image_queue = queue.Queue(maxsize=10)

def capture_images():

    # Capture frames and calculate FPS
    startTime = time.time()
    frames = 100
    prev_time = time.time()



    for i in range(frames):
        array = camera.capture_array()
        array = camera.capture_array()
        image_queue.put(array)


        curr_time = time.time()
        print("image", i, round((curr_time - prev_time) * 1000, 2), "ms")
        prev_time = curr_time


    print("fps", 1 / (time.time() - startTime) * frames)

def process_images():
    while True:
        array = image_queue.get()
        img = cv2.cvtColor(array, cv2.COLOR_RGB2BGR)
        # Perform further processing if needed
        image_queue.task_done()

def save_images():
    while True:
        array = image_queue.get()
        img = cv2.cvtColor(array, cv2.COLOR_RGB2BGR)
        output_path = f"output_image_{time.time()}.jpg"
        cv2.imwrite(output_path, img)
        print(f"Image saved to {output_path}")
        image_queue.task_done()



# Configure camera for 2028x1520 mode
camera = Picamera2()
sensor_modes = camera.sensor_modes

print("sensor modes:", sensor_modes)

config = camera.create_preview_configuration(main={"size": (2304, 1296)})
camera.configure(config)

camera.set_controls({"FrameRate": 30})
# estimate 30 fps

# Start camera
camera.start()

time.sleep(1)


active_threads = []

# Capture frames and calculate FPS
startTime = time.time()
frames = 100
prev_time = time.time()


capture_thread = threading.Thread(target=capture_images)
process_thread = threading.Thread(target=process_images)
save_thread = threading.Thread(target=save_images)

capture_thread.start()
process_thread.start()
save_thread.start()

capture_thread.join()
process_thread.join()
save_thread.join()


for i in range(frames):
    array = camera.capture_array()

    img = cv2.cvtColor(array, cv2.COLOR_RGB2BGR)

    output_path = f"output_image_{time.time()}.jpg"


    # cv2.imwrite(output_path, img)
    # print(f"Image saved to {output_path}")

    # save_thread = threading.Thread(target=save_image_async, args=(img, output_path))
    # save_thread.start()

    # active_threads.append(save_thread)

    # # Prune finished threads from the list
    # active_threads = [t for t in active_threads if t.is_alive()]

    # # Print the number of active threads
    # print(f"Active threads: {len(active_threads)}")

    curr_time = time.time()
    print("image", i, round((curr_time - prev_time) * 1000, 2), "ms")
    prev_time = curr_time

print("fps", 1 / (time.time() - startTime) * frames)
