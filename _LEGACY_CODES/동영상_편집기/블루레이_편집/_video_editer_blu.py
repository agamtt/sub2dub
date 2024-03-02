
import video_editor as ve
import csv, os

filename = "_blu_edit_frame_index.csv"
os.chdir(os.path.dirname(os.path.abspath(__file__)))
with open(filename, "r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if(len(row)!=0):
            ep_num=int(row[0])
            fr_after_op = int(row[1])
            fr_start_eyecatch = int(row[2])
            # fr_end_eyecatch = int(row[2])+134+202
            fr_end_eyecatch = int(row[2])+134
            fr_before_ending = int(row[3])
            try:
                ve.cut_and_combine(f'[SHANA]{ep_num}blu.mp4',f'shana+cut_{ep_num}blu.mp4',fr_after_op,fr_start_eyecatch,fr_end_eyecatch,fr_before_ending)
            except Exception as e:
                print(f"ve.cut_and_combine ERROR blu : {e}")

## no csv

# for i in range(1,5):
#     ve.cut_and_combine(f'{i}dub.mp4',f'cut_{i}dub.mp4',ve.frtoTC(773),ve.frtoTC(2033),ve.frtoTC(2287),ve.frtoTC(2465))

# print("every jobs DONE!")