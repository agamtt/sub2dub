from moviepy.editor import VideoFileClip
import os
from tqdm import tqdm

def get_video_frames(file_path):
    video = VideoFileClip(file_path)
    frames = []

    # tqdm을 사용하여 진행 상황 바 표시
    with tqdm(total=int(video.fps * video.duration)) as pbar:
        for frame in video.iter_frames():
            frames.append(frame)
            pbar.update(1)

    video.close()
    return frames


def calculate_total_frames(file_path): #더 빠르지만 부정확함
    video = VideoFileClip(file_path)
    fps = video.fps
    duration = video.duration
    total_frames = int(fps * duration)
    video.close()
    return total_frames


for ep_num in range(3,15):
    VIDEO_FILENAME = f'[SHANA]{ep_num}blu.mp4'
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    frames = calculate_total_frames(VIDEO_FILENAME)
    print(f"ep : {ep_num} / 프레임 수: ", frames)