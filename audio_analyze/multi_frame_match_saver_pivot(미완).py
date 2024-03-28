import librosa
import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf

### MP3 파일로 저장 ### 

def save_mp3(tag, audio_file, frame_number, sim, start_index, end_index, sr1=1000, sr2=44100):
    y_ex, sr_ex = librosa.load(audio_file, sr=sr2)
    
    conv_start_index = int((start_index / sr1)*sr2)
    conv_end_index = int((end_index / sr1)*sr2)
    
    # 추출된 오디오 저장
    y_extracted = y_ex[conv_start_index:conv_end_index]

    # 파일 이름에 시작 시간을 포함하여 설정
    output_file = f"{frame_number}_{tag}_{sim}.mp3"
    sf.write(output_file, y_extracted, sr2, format='mp3')


### 프레임 파인더 : 음성을 "프레임"으로 등분하고, 프레임끼리의 음성의 유사도를 기준으로 매칭 프레임을 탐색

# 두 음악 파일 로드
audio_file1 = r"C:\Users\girin\Desktop\sub2dub\movies\audio_extracked\blu_ep1_cfr_audio.mp3"
audio_file2 = r"C:\Users\girin\Desktop\sub2dub\movies\audio_extracked\dub_ep1_cfr_audio.mp3"
# audio_file1 = r"C:\Users\girin\Desktop\sub2dub\movies\audio_extracked\blu_ep1_event_peaceful.mp3"
# audio_file2 = r"C:\Users\girin\Desktop\sub2dub\movies\audio_extracked\dub_ep1_range_contain_peaceful.mp3"

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

frame_second = 2 # 프레임길이(초) 성능을 위해 10
frame_size = int(frame_second * sampling_rate)
matching_indices = []

# 초반 오프닝 불일치를 적용한 성능 향상 또는 실험을 위한 시작 프레임 설정기능 (기본값=0)
pre_start_sec = 90
pre_start_idx = pre_start_sec*sampling_rate

## 오디오 파일로 저장할 최소 Thresh hold
## 실측 결과, 0.7 이상이여야 매칭 프레임임.
save_sim_thresh = 0.7 

''' 계산 수행 '''

start = 0 # 백트래킹 스타트
for i in range(pre_start_idx, len(y1)- frame_size + 1, frame_size): # y1 을 frame 기준으로 순회 / step : frame_size >> 1로 하기?

    frame_num = int(i/frame_size)

    src_start_idx = i # 현재 프레임의 시작 인덱스
    src_end_idx = i + frame_size # 현재 프레임의 끝 인덱스

    frame = y1[i:i+frame_size] # 프레임 : y1 을 등분

    max_similarity = 0 # 최대 유사도 선언
    max_index = -1 # 최대 유사도인 인덱스 선언 (초기값은 -1)
    cosine_similarity = [] # 코사인 유사도 리스트 선언 (최댓값 계산용)

    ''' 
    피벗: 
    1) 피벗 탐색(일치 탐색)
        우선, 각 프레임에 대해 윈도우를 조사한 후, 기준(피벗)으로 삼을 프레임을 정한다.
        피벗 프레임과 피벗 윈도우는 완벽한 매칭이라고 가정,

        피벗 프레임과 피벗 윈도우의 차이만큼 y2를 평행이동
    2) 불일치 탐색
        

    '''

    print(f"y2 탐색 : {start}~{len(y2) - frame_size}")
    for j in range(start ,len(y2) - frame_size + 1,1): # y2 를 step 1로 순회(전수조사)  
        window = y2[j:j+frame_size] # 윈도우 : 프레임 사이즈와 동일
        similarity = np.dot(frame, window) / (np.linalg.norm(frame) * np.linalg.norm(window)) # y1 frame 과 y2 window 의 유사도를 계산
        cosine_similarity.append(similarity) # 코사인 유사도 리스트에 저장

    '''
    실측 결과, 
    코사인 유사도는 frame 크기에 크게 영향을 받음.

    매칭 실패 프레임의 경우, 전체 윈도우에서 유사도 0.3 미만 (sample_rate:1000, frame_size=2sec) 약 15초 소요
    매칭 실패 프레임의 경우, 전체 윈도우에서 유사도 0.01 미만 (sample_rate:1000, frame_size=10sec)

    매칭 성공 프레임의 경우,
    '''

    ## 시각화
    
    # 코사인 유사도 리스트의 값을 그래프로 그린다. (하나의 프레임에 대해 출력됨)
    # plt.plot(np.arange(len(cosine_similarity)) / sampling_rate, cosine_similarity)
    # plt.title(f'Frame_Index : {i}')
    # plt.xlabel('Time (seconds)')
    # plt.ylabel('Cosine Similarity')
    # plt.show()

    ## 코사인 유사도가 최대인 인덱스를 추출 (시작~끝 : 매칭된 윈도우)
    max_sim_start_idx = np.argmax(cosine_similarity)
    max_sim_end_idx = max_sim_start_idx+ frame_size

    ## 시간 계산 (인간 확인용)
    start_time = src_start_idx / sampling_rate
    end_time = src_end_idx / sampling_rate

    print(f"y1 frame_num : {frame_num}")
    print(f"y1 time : {0} {start_time} : {end_time}")

    print(f"cosine_sim_max : {max(cosine_similarity)}")

    if(max(cosine_similarity)>save_sim_thresh):
        # # 첫 번째 음악 파일의 일부분을 MP3 파일로 저장
        save_mp3("audio1",audio_file1, frame_num, max(cosine_similarity),  src_start_idx, src_end_idx, sr1=sampling_rate, sr2=sampling_rate_final)

        # # 두 번째 음악 파일의 일부분을 MP3 파일로 저장
        save_mp3("audio2",audio_file2, frame_num, max(cosine_similarity), max_sim_start_idx, max_sim_end_idx, sr1=sampling_rate, sr2=sampling_rate_final)

        print("audio saved!!!")

        # # 백트래킹 변수 : 매칭 프레임 인덱스에서 한 프레임 전부터 탐색 시작
        start = max_sim_start_idx - frame_size