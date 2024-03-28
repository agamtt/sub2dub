import librosa
import numpy as np
import soundfile as sf

# 두 음악 파일 로드
audio_file1 = r"C:\Users\girin\Desktop\sub2dub\movies\audio_extracked\blu_ep1_event_peaceful.mp3"
audio_file2 = r"C:\Users\girin\Desktop\sub2dub\movies\audio_extracked\dub_ep1_range_contain_peaceful.mp3"

sampling_rate = 44100

# 음악 파일을 librosa를 사용하여 로드하고, 음악 데이터와 샘플링 주파수를 가져옴
y1, sr1 = librosa.load(audio_file1, sr=sampling_rate)
y2, sr2 = librosa.load(audio_file2, sr=sampling_rate)

chunk_size = 1024
window_size = 512

matching_indices = []
for i in range(0, len(y1) - chunk_size, window_size):
    chunk = y1[i:i+chunk_size]
    best_match_index = np.argmax([np.dot(chunk, y2[j:j+chunk_size]) for j in range(0, len(y2) - chunk_size, window_size)])
    matching_indices.append(best_match_index)
    print(f"calc : {chunk}")

new_audio = np.concatenate([y2[i:i+chunk_size] for i in matching_indices])

sf.write('new_audio.mp3', new_audio, sr2, format='mp3')
