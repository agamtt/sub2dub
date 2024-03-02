'''
_dub_edit_frame_index.csv 를 parsing 하여 해당 프레임대로 영상을 잘라내고 잘린 영상을 반환한다.

csv 형식 : 시작프레임,첫 아이캐치프레임, 아이캐치 길이, 엔딩프레임

'''

import video_editor as ve
import csv, os

filename = "_dub_edit_frame_index.csv"
os.chdir(os.path.dirname(os.path.abspath(__file__)))
with open(filename, "r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if(len(row)!=0):
            ep_num=int(row[0])
            fr_after_op = int(row[1]) #오프닝을 포함하면 안됨
            fr_start_eyecatch = int(row[2]) # 첫 아이캐치 프레임
            fr_end_eyecatch = int(row[2])+80 #아이캐치를 포함하면 안됨 / 아이캐치 길이
            fr_before_ending = 0 # 첫 엔딩 프레임
            try:
                ve.cut_and_combine_to_end(f'[SHANA]dub_tor_{ep_num}.mp4',f'shana+cut_{ep_num}dub.mp4',fr_after_op,fr_start_eyecatch,fr_end_eyecatch,fr_before_ending)
            except Exception as e:
                print(f"ve.cut_and_combine ERROR : {e}")

## no csv

# for i in range(1,5):
#     ve.cut_and_combine(f'{i}dub.mp4',f'cut_{i}dub.mp4',ve.frtoTC(773),ve.frtoTC(2033),ve.frtoTC(2287),ve.frtoTC(2465))

# print("every jobs DONE!")