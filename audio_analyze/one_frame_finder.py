import librosa
import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt

# 두 음악 파일 로드
audio_file1 = r"C:\Users\girin\Desktop\sub2dub\movies\audio_extracked\blu_ep1_event_peaceful.mp3"
audio_file2 = r"C:\Users\girin\Desktop\sub2dub\movies\audio_extracked\dub_ep1_range_contain_peaceful.mp3"

# 정보 적음
sampling_rate = 1000

# 정보 많음
sampling_rate_high = 44100

# 음악 파일을 librosa를 사용하여 로드하고, 음악 데이터와 샘플링 주파수를 가져옴
y1, sr1 = librosa.load(audio_file1, sr=sampling_rate)
y2, sr2 = librosa.load(audio_file2, sr=sampling_rate)

chunk_size = 1024
window_size = len(y1)

matching_indices = []
cosine_similarity = []

for i in range(len(y2) - window_size + 1):
    window = y2[i:i+window_size]
    similarity = np.dot(y1, window) / (np.linalg.norm(y1) * np.linalg.norm(window))
    cosine_similarity.append(similarity)

# 시각화
plt.plot(np.arange(len(cosine_similarity)) / sampling_rate, cosine_similarity)
plt.title('Cosine Similarity between two audio signals')
plt.xlabel('Time (seconds)')
plt.ylabel('Cosine Similarity')
plt.show()

max_index = np.argmax(cosine_similarity)

# 첫번째 파일의 길이 (초 단위)
length_audio1 = len(y1) / sampling_rate

# 두번째 파일의 길이 (초 단위)
length_audio2 = len(y2) / sampling_rate

# 가장 유사한 부분의 시작과 끝 시간 계산
start_time = max_index / sampling_rate
end_time = (max_index + len(y1)) / sampling_rate


print("First audio file length:", length_audio1, "seconds")
print("Second audio file length:", length_audio2, "seconds")
print("Start time:", start_time, "seconds")
print("End time:", end_time, "seconds")
print("Second Extract Len:", start_time-end_time)

y_ex, sr_ex = librosa.load(audio_file2, sr=44100)

# 새로운 음악 파일로 저장할 시간 범위 설정
start_index = int(start_time * sr2)
end_index = int(end_time * sr2)

# y2를 44100Hz로 열어서 해당 시간 범위만 추출
start_index = int(start_time * sampling_rate_high)
end_index = int(end_time * sampling_rate_high)
y2_extracted, sr2_extracted = librosa.load(audio_file2, sr=sampling_rate_high, offset=start_time, duration=end_time-start_time)

sf.write('new_audio.mp3', y2_extracted, 44100 , format='mp3')