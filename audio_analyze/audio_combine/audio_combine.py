import os
from pydub import AudioSegment

def merge_mp3_segments(output_file, folder):
    # 폴더 내의 모든 MP3 파일을 읽어옴
    mp3_files = [f for f in os.listdir(folder) if f.endswith('.mp3')]

    # 오디오 세그먼트를 저장할 리스트 생성
    audio_segments = []

    # 각 MP3 파일을 오디오 세그먼트로 변환하여 리스트에 추가
    for mp3_file in mp3_files:
        audio_segment = AudioSegment.from_file(os.path.join(folder, mp3_file))
        audio_segments.append(audio_segment)

    # 오디오 세그먼트를 합쳐서 하나의 오디오 세그먼트로 만듦
    merged_audio = sum(audio_segments)

    # 합쳐진 오디오를 MP3 파일로 저장
    merged_audio.export(output_file, format="mp3")

# 저장할 MP3 파일의 경로와 이름 설정
output_file = "merged_audio.mp3"

# 잘린 프레임들이 저장된 폴더 경로 설정
folder = "your_folder_path_here"  # 잘린 프레임들이 저장된 폴더 경로를 입력하세요.

# 잘린 프레임들을 합쳐서 MP3 파일로 저장
merge_mp3_segments(output_file, folder)
