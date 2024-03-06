import cv2
import os
from custom_lib import image_compare as ic
import shutil
import matplotlib.pyplot as plt
import json
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


'''
<<puzzle algorithm>>
swap blu frame image <=> dub frame image
backtracking : look ahead N frame, break when there is no matched frame

프레임이 일대일 대응하지 않아서 (false-positive 즉, 다른프레임과의 일치율이 더 높은 경우가 나타나서)
청크 방식으로 해보는 중.
'''
def copy_and_rename_file_idx(src_file_path, dest_folder_path, idx, label):
    # 파일을 새로운 폴더로 복사

    new_filename = f"{idx}_{label}.jpg"
    dest_file_path = os.path.join(dest_folder_path, new_filename)

    shutil.copy(src_file_path, dest_file_path)

def search_and_swap(blu_img_folder_path, dub_img_folder_path, output_folder_path, sim_thresh=20, index_frame_num=3369, input_lookahead_limit=10, lookahead_offset=0):
    blu_img_basename_list = sorted(os.listdir(blu_img_folder_path), key=lambda x: int(x.split('.')[0]))
    dub_img_basename_list = sorted(os.listdir(dub_img_folder_path), key=lambda x: int(x.split('.')[0]))
    output_img_idx = 0

    if not os.path.exists(output_folder_path): # 비교 결과를 저장할 폴더 (없으면) 생성
        os.makedirs(output_folder_path)

    index_frame = os.path.join(blu_img_folder_path,f"{index_frame_num}.jpg")
    max_sim = 0
    max_sim_idx = 0

    for dub_img in dub_img_basename_list:
        dub_img_path = os.path.join(dub_img_folder_path,dub_img)
        dub_idx = dub_img.split('.')[0]
        sim = ic.get_sim_sift_imshow(index_frame,dub_img_path)
        print(f"initial_search / index frame : {index_frame} / {dub_img_path} / {sim}")
        
        if(sim>max_sim):
            max_sim = sim
            max_sim_idx = dub_idx

    for blu_img_basename in blu_img_basename_list:
        blu_img_idx = blu_img_basename.split('.')[0]
        blu_img_path = os.path.join(blu_img_folder_path,blu_img_basename)

        for lookahead in range(0,lookahead_limit):
            pair_dub_img_basename = f"{blu_img_idx+lookahead+lookahead_offset}.jpg"
            pair_dub_img_path = os.path.join(dub_img_folder_path,pair_dub_img_basename)
            pair_dub_img_idx = int(pair_dub_img_basename.split('.')[0])
            
            sim = ic.get_sim_sift_noshow(blu_img_path,pair_dub_img_path)
            print(f"{blu_img_path} / {pair_dub_img_path} / {sim} / limit:{lookahead}")

            if(sim>sim_thresh): # frame matched
                print("frame matched!")
                copy_and_rename_file_idx(src_file_path=pair_dub_img_path, dest_folder_path=output_folder_path, idx=output_img_idx, label="dub")
                output_img_idx += 1
                # lookahead_offset 을 조정하는 코드
                lookahead_limit = input_lookahead_limit
                lookahead_offset = abs(pair_dub_img_idx-blu_img_idx)
                break
            elif(sim==-1):
                print("black screen found...")
                copy_and_rename_file_idx(src_file_path=blu_img_path, dest_folder_path=output_folder_path, idx=output_img_idx, label="blu")
                output_img_idx += 1
                break
            
            if(lookahead==lookahead_limit-1): # if no matched frame up to the lookahead
                print("no matched frame up to the lookahead")
                copy_and_rename_file_idx(src_file_path=blu_img_path, dest_folder_path=output_folder_path, idx=output_img_idx, label="blu")
                output_img_idx += 1
        
'''
chunk analyzing
'''
def chunk_finder_by_shift(img_folder_path, json_save_path, sim_thresh=50):

    frame_list = sorted(os.listdir(img_folder_path), key=lambda x: int(x.split('.')[0]))
    
    prev_file_path = None
    
    chunk_list = []
    for frame in frame_list:
        frame_path = os.path.join(img_folder_path, frame)
        if(prev_file_path): # 바로 이전 프레임이 존재할때만
            # 비교 로직 작성
            try:
                sim_shift = ic.get_sim_sift_noshow(prev_file_path,frame_path)
                print(f"현재:{frame} / sim_sift : {sim_shift}")

                chunk_list.append((frame, sim_shift)) # 그래프용 좌표

                if(sim_shift<sim_thresh): # 실측 시 화면 전환 thresh : 약 50
                    #sim_shift = ic.get_sim_sift_imshow(prev_file_path,frame_path)
                    print(f"shift frame : {frame}")

            except Exception as e:
                print(e)

        prev_file_path = frame_path
    

    with open(json_save_path, 'w') as json_file:
        json.dump(chunk_list, json_file)
        print(f"json saved : {json_save_path}")

    return chunk_list


#def chunk_generator(json_path):
