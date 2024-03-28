from custom_lib import video_editor as ve
from custom_lib import file_handler as fh
from custom_lib import video_comparator as vc
from custom_lib import image_compare as ic
from custom_lib import video_editor as ve

folder_path = r'C:\Users\girin\Desktop\sub2dub\movies\test_ep'
img_output_path = r'C:\Users\girin\Desktop\sub2dub\movies\img_sep_temp'
json_path = r'C:\Users\girin\Desktop\sub2dub\sub2dub\match_frames\movie_json'

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
    "frame_tester" : {"name":"frame_tester_blu_ep1_cfr25_abs", "format":"mp4", "full_path":""},
    
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

### vc.image_array_comparator(img_output_path,"C","D",sim_thresh=15)
#print(ic.get_sim_sift_noprint(r"C:\Users\girin\Desktop\sub2dub\movies\img_sep_temp\A\0.jpg",r"C:\Users\girin\Desktop\sub2dub\movies\img_sep_temp\B\0.jpg"))

#vc.shift_frame_finder_by_sift(img_output_path,"D",30)

#vc.seperate_video_N_save_img_label(fileinfo["frame_tester"]["full_path"],img_output_path,"frame_test_blu_ep1_cfr25_abs")
#vc.seperate_video_N_save_img_label(fileinfo["dub_ep1_cfr"]["full_path"],img_output_path,"dub_ep1_cfr")


## image seperation test...

# ic.calc_sim_pixel_keypoint(r"C:\Users\girin\Desktop\sub2dub\movies\img_sep_temp\blu_ep1_cfr\48.jpg")
# ic.calc_sim_pixel_keypoint(r"C:\Users\girin\Desktop\sub2dub\movies\img_sep_temp\blu_ep1_cfr\49.jpg")

## image to video test...

#ve.images_to_video(r"C:\Users\girin\Desktop\sub2dub\movies\img_sep_temp\blu_ep1_cfr","output_blu_ep1_sqeuntial.mp4",fps=25)

'''
puzzle algorithm test
'''

#ic.get_sim_sift_imshow(r"C:\Users\girin\Desktop\sub2dub\movies\img_sep_temp\blu_ep1_cfr\25.jpg",r"C:\Users\girin\Desktop\sub2dub\movies\img_sep_temp\blu_ep1_cfr\67.jpg")

#ic.get_sim_sift_imshow(r"C:\Users\girin\Desktop\sub2dub\movies\img_sep_temp\blu_ep1_cfr\311.jpg",r"C:\Users\girin\Desktop\sub2dub\movies\img_sep_temp\dub_ep1_cfr\300.jpg")

#vc.search_and_swap(r"C:\Users\girin\Desktop\sub2dub\movies\img_sep_temp\blu_ep1_cfr",r"C:\Users\girin\Desktop\sub2dub\movies\img_sep_temp\dub_ep1_cfr",r"C:\Users\girin\Desktop\sub2dub\movies\img_sep_temp\output_ep1")

'''
chunk algorithm test
'''

#vc.chunk_finder_by_sift(r"C:\Users\girin\Desktop\sub2dub\movies\img_sep_temp\blu_ep1_cfr")

'''
audio
'''
#ve.extract_audio_from_vid(r"C:\Users\girin\Desktop\sub2dub\movies\test_ep\dub_ep1_cfr.mp4",r"C:\Users\girin\Desktop\sub2dub\movies\test_ep\dub_ep1_cfr_audio.mp3")