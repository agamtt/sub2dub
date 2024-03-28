import librosa
import numpy as np
import matplotlib.pyplot as plt

# 두 음악 파일 로드
audio_file1 = r"C:\Users\girin\Desktop\sub2dub\movies\audio_extracked\blu_ep1_event_peaceful.mp3"
audio_file2 = r"C:\Users\girin\Desktop\sub2dub\movies\audio_extracked\dub_ep1_range_contain_peaceful.mp3"

sampling_rate = 1000

# 음악 파일을 librosa를 사용하여 로드하고, 음악 데이터와 샘플링 주파수를 가져옴
y1, sr1 = librosa.load(audio_file1, sr=sampling_rate)  # 샘플링 레이트를 None으로 설정하여 원본 샘플링 레이트로 로드
y2, sr2 = librosa.load(audio_file2, sr=sampling_rate)

print("audio loaded!")

# 코사인 유사도 계산
cosine_similarity = []
window_size = len(y1)  # 첫 번째 오디오 신호의 길이를 윈도우 크기로 설정

# 두 번째 오디오를 첫 번째 오디오와 동일한 길이의 윈도우로 이동하며 코사인 유사도를 계산
for i in range(len(y2) - window_size + 1):
    window = y2[i:i+window_size]
    similarity = np.dot(y1, window) / (np.linalg.norm(y1) * np.linalg.norm(window))
    cosine_similarity.append(similarity)
    print(f"calc : {i}")

# 시각화
plt.plot(np.arange(len(cosine_similarity)) / sampling_rate, cosine_similarity)
plt.title('Cosine Similarity between two audio signals')
plt.xlabel('Time (seconds)')
plt.ylabel('Cosine Similarity')
plt.show()
