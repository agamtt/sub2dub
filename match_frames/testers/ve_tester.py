from custom_lib import video_editor as ve
from custom_lib import file_handler as fh

folder_path = r'C:\Users\girin\Desktop\sub2dub\movies\test_ep38'

fileinfo = {
    "dub_origin" : {"name":"dub38", "format":"mp4", "full_path":""},
    "dub_edited" : {"name":"dub38_edited", "format":"mp4", "full_path":""},
    "blu_origin" : {"name":"blu38", "format":"mp4", "full_path":""},
    "output" : {"name":"output", "format":"mp4", "full_path":""},
}

fh.init_path(parent_folder_path=folder_path, fileinfo_dict=fileinfo)

#print(fileinfo)
'''
video_clips = [
    ve.cut_video(fileinfo["dub_origin"]["full_path"], 0, 10),
    ve.cut_video(fileinfo["blu_origin"]["full_path"], 0, 5),
    ve.cut_video(fileinfo["dub_origin"]["full_path"], 5, 15),
]

ve.concat_subclip(video_clips,fileinfo["output"]["full_path"])
'''

cutinfo = {
    "video_path": fileinfo["blu_origin"]["full_path"],
    "insert_video_path": fileinfo["dub_origin"]["full_path"],
    "cuts" : [
        {"part":1, "start_time":0, "end_time": 10, "used": True},
        {"part":2, "start_time":10, "end_time": 20, "used": False},
        {"part":3, "start_time":20, "end_time": 30, "used": True},
    ],
    "insert" : [
        {"part":1, "start_time":0, "end_time": 10, "used": False},
        {"part":2, "start_time":10, "end_time": 20, "used": True},
        {"part":3, "start_time":20, "end_time": 30, "used": False},
    ]
}

ve.edit_by_cutinfo(cutinfo, fileinfo["output"]["full_path"])