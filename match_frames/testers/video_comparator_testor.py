from custom_lib import video_editor as ve
from custom_lib import file_handler as fh
from custom_lib import video_comparator as vc
from custom_lib import image_compare as ic

folder_path = r'C:\Users\girin\Desktop\sub2dub\movies\test_ep38'
img_output_path = r'C:\Users\girin\Desktop\sub2dub\movies\img_sep_temp'

fileinfo = {
    "dub_origin" : {"name":"dub38", "format":"mp4", "full_path":""},
    "dub_edited" : {"name":"dub38_edited", "format":"mp4", "full_path":""},
    "blu_origin" : {"name":"blu38", "format":"mp4", "full_path":""},

    "blu_miroku_fixed_frame" : {"name":"blu_miroku_cfr", "format":"mp4", "full_path":""},
    "dub_miroku_fixed_frame" : {"name":"dub_miroku_cfr", "format":"mp4", "full_path":""},

    "blu_fixed_frame" : {"name":"blu38_cfr25", "format":"mp4", "full_path":""},
    "blu_kagome" : {"name":"kagome", "format":"mp4", "full_path":""},
    "output" : {"name":"output", "format":"mp4", "full_path":""},

    "blu_ep1_cfr" : {"name":"blu_ep1_cfr", "format":"mp4", "full_path":""},
    "dub_ep1_cfr" : {"name":"dub_ep1_cfr", "format":"mp4", "full_path":""},
    
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
'''

#vc.seperate_video_N_save_img_label(fileinfo["blu_miroku_fixed_frame"]["full_path"],img_output_path,"A")
#vc.seperate_video_N_save_img_label(fileinfo["blu_kagome"]["full_path"],img_output_path,"kagome")

#vc.image_array_comparator(img_output_path,"C","D",sim_thresh=15)
#print(ic.get_sim_sift_noprint(r"C:\Users\girin\Desktop\sub2dub\movies\img_sep_temp\A\0.jpg",r"C:\Users\girin\Desktop\sub2dub\movies\img_sep_temp\B\0.jpg"))

#vc.shift_frame_finder(img_output_path,"kagome",50)

vc.seperate_video_N_save_img_label(fileinfo["blu_ep1_cfr"]["full_path"],img_output_path,"blu_ep1_cfr")
vc.seperate_video_N_save_img_label(fileinfo["dub_ep1_cfr"]["full_path"],img_output_path,"dub_ep1_cfr")
