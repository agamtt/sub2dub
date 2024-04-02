import librosa
import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import json

DRWA_PLT = False # 유사도 그래프 출력 토글


### MP3 파일로 저장 ### 

def save_mp3(tag, audio_file, start_index, end_index, sr1, sr2):
    y_ex, sr_ex = librosa.load(audio_file, sr=sr2)
    
    conv_start_index = round((start_index / sr1)*sr2)
    conv_end_index = round((end_index / sr1)*sr2)
    
    # 추출된 오디오 저장
    y_extracted = y_ex[conv_start_index:conv_end_index]

    # 추출된 오디오 원본 기준 시간

    # 파일 이름에 시작 시간을 포함하여 설정
    output_file = f"{tag}.mp3"
    sf.write(output_file, y_extracted, sr2, format='mp3')
    print("audio file saved!!!")

## timecode 컨버터 ###
def convert_time(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return "{:02d}:{:02d}:{:02d}".format(int(hours), int(minutes), int(seconds))


### 프레임 파인더 : y1 전체를 "프레임"으로 지정한 후, y2 에서 해당 프레임을 찾음
eye_type = "sahon"
ep_type = "blu"

eye_sahon_start = 1
eye_sahon_end = 55

eye_sword_start = 56
eye_sword_end = 168

eye_spin_start = 0
eye_spin_end = 0

eye_offset = 700

eye_len = 2000

SIM_MATCH = 0.7
SIM_OFFSET = 0.3

offset_need_lst = []

# 딕셔너리 불러오기
try:
    with open(f"{ep_type}_time.json", "r") as f:
        episode_time_dict = json.load(f)
except FileNotFoundError:
    episode_time_dict = {}


# 변환된 시간 저장
for ep_num in range(eye_sahon_start,13):
    episode_key = f"{ep_type}_ep{ep_num}"

    if(episode_time_dict[episode_key]["eye_match"] == "OFFSET_UNCORRECT"):
        offset_need_lst.append(ep_num)


for ep_num in offset_need_lst:

    # 두 음악 파일 로드
    audio_file1 = f"C:\\Users\\girin\\Desktop\\sub2dub\\movies\\audio_index\\eye_{eye_type}.mp3"
    audio_file2 = f"C:\\Users\\girin\Desktop\sub2dub\\movies\\audio_shana\\{ep_type}\\{ep_type}_{str(ep_num).zfill(3)}.mp3"


    # 샘플링 레이트 설정 (높을 수록 단위 샘플 많아짐, 시간 오래 걸림, 1000~44100(mp3))
    sampling_rate = 1000 # 실험결과 1000 정도가 적당
    sampling_rate_final = 44100

    max_sim_start_idx = episode_time_dict[episode_key]["eye_start_idx"] - eye_offset
    max_sim_end_idx = max_sim_start_idx+ eye_len

    save_mp3(tag=f"offset{eye_offset}_{ep_type}_ep{ep_num}_{eye_type}_{sampling_rate}", audio_file=audio_file2, start_index=max_sim_start_idx, end_index=max_sim_end_idx, sr1=sampling_rate, sr2=sampling_rate_final)