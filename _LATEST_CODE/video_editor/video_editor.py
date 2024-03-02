from moviepy.editor import *
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.VideoClip import TextClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.video.compositing.concatenate import concatenate_videoclips
import os

current_file_path = os.path.abspath(__file__)
current_dir_path = os.path.dirname(current_file_path)
os.chdir(current_dir_path)

def ctos(timecode): #code to sec
    fps=25
    hours, minutes, seconds, frames = [int(x) for x in timecode.split(":")]
    total_seconds = hours*3600 + minutes*60 + seconds + frames/fps
    return total_seconds

def frtoTC(frames, fps=25):
    total_seconds = int(frames / fps)
    h = int(total_seconds / 3600)
    m = int((total_seconds % 3600) / 60)
    s = int(total_seconds % 60)
    f = frames % fps
    return ("%02d:%02d:%02d:%02d" % (h, m, s, f))

def cut_and_combine(video_filename,dest_filename,fr_after_op,fr_start_eyecatch,fr_end_eyecatch,fr_before_ending):
    after_op = frtoTC(fr_after_op)
    start_eyecatch = frtoTC(fr_start_eyecatch)
    end_eyecatch = frtoTC(fr_end_eyecatch)
    before_ending = frtoTC(fr_before_ending)

    video = VideoFileClip(video_filename)
    after_op_to_start_eyecatch = video.subclip(ctos(after_op),ctos(start_eyecatch))
    end_eyecatch_to_before_ending = video.subclip(ctos(end_eyecatch),ctos(before_ending))

    combined = concatenate_videoclips([after_op_to_start_eyecatch,end_eyecatch_to_before_ending])

    combined.write_videofile(dest_filename,fps=video.fps)