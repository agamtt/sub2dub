import os
import json

def get_full_path(video_folder_path,video_filename_only):
    video_filename = os.path.join(video_folder_path,video_filename_only)
    return video_filename

def get_full_path_N_format(video_folder_path, video_filename_only, file_format):
    video_filename = os.path.join(video_folder_path, video_filename_only)
    return f"{video_filename}.{file_format}"

def init_path(parent_folder_path,fileinfo_dict):
    for key, value in fileinfo_dict.items():
        name = value["name"]
        file_format = value["format"]
        full_path = get_full_path_N_format(parent_folder_path, name, file_format)
        value["full_path"] = full_path

def cd_pwd(): # change dir as pwd
    current_file_path = os.path.abspath(__file__)
    current_dir_path = os.path.dirname(current_file_path)
    os.chdir(current_dir_path)

def make_and_move_to_folder(folder_path):
    os.makedirs(folder_path, exist_ok=True)
    os.chdir(folder_path)

def rmdir(folder_path):
    try:
        # 폴더 삭제
        os.rmdir(folder_path)
        print(f"폴더 '{folder_path}'가 삭제되었습니다.")
    except OSError as e:
        print(f"폴더 삭제 실패: {e}")

## os.chdir wrapper
def cd(dir):
    os.chdir(dir)

'''
json and dict handlers
'''

def json_reader(json_file_path):
    with open('data.json', 'r') as f:
         return json.load(f)
    
# def json_init(json_file_dir):
