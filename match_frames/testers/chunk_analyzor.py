import matplotlib.pyplot as plt
import json

from custom_lib import video_editor as ve
from custom_lib import file_handler as fh
from custom_lib import video_comparator as vc
from custom_lib import image_compare as ic
from custom_lib import video_editor as ve


json_save_path_blu_ep1 = r"C:\Users\girin\Desktop\sub2dub\sub2dub\match_frames\movie_json\chunk_test_blu_ep1.json"
json_save_path_dub_ep1 = r"C:\Users\girin\Desktop\sub2dub\sub2dub\match_frames\movie_json\chunk_test_dub_ep1.json"

## sim 을 계산한 후, json으로 저장
vc.chunk_finder_by_shift(r"C:\Users\girin\Desktop\sub2dub\movies\img_sep_temp\blu_ep1_cfr",json_save_path_blu_ep1)
vc.chunk_finder_by_shift(r"C:\Users\girin\Desktop\sub2dub\movies\img_sep_temp\dub_ep1_cfr",json_save_path_dub_ep1)
'''
# json을 읽어서 points 에 저장
with open(json_save_path, 'r') as json_file:
    data = json.load(json_file)



# 튜플로 좌표를 나타내는 리스트 생성
#points = [(1, 5), (2, 7), (3, 9), (4, 11), (5, 13)]
points = data
# x값과 y값을 추출하여 리스트로 변환
x_values = [point[0] for point in points]
y_values = [point[1] for point in points]

# 그래프 그리기
plt.plot(x_values, y_values, marker='o', linestyle='-')

# 그래프 제목 및 축 라벨 설정
plt.title('Scatter Plot with Tuple Coordinates')

# x 축의 눈금과 라벨 제거
plt.xticks([])

# 그래프 보이기
plt.show()


'''
