'''
ffmpeg 로 mp4 -> mkv convert 가 가능한지 테스트

'''


import subprocess, os

def convert_video(input_path, output_path):
    subprocess.run(['ffmpeg', '-i', input_path, output_path]) 

os.chdir(os.path.dirname(os.path.abspath(__file__)))
convert_video('[Fullmetal] Inuyasha - 01 [1080p][HEVC 10bits].mp4', '[Fullmetal] Inuyasha - 01 [1080p][HEVC 10bits].mkv')