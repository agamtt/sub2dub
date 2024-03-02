import cv2
import os
from tqdm import tqdm

os.chdir(os.path.dirname(os.path.abspath(__file__)))
# Open the input video file
input_file = '1blu.mkv'
cap = cv2.VideoCapture(input_file)

# Get the input video's frame rate and calculate the desired output fps
input_fps = cap.get(cv2.CAP_PROP_FPS)
output_fps = 25

# Create an output video writer with the desired fps
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_file = '1blu_cv.mp4'
out = cv2.VideoWriter(output_file, fourcc, output_fps, (640, 480))

# Get the total number of frames in the input video
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# Loop through each frame of the input video and write it to the output video
frame_count = 0
with tqdm(total=total_frames, unit='frame') as pbar:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        # Convert the frame rate to the desired output fps
        frame_rate_ratio = int(round(input_fps / output_fps))
        if frame_rate_ratio == 0:
            frame_rate_ratio = 1
        # Write each frame to the output video the appropriate number of times
        for i in range(frame_rate_ratio):
            out.write(frame)
        frame_count += 1
        pbar.update(1)

# Release the input and output video files
cap.release()
out.release()
