import cv2
import os
import shutil


####
def make_and_move_to_folder(folder_path):
    os.makedirs(folder_path, exist_ok=True)
    os.chdir(folder_path)

def video_sepatate_to_dir(filename,dirname):
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    print(os.listdir())  

    vidcap = cv2.VideoCapture(filename)
    fps = vidcap.get(cv2.CAP_PROP_FPS)
    total_frames = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))

    make_and_move_to_folder(f"{dirname}")

    for i in range(0, total_frames):
        # 비디오의 현재 위치 설정
        vidcap.set(cv2.CAP_PROP_POS_FRAMES, i)

        # 프레임 읽기
        ret, frame = vidcap.read()

        # 이미지 파일 저장하기
        cv2.imwrite(f'{i}.jpg',frame)
        print(f"saved img : {i}")

    # 비디오 파일 닫기
    vidcap.release()


def rm_sep_dir(filename):
   shutil.rmtree(f"{filename}+sep")