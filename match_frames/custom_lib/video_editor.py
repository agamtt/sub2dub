from moviepy.editor import *
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.VideoClip import TextClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.video.compositing.concatenate import concatenate_videoclips
import os


def ctos(timecode): # convert timecode to total_second
    fps=25
    hours, minutes, seconds, frames = [int(x) for x in timecode.split(":")]
    total_seconds = hours*3600 + minutes*60 + seconds + frames/fps
    return total_seconds

def frtoTC(frames, fps=25): # convert frame to timecode
    total_seconds = int(frames / fps)
    h = int(total_seconds / 3600)
    m = int((total_seconds % 3600) / 60)
    s = int(total_seconds % 60)
    f = frames % fps
    return ("%02d:%02d:%02d:%02d" % (h, m, s, f))


## ABA -> AA
def cut_and_combine(video_filename,dest_filename,fr_after_op,fr_start_eyecatch,fr_end_eyecatch,fr_before_ending):

    ## convert frame to timecode
    after_op = frtoTC(fr_after_op)
    start_eyecatch = frtoTC(fr_start_eyecatch)
    end_eyecatch = frtoTC(fr_end_eyecatch)
    before_ending = frtoTC(fr_before_ending)

    
    ## get main_video_file (abs_path)
    video = VideoFileClip(video_filename)

    ## subclip = little part of main_video

    after_op_to_start_eyecatch = video.subclip(ctos(after_op),ctos(start_eyecatch))
    end_eyecatch_to_before_ending = video.subclip(ctos(end_eyecatch),ctos(before_ending))

    ## concat subclip1 and subclip2

    combined = concatenate_videoclips([after_op_to_start_eyecatch,end_eyecatch_to_before_ending])

    ## do file write (concated new video)

    combined.write_videofile(dest_filename,fps=video.fps)

def combine_vid_N_audio(vid_path,audio_path,dest_path):
    video_clip = VideoFileClip(vid_path)
    audio_clip = AudioFileClip(audio_path)

    # 오디오를 비디오에 합성합니다.
    video_clip = video_clip.set_audio(audio_clip)

    # 합성된 비디오를 저장합니다.
    video_clip.write_videofile(dest_path)


# 비디오로부터 오디오 추출
def extract_audio_from_vid(vid_path,output_audio_path):
    video_clip = VideoFileClip(vid_path)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(output_audio_path)

# 비디오로부터 오디오 추출, 자동으로 비디오와 동일한 이름 설정
def extract_audio_from_vid_autoname(vid_path):
    filename, file_extension = os.path.splitext(vid_path)

    video_clip = VideoFileClip(vid_path)
    audio_clip = video_clip.audio

    output_audio_path = filename + ".mp3"
    audio_clip.write_audiofile(output_audio_path)

def cut_video(video_path, start_time, end_time):
    video_clip = VideoFileClip(video_path)
    return video_clip.subclip(start_time,end_time)

def concat_subclip(subclip_list, output_path):
    combined_clip = concatenate_videoclips(subclip_list)

    # 생성된 영상을 저장
    combined_clip.write_videofile(output_path)

def edit_by_cutinfo(cutinfo, output_path):
    subclip_list = []

    for cut in cutinfo["cuts"]:
        if cut["used"]:
            start_time = cut["start_time"]
            end_time = cut["end_time"]
            subclip = cut_video(cutinfo["video_path"],start_time,end_time)
            subclip_list.append(subclip)

    for insert in cutinfo["insert"]:
        if insert["used"]:
            start_time = insert["start_time"]
            end_time = insert["end_time"]
            subclip = cut_video(cutinfo["insert_video_path"], start_time, end_time)
            subclip_list.append(subclip)

    concat_subclip(subclip_list, output_path)