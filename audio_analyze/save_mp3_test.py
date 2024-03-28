import librosa
import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt

def save_mp3(audio_file, idx, length, sr_calc=1000, sr_target=44100):
    y_ex, sr_ex = librosa.load(audio_file, sr=sr_target)

    # 추출할 오디오의 시작 시간과 끝 시간 계산
    start_time = idx / sr_calc
    end_time = (idx + length) / sr_calc

    # 추출할 오디오의 시작 인덱스와 끝 인덱스 계산
    start_index = int(start_time * sr_target)
    end_index = int(end_time * sr_target)

    # 추출된 오디오 저장
    y_extracted = y_ex[start_index:end_index]
    output_file = f"extracted_audio_{idx}.mp3"
    sf.write(output_file, y_extracted, sr_target, format='mp3')

# 두 음악 파일 로드
audio_file1 = r"C:\Users\girin\Desktop\sub2dub\movies\audio_extracked\blu_ep1_cfr_audio.mp3"
audio_file2 = r"C:\Users\girin\Desktop\sub2dub\movies\audio_extracked\dub_ep1_cfr_audio.mp3"

sampling_rate = 1000
sampling_rate_final = 44100

# 음악 파일을 librosa를 사용하여 로드하고, 음악 데이터와 샘플링 주파수를 가져옴
y1, sr1 = librosa.load(audio_file1, sr=sampling_rate)
y2, sr2 = librosa.load(audio_file2, sr=sampling_rate)

# 첫번째 파일의 길이 (초 단위)
length_audio1 = len(y1) / sampling_rate

# 두번째 파일의 길이 (초 단위)
length_audio2 = len(y2) / sampling_rate

frame_second = 4 # 4초의 프레임
frame_size = int(frame_second * sampling_rate)
matching_indices = []

'''파일 추출'''

# 추출할 음악의 시작 인덱스와 길이 설정
start_index_audio1 = 10000  # 시작 인덱스 (예시 값)
length_audio1 = 5000  # 추출할 길이 (예시 값)

start_index_audio2 = 20000  # 시작 인덱스 (예시 값)
length_audio2 = 7000  # 추출할 길이 (예시 값)

# 첫번째 음악 파일의 일부분을 MP3 파일로 저장
save_mp3(audio_file1, start_index_audio1, length_audio1)

# 두번째 음악 파일의 일부분을 MP3 파일로 저장
save_mp3(audio_file2, start_index_audio2, length_audio2)