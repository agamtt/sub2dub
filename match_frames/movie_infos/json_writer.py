
import json


'''
fileinfo = {
    "dub_origin" : {"name":"dub38", "format":"mp4", "full_path":""},
    "dub_edited" : {"name":"dub38_edited", "format":"mp4", "full_path":""},
    "blu_origin" : {"name":"blu38", "format":"mp4", "full_path":""},
    "output" : {"name":"output", "format":"mp4", "full_path":""},
}

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
with open('cutinfo_hand.json', 'w') as f:
    json.dump(cutinfo, f)
'''


# 파일에서 딕셔너리 불러오기
with open('cutinfo_hand_data.json', 'r') as f:
    loaded_dictionary = json.load(f)

print(loaded_dictionary)