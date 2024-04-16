from moviepy.editor import *
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.VideoClip import TextClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.video.compositing.concatenate import concatenate_videoclips
import os

import json
from datetime import datetime, timedelta
import os
import re

current_file_path = os.path.abspath(__file__)
current_dir_path = os.path.dirname(current_file_path)
os.chdir(current_dir_path)

def ctos(timecode):
    # 시간 코드를 "시:분:초.밀리초" 형식으로 파싱합니다.
    hours, minutes, seconds_ms = timecode.split(':')
    seconds, ms = seconds_ms.split('.')
    # 시, 분, 초, 밀리초를 각각 정수 또는 실수로 변환
    total_seconds = int(hours) * 3600 + int(minutes) * 60 + int(seconds) + int(ms) / 1000.0
    return total_seconds


def frtoTC(frames, fps=25):
    total_seconds = int(frames / fps)
    h = int(total_seconds / 3600)
    m = int((total_seconds % 3600) / 60)
    s = int(total_seconds % 60)
    f = frames % fps
    return ("%02d:%02d:%02d:%02d" % (h, m, s, f))

def cut_and_combine(video_filename,dest_filename,tc_after_op,tc_start_eyecatch,tc_end_eyecatch,tc_before_ending):

    video = VideoFileClip(video_filename)
    after_op_to_start_eyecatch = video.subclip(ctos(tc_after_op),ctos(tc_start_eyecatch))
    end_eyecatch_to_before_ending = video.subclip(ctos(tc_end_eyecatch),ctos(tc_before_ending))

    combined = concatenate_videoclips([after_op_to_start_eyecatch,end_eyecatch_to_before_ending])

    # after_op_to_start_eyecatch.write_videofile(dest_filename+"after_op.mp4",fps=video.fps)
    # end_eyecatch_to_before_ending.write_videofile(dest_filename+"after_eye.mp4",fps=video.fps)
    combined.write_videofile(dest_filename,fps=video.fps)

def set_audio_from_video(dest,display_video,src_video):
    src_video = VideoFileClip(src_video)
    audio = src_video.audio

    display_video = VideoFileClip(display_video)

    final_clip = display_video.set_audio(audio)
    final_clip.write_videofile("음성합성테스트.mp4")



### VIDEO READ ###

dub_path = r"C:\Users\girin\Desktop\이누야샤_영상\이누야샤_원본_한국어\이누야샤더빙(투니버스_토렌트)"
dub_video = {}
i = 1

for file_name in os.listdir(dub_path):  # 폴더 내 파일들에 대해 반복
    if os.path.isfile(os.path.join(dub_path, file_name)):  # 파일인지 확인
        dub_video[f"ep{i}"] = {"file_name": file_name, "path": os.path.join(dub_path,file_name)}
        i+=1

blu_path = r"C:\Users\girin\Desktop\이누야샤_영상\이누야샤_원본_일본어\이누야샤일어_블루레이(fullmetal)"
blu_video = {}
i = 1
files = os.listdir(blu_path)
pattern = re.compile(r"Inuyasha - (\d+)")
sorted_files = sorted(files, key=lambda x: int(pattern.search(x).group(1)))
for file_name in sorted_files:  # 폴더 내 파일들에 대해 반복
    if os.path.isfile(os.path.join(blu_path, file_name)):  # 파일인지 확인
        blu_video[f"ep{i}"] = {"file_name": file_name, "path": os.path.join(blu_path,file_name)}
        i+=1


    
### JSON READ ###
blu_dict_file = r"C:\Users\girin\Desktop\sub2dub\blu_merged_time.json"
with open(blu_dict_file, "r") as f:
  blu_dict = json.load(f)

dub_dict_file = r"C:\Users\girin\Desktop\sub2dub\dub_merged_time.json"
with open(dub_dict_file, "r") as f:
  dub_dict = json.load(f)

zero_time = "00:00:00.000"
big_time = "00:99:99.000"

### Video Concat

for ep in range(1,2):
    blu_op_end = "00:"+blu_dict[f"blu_ep{ep}"]["op_end"][3:-3]+".000"
    blu_eye_start = blu_dict[f"blu_ep{ep}"]["eye_start_time"]+".000"
    blu_eye_start_obj = datetime.strptime(blu_eye_start,"%H:%M:%S.%f")
    blu_eye_len = blu_dict[f"blu_ep{ep}"]["eye_len_sec"]
    blu_eye_end_obj = blu_eye_start_obj + timedelta(seconds=blu_eye_len)
    blu_eye_end = blu_eye_end_obj.strftime("%H:%M:%S.%f")[:-3]
    blu_ed_start = blu_dict[f"blu_ep{ep}"]["ed_start"]

    dub_op_end = dub_dict[f"dub_ep{ep}"]["op_end"]
    dub_eye_start = dub_dict[f"dub_ep{ep}"]["eye_start_time"]+".000"
    dub_eye_start_obj = datetime.strptime(dub_eye_start,"%H:%M:%S.%f")
    dub_eye_start = dub_eye_start_obj.strftime("%H:%M:%S.%f")[:-3]
    dub_eye_len = dub_dict[f"dub_ep{ep}"]["eye_len_sec"]
    dub_eye_end_obj = dub_eye_start_obj + timedelta(seconds=dub_eye_len)
    dub_eye_end = dub_eye_end_obj.strftime("%H:%M:%S.%f")[:-3]
    dub_ed_start = dub_dict[f"dub_ep{ep}"]["ed_start"]

    dub_ed_start = dub_ed_start[:8] + '.' + dub_ed_start[9:]


    #cut_and_combine(blu_video[f"ep{ep}"]["path"],"blu1_concat.mp4",blu_op_end,blu_eye_start,blu_eye_end,blu_ed_start)
    #cut_and_combine(dub_video[f"ep{ep}"]["path"],"dub1_concat.mp4",dub_op_end,dub_eye_start,dub_eye_end,dub_ed_start)
    set_audio_from_video("dest.mp4","blu1_concat.mp4","dub1_concat.mp4")










