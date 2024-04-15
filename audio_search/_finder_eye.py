import librosa
import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import json
import re
from collections import OrderedDict

DRAW_PLT = False # 유사도 그래프 출력 토글


### MP3 파일로 저장 ### 

def save_mp3(tag, audio_file, start_index, end_index, sr1, sr2):
    y_ex, sr_ex = librosa.load(audio_file, sr=sr2)
    
    conv_start_index = round((start_index / sr1)*sr2)
    conv_end_index = round((end_index / sr1)*sr2)
    
    # 추출된 오디오 저장
    y_extracted = y_ex[conv_start_index:conv_end_index]

    # 추출된 오디오 원본 기준 시간

    # 파일 이름에 시작 시간을 포함하여 설정
    output_file = f"{tag.split()[0]}_{tag.split()[2]}.mp3"
    sf.write(output_file, y_extracted, sr2, format='mp3')
    print("audio file saved!!!")

## timecode 컨버터 ###
def convert_time(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return "{:02d}:{:02d}:{:02d}".format(int(hours), int(minutes), int(seconds))

def update_episode_time_dict(episode_time_dict, episode_key, cosine_similarity, sampling_rate, time_code_searched, max_sim_start_idx, eye_len_sec, ep_type, eye_type, match_status, audio_file2, max_sim_end_idx, sampling_rate_final, eye_offset=None, start_time=None):
    episode_time_dict[episode_key]["eye_sim"] = str(max(cosine_similarity))
    episode_time_dict[episode_key]["eye_sampling_rate"] = sampling_rate
    episode_time_dict[episode_key]["eye_searched_start_time"] = time_code_searched
    episode_time_dict[episode_key]["eye_searched_start_idx"] = int(max_sim_start_idx)
    episode_time_dict[episode_key]["eye_len_sec"] = eye_len_sec[f"eye_{ep_type}_{eye_type}_len_sec"]
    episode_time_dict[episode_key]["eye_match"] = match_status
    episode_time_dict[episode_key]["eye_type"] = eye_type
    episode_time_dict[episode_key]["eye_offset"] = eye_offset
    episode_time_dict[episode_key]["eye_start_time"] = start_time
    print(match_status)
    save_mp3(tag=f"{match_status}{ep_type}_ep{ep_num}_{eye_type}_{sampling_rate}", audio_file=audio_file2, start_index=max_sim_start_idx, end_index=max_sim_end_idx, sr1=sampling_rate, sr2=sampling_rate_final)


### 프레임 파인더 : y1 전체를 "프레임"으로 지정한 후, y2 에서 해당 프레임을 찾음

''' 전역상수 '''
###################

eye_type = "spin_ep106"
ep_type = "dub"

ep_eye_type = {
    "eye_sahon_start" : 1,
    "eye_sahon_end" : 55,
    "eye_sword_start" : 56,
    "eye_sword_end" : 168,
    "eye_spin_start" : 0,
    "eye_spin_end" : 0,

}

eye_len = 2000
eye_len_sec = {
    "eye_blu_sahon_len_sec" : 6.4,
    "eye_blu_sahon_from_ep9_len_sec" : 6.4,
    "eye_blu_sword_len_sec" : 0,
    "eye_blu_spin_len_sec" : 0,

    "eye_dub_sahon_ep1_len_sec" : 0,
    "eye_dub_sahon_len_sec" : 0,
    "eye_dub_sahon_ep9_len_sec" : 0,
    "eye_dub_sword_len_sec" : 0,
    "eye_dub_spin_len_sec" : 0,
    "eye_dub_spin_ep106_len_sec" : 0,
}

SIM_MATCH = 0.7
SIM_OFFSET = 0.3

#####################

print(f"PROGRAM START : {eye_type}")

for ep_num in range(126,127):

    # 두 음악 파일 로드
    audio_file1 = f"C:\\Users\\girin\\Desktop\\sub2dub\\movies\\audio_index\\{ep_type}_eye_{eye_type}.mp3"
    audio_file2 = f"C:\\Users\\girin\Desktop\sub2dub\\movies\\audio_shana\\{ep_type}\\{ep_type}_{str(ep_num).zfill(3)}.mp3"

    # 샘플링 레이트 설정 (높을 수록 단위 샘플 많아짐, 시간 오래 걸림, 1000~44100(mp3))
    sampling_rate = 1000 # 실험결과 1000 정도가 적당
    sampling_rate_final = 44100

    # 음악 파일을 librosa를 사용하여 로드하고, 음악 데이터와 샘플링 주파수를 가져옴
    y1, sr1 = librosa.load(audio_file1, sr=sampling_rate)
    y2, sr2 = librosa.load(audio_file2, sr=sampling_rate)

    ''' 물리량 정의 '''

    # 첫번째 파일의 길이 (초 단위)
    length_audio1 = len(y1) / sampling_rate

    # 두번째 파일의 길이 (초 단위)
    length_audio2 = len(y2) / sampling_rate

    ## 오디오 파일로 저장할 최소 Thresh hold
    ## 실측 결과, 0.7 이상이여야 매칭 프레임임.
    save_sim_thresh = 0.7

    ''' 계산 수행 '''

    frame = y1[:] # y1 전체
    max_similarity = 0 # 최대 유사도 선언
    max_index = -1 # 최대 유사도인 인덱스 선언 (초기값은 -1)
    cosine_similarity = [] # 코사인 유사도 리스트 선언 (최댓값 계산용)
    #print(f"y2 탐색 : {0}~{len(y2) - frame_size}")
    for j in range(0 ,len(y2) - len(y1) + 1,1): # y2 를 step 1로 순회(전수조사)
        window = y2[j:j+len(y1)] # 윈도우 : 프레임 사이즈와 동일
        similarity = np.dot(frame, window) / (np.linalg.norm(frame) * np.linalg.norm(window)) # y1 frame 과 y2 window 의 유사도를 계산
        cosine_similarity.append(similarity) # 코사인 유사도 리스트에 저장

    ## 시각화

    # 코사인 유사도 리스트의 값을 그래프로 그린다. (하나의 프레임에 대해 출력됨)
    if(DRAW_PLT==True):
        plt.plot(np.arange(len(cosine_similarity)) / sampling_rate, cosine_similarity)
        plt.title(f'Frame_Finder')
        plt.xlabel('Time (seconds)')
        plt.ylabel('Cosine Similarity')
        plt.show()

    ## 코사인 유사도가 최대인 인덱스를 추출 (시작~끝 : 매칭된 윈도우)
    max_sim_start_idx = np.argmax(cosine_similarity)
    max_sim_end_idx = max_sim_start_idx+ eye_len

    time_code_searched = convert_time(max_sim_start_idx/sampling_rate)

    print(f"EPISODE : {ep_num}")
    print(f"cosine_sim_max : {max(cosine_similarity)}")
    print(f"searched_index : {max_sim_start_idx}")
    print(f"serched_time  : {time_code_searched}")


    # 딕셔너리에 에피소드와 시간 저장
    try:
        with open(f"{ep_type}_eye_time.json", "r") as f:
            episode_time_dict = json.load(f, object_pairs_hook=OrderedDict)
    except Exception as e:
        episode_time_dict = {}

    
    # 변환된 시간 저장
    episode_key = f"{ep_type}_ep{ep_num}"

    if episode_key not in episode_time_dict:
        episode_time_dict[episode_key] = {}

    ## 딕셔너리 편집 및 파일 저장
    
    if(max(cosine_similarity)>SIM_MATCH):
        update_episode_time_dict(episode_time_dict, episode_key, cosine_similarity, sampling_rate, time_code_searched, max_sim_start_idx, eye_len_sec, ep_type, eye_type, f"MATCHED : {eye_type}", audio_file2, max_sim_end_idx, sampling_rate_final, eye_offset=None, start_time=time_code_searched)
        print(f"MATCHED : {eye_type}")

    elif(max(cosine_similarity)>=SIM_OFFSET):
        if("eye_match" in episode_time_dict[episode_key]):
            if(episode_time_dict[episode_key]["eye_match"][:7] != "MATCHED"):
                update_episode_time_dict(episode_time_dict, episode_key, cosine_similarity, sampling_rate, time_code_searched, max_sim_start_idx, eye_len_sec, ep_type, eye_type, f"OFFSET_UNCORRECT : {eye_type}", audio_file2, max_sim_end_idx, sampling_rate_final, eye_offset=None, start_time=None)
                print(f"OFFSET_UNCORRECT : {eye_type}")
            else:
                print("Already Matched, PASS")
        else:
            update_episode_time_dict(episode_time_dict, episode_key, cosine_similarity, sampling_rate, time_code_searched, max_sim_start_idx, eye_len_sec, ep_type, eye_type, f"OFFSET_UNCORRECT : {eye_type}", audio_file2, max_sim_end_idx, sampling_rate_final, eye_offset=None, start_time=None)
            print(f"OFFSET_UNCORRECT : {eye_type}")
            

    elif(max(cosine_similarity)<SIM_OFFSET):
        if("eye_match" in episode_time_dict[episode_key]):
            if(episode_time_dict[episode_key]["eye_match"][:7] != "MATCHED"):
                update_episode_time_dict(episode_time_dict, episode_key, cosine_similarity, sampling_rate, time_code_searched, max_sim_start_idx, eye_len_sec, ep_type, eye_type, f"MISS : {eye_type}", audio_file2, max_sim_end_idx, sampling_rate_final, eye_offset=None, start_time=None)
                print(f"MISS : {eye_type}")
            else:
                print("Already Matched, PASS")
        else:
            update_episode_time_dict(episode_time_dict, episode_key, cosine_similarity, sampling_rate, time_code_searched, max_sim_start_idx, eye_len_sec, ep_type, eye_type, f"MISS : {eye_type}", audio_file2, max_sim_end_idx, sampling_rate_final, eye_offset=None, start_time=None)
            print(f"MISS : {eye_type}")

    with open(f"{ep_type}_eye_time.json", "w") as f:
        sorted_keys = sorted(episode_time_dict.keys(), key=lambda x: int(re.search(r'\d+', x).group()))
        sorted_data = {key: episode_time_dict[key] for key in sorted_keys}
        #print(sorted_keys)
        json.dump(sorted_data, f, indent=4)