import librosa
import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf

def save_mp3(tag, audio_file, start_index, end_index, sr1=1000, sr2=44100):
    y_ex, sr_ex = librosa.load(audio_file, sr=sr2)
    
    conv_start_index = int((start_index / sr1)*sr2)
    conv_end_index = int((end_index / sr1)*sr2)
    
    # 추출된 오디오 저장
    y_extracted = y_ex[conv_start_index:conv_end_index]

    # 파일 이름에 시작 시간을 포함하여 설정
    output_file = f"{tag}_{conv_start_index}_{conv_end_index}.mp3"
    sf.write(output_file, y_extracted, sr2, format='mp3')

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

'''반복기'''
for i in range(0, len(y1)- frame_size + 1, frame_size):
    src_start_idx = i
    src_end_idx = i + frame_size
    idx_diff = src_end_idx - src_start_idx

    frame = y1[i:i+frame_size]
    max_similarity = 0
    max_index = -1
    cosine_similarity = []
    for j in range(len(y2) - frame_size + 1):
        window = y2[j:j+frame_size]
        similarity = np.dot(frame, window) / (np.linalg.norm(frame) * np.linalg.norm(window))
        cosine_similarity.append(similarity)

    ## 시각화
    # plt.plot(np.arange(len(cosine_similarity)) / sampling_rate, cosine_similarity)
    # plt.title(f'Frame_Index : {i}')
    # plt.xlabel('Time (seconds)')
    # plt.ylabel('Cosine Similarity')
    # plt.show()

    # 재생
    max_sim_start_idx = np.argmax(cosine_similarity)
    max_sim_end_idx = max_sim_start_idx+idx_diff

    ## 시간 계산
    start_time = src_start_idx / sampling_rate
    end_time = src_end_idx / sampling_rate

    print(f"idx : {0} {start_time} : {end_time}")

    # # 첫 번째 음악 파일의 일부분을 MP3 파일로 저장
    save_mp3("audio1",audio_file1, src_start_idx, src_end_idx)

    # # 두 번째 음악 파일의 일부분을 MP3 파일로 저장
    save_mp3("audio2",audio_file2, max_sim_start_idx, max_sim_end_idx)


''' Unit Test'''

'''
src_start_idx = 80000
src_end_idx = 84000
idx_diff = src_end_idx - src_start_idx

frame = y1[src_start_idx:src_end_idx]

max_similarity = 0
max_index = -1
cosine_similarity = []
for j in range(len(y2) - frame_size + 1):
    window = y2[j:j+frame_size]
    similarity = np.dot(frame, window) / (np.linalg.norm(frame) * np.linalg.norm(window))
    cosine_similarity.append(similarity)

## 시각화
plt.plot(np.arange(len(cosine_similarity)) / sampling_rate, cosine_similarity)
plt.title(f'Frame_Index : {0}')
plt.xlabel('Time (seconds)')
plt.ylabel('Cosine Similarity')
plt.show()

# 재생
max_sim_start_idx = np.argmax(cosine_similarity)
max_sim_end_idx = max_sim_start_idx+idx_diff

## 시간 계산
start_time = src_start_idx / sampling_rate
end_time = src_end_idx / sampling_rate

print(f"idx : {0} {start_time} : {end_time}")

# # 첫 번째 음악 파일의 일부분을 MP3 파일로 저장
save_mp3("audio1",audio_file1, src_start_idx, src_end_idx)

# # 두 번째 음악 파일의 일부분을 MP3 파일로 저장
save_mp3("audio2",audio_file2, max_sim_start_idx, max_sim_end_idx)
'''