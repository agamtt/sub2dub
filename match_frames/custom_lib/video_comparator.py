import cv2
import os
from custom_lib import image_compare as ic
'''
seperating by frame require cfr (fixed frame encoded)
use shana encoder to encode video
'''

def seperate_video(video_path):
    vidcap = cv2.VideoCapture(video_path)
    fps = vidcap.get(cv2.CAP_PROP_FPS)
    total_frames = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))

    for i in range(0, total_frames):
        vidcap.set(cv2.CAP_PROP_POS_FRAMES, i)
        success, frame = vidcap.read()
        cv2.imshow("Frame", frame)
        #cv2.imwrite(f'{i}.jpg',frame)
        #print(f"saved img : {i}")
        cv2.waitKey(100)
        cv2.destroyAllWindows()

    # 비디오 파일 닫기
    vidcap.release()

def seperate_video_N_save_img(video_path,output_dir):

    vidcap = cv2.VideoCapture(video_path)
    fps = vidcap.get(cv2.CAP_PROP_FPS)
    total_frames = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))

    for i in range(0, total_frames):
        vidcap.set(cv2.CAP_PROP_POS_FRAMES, i)
        success, frame = vidcap.read()
        output_full_path = os.path.join(output_dir,f'{i}.jpg') 
        cv2.imwrite(output_full_path,frame)
        print(f"saved img : {output_full_path}")

    # 비디오 파일 닫기
    vidcap.release()

def seperate_video_N_save_img_label(video_path,output_dir,label):

    os.makedirs(os.path.join(output_dir, label), exist_ok=True)

    vidcap = cv2.VideoCapture(video_path)
    fps = vidcap.get(cv2.CAP_PROP_FPS)
    total_frames = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))

    for i in range(0, total_frames):
        vidcap.set(cv2.CAP_PROP_POS_FRAMES, i)
        success, frame = vidcap.read()
        output_full_path = os.path.join(output_dir,label,f'{i}.jpg') 
        cv2.imwrite(output_full_path,frame)
        print(f"saved img : {output_full_path}")

    # 비디오 파일 닫기
    vidcap.release()

def seperate_video_N_compare_to_saved_img(src_video_path,src_img_path):

    vidcap = cv2.VideoCapture(src_video_path)
    fps = vidcap.get(cv2.CAP_PROP_FPS)
    total_frames = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))

    for i in range(total_frames):
        vidcap.set(cv2.CAP_PROP_POS_FRAMES, i)
        success, frame = vidcap.read()
        if success:
            for img_filename in os.listdir(src_img_path):
                img_path = os.path.join(src_img_path, img_filename)
                if os.path.isfile(img_path):
                    print(ic.get_sim_sift_noprint(frame, img_path))

    # 비디오 파일 닫기
    vidcap.release()

def image_array_comparator(img_root_path, first_label ,second_label, sim_thresh):
    folder_A_path = os.path.join(img_root_path,first_label)
    folder_B_path = os.path.join(img_root_path,second_label)

    files_A = sorted(os.listdir(folder_A_path), key=lambda x: int(x.split('.')[0]))

    files_B = sorted(os.listdir(folder_B_path), key=lambda x: int(x.split('.')[0]))

    for file_A in files_A:
        file_A_path = os.path.join(folder_A_path, file_A)
        print(f"A 파일: {file_A_path}")
        for file_B in files_B:
            file_B_path = os.path.join(folder_B_path, file_B)
            print(f"B 파일: {file_B_path}")
            sim = ic.get_sim_sift_imshow(file_A_path,file_B_path,60)
            if(sim>sim_thresh):
                #print(f"sim_thresh : {sim_thresh}, break!")
                pass
                #break

def shift_frame_printer(img_root_path, first_label):
    folder_A_path = os.path.join(img_root_path,first_label)
    files_A = sorted(os.listdir(folder_A_path), key=lambda x: int(x.split('.')[0]))
    
    prev_file_A_path = None

    for file_A in files_A:
        file_A_path = os.path.join(folder_A_path, file_A)
        if(prev_file_A_path):
            # 비교 로직 작성
            sim = ic.get_sim_sift_noshow(prev_file_A_path,file_A_path)
            print(f"현재:{file_A} / sim : {sim}")
        prev_file_A_path = file_A_path

def shift_frame_finder_by_sift(img_root_path, first_label, sim_thresh):
    folder_A_path = os.path.join(img_root_path,first_label)
    files_A = sorted(os.listdir(folder_A_path), key=lambda x: int(x.split('.')[0]))
    
    prev_file_A_path = None

    for file_A in files_A:
        file_A_path = os.path.join(folder_A_path, file_A)
        if(prev_file_A_path):
            # 비교 로직 작성
            sim = ic.get_sim_sift_noshow(prev_file_A_path,file_A_path)
            print(f"현재:{file_A} / sim : {sim}")

            if(sim<sim_thresh): # 실측 시 화면 전환 thresh : 약 50
                print(f"shift frame : {file_A}")

        prev_file_A_path = file_A_path


'''
chunk analyzing
'''

#def chunk_generator(json_path):
