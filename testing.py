import cv2
import asyncio

from picamera2 import Picamera2
import time

# Define a coroutine to save images asynchronously
async def save_image_async(img, output_path):
    cv2.imwrite(output_path, img)
    print(f"Image saved to {output_path}")

# Initialize your camera and other necessary variables

# Configure camera for 2028x1520 mode
camera = Picamera2()

print("sensor modes:", camera.sensor_modes)

config = camera.create_preview_configuration(main = {"size": (2304, 1296)})
camera.configure(config)

camera.set_controls({"FrameRate": 100})
# estimate 30 fps

# Start camera
camera.start()

time.sleep(1)

active_tasks = []
# Capture frames and calculate FPS
startTime = time.time()
frames = 500
prev_time = time.time()
for i in range(frames):
    array = camera.capture_array()
    
    img = cv2.cvtColor(array, cv2.COLOR_RGB2BGR)

# Start your loop
async def main_loop():






    # Configure camera for 2028x1520 mode
    camera = Picamera2()

    print("sensor modes:", camera.sensor_modes)

    config = camera.create_preview_configuration(main = {"size": (2304, 1296)})
    camera.configure(config)

    camera.set_controls({"FrameRate": 100})
    # estimate 30 fps

    # Start camera
    camera.start()

    time.sleep(1)

    active_tasks = []
    # Capture frames and calculate FPS
    startTime = time.time()
    frames = 500
    prev_time = time.time()
    for i in range(frames):
        array = camera.capture_array()
        
        img = cv2.cvtColor(array, cv2.COLOR_RGB2BGR)

        output_path = f"output_image_{time.time()}"

        #  save the image asynchronously
        save_task = asyncio.create_task(save_image_async(img, output_path))
        active_tasks.append(save_task)

        print(f"Active tasks: {len(active_tasks)}")

        curr_time = time.time()
        print("image", i, (curr_time-prev_time)*10)
        prev_time=curr_time


        # Clean up finished tasks from the list
        active_tasks = [task for task in active_tasks if not task.done()]

        await asyncio.sleep(0.1)  # Small delay to avoid busy-waiting



# # Run the event loop
# async def run():
#     await asyncio.gather(main_loop())

# # Start the asyncio event loop
# if __name__ == "__main__":
#     asyncio.run(run())






# import asyncio
# from picamera2 import Picamera2
# import time
# import cv2
# import numpy as np
# import asyncio

# # Define a coroutine to save images asynchronously
# async def save_image_async(img, output_path):
#     cv2.imwrite(output_path, img)
#     print(f"Image saved to {output_path}")

# # Configure camera for 2028x1520 mode
# camera = Picamera2()

# print("sensor modes:", camera.sensor_modes)

# config = camera.create_preview_configuration(main = {"size": (2304, 1296)})
# camera.configure(config)

# camera.set_controls({"FrameRate": 100})
# # estimate 30 fps

# # Start camera
# camera.start()

# time.sleep(1)

# active_tasks = []
# # Capture frames and calculate FPS
# startTime = time.time()
# frames = 500
# prev_time = time.time()
# for i in range(frames):
#     array = camera.capture_array()
    
#     img = cv2.cvtColor(array, cv2.COLOR_RGB2BGR)

#     output_path = f"output_image_{time.time()}.jpg"

#     save_task = asyncio.create_task(save_image_async(img, output_path))
#     # Create a coroutine to save the image asynchronously
#     save_task = asyncio.create_task(save_image_async(img, output_path))
#     active_tasks.append(save_task)  # Add the task to the active tasks list

#     # Clean up finished tasks from the list
#     active_tasks = [task for task in active_tasks if not task.done()]

#     # Print the number of active tasks
#     print(f"Active tasks: {len(active_tasks)}")


#     # Prune finished threads from the list
#     active_threads = [t for t in active_threads if t.is_alive()]

#     # Print the number of active threads
#     print(f"Active threads: {len(active_threads)}")

#     curr_time = time.time()
#     print("image", i, (curr_time-prev_time)*10)
#     prev_time=curr_time

# print(1 / (time.time() - startTime) * frames)