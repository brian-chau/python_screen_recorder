import pyautogui
import cv2 as camera
import numpy as np
import sys

# Specify resolution
resolution = (1920, 1080)

# Specify video codec
codec = camera.VideoWriter_fourcc(*"XVID")

# Specify name of Output file
filename = "Recording.avi"

# Specify frames rate. We can choose any 
# value and experiment with it
fps = 60.0

# Creating a VideoWriter object
out = camera.VideoWriter(filename, codec, fps, resolution)

while True:
    # Take screenshot using PyAutoGUI
    img = pyautogui.screenshot()

    # Convert the screenshot to a numpy array
    frame = np.array(img)

    # Convert it from BGR(Blue, Green, Red) to
    # RGB(Red, Green, Blue)
    frame = camera.cvtColor(frame, camera.COLOR_BGR2RGB)

    # Display the smoothed cursor to the screen
    pos_x, pos_y = pyautogui.position()

    for x in range(pos_x - 10, pos_x + 10):
        for y in range(pos_y - 10, pos_y + 10):
            if 0 < x - 10 and x + 10 < len(frame[0]) - 1 and 0 < y - 10 and y + 10 < len(frame) - 1:
                frame[y][x] = [255,0,0]

    # Write it to the output file
    out.write(frame)

    # Stop recording when we press 'q'
    if camera.waitKey(1) == ord('q'):
        break

# Release the Video writer
out.release()

# Destroy all windows
camera.destroyAllWindows()