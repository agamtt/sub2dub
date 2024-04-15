import json
import re
from collections import OrderedDict
from enum import Enum

blu_ep_type = "blu"
blu_eye_dict = {}
## 블루레이 아이캐치 딕셔너리 불러오기
with open(f"{blu_ep_type}_eye_time.json", "r") as f:
    blu_eye_dict = json.load(f, object_pairs_hook=OrderedDict)

## 테스트
#print(blu_eye_dict["blu_ep1"])

blu_op_dict = {
    "blu_intro" : {
        "start" : 1,
        "end" : 34,
        "time" : "00:01:17:02"
    },
    "I_AM" : {
        "start" : 35,
        "end" : 64,
        "time" : "00:01:36:01"
    },
    "Endless" : {
        "start" : 65,
        "end" : 95,
        "time" : "00:01:36:01"
    },
    "Grip" : {
        "start" : 96,
        "end" : 127,
        "time" : "00:02:00:01"
    },
    "Special-I_AM" : {
        "start" : 128,
        "end" : 128,
        "time" : "00:01:36:01"
    },
    "new_intro" : {
        "start" : 129,
        "end" : 153,
        "time" : "00:01:36:02"
    },
    "Angelus" : {
        "start" : 154,
        "end" : 167,
        "time" : "00:02:00:01"
    },
}

blu_ed_dict = {
    "MyWill" : {
        "start" : 1,
        "end" : 20,
        "time" : "00:21:51.640"
    },
    "DeepWoods" : {
        "start" : 21,
        "end" : 41,
        "time" : "00:21:51.640"
    },
    "Dearest" : {
        "start" : 42,
        "end" : 60,
        "time" : "00:22:10"
    },
    "TruePoetry" : {
        "start" : 61,
        "end" : 108,
        "time" : "00:22:10.000"
    },
    "ItasuraNaKiss" : {
        "start" : 109,
        "end" : 127,
        "time" : "00:22:10.000"
    },
    "Come" : {
        "start" : 128,
        "end" : 146,
        "time" : "00:20:42.000"
    },
    "TheTruthUntold" : {
        "start" : 147,
        "end" : 166,
        "time" : "00:24:40.000"
    },
    "Special" : {
        "start" : 167,
        "end" : 167,
        "time" : "00:21:04.000"
    },
}

op_end_time_dict = {
    "blu_intro" : "00:01:17:02"
}


## 오프닝 엔딩 시간 업데이트
merged_blu_dict = {}

for key, value in blu_op_dict.items():
    start_value = value.get("start")
    end_value = value.get("end")
    for ep in range(start_value,end_value+1):
        blu_eye_dict[f"blu_ep{ep}"]["op_type"] = key
        blu_eye_dict[f"blu_ep{ep}"]["op_start"] = blu_op_dict[key]["time"]

for key, value in blu_ed_dict.items():
    start_value = value.get("start")
    end_value = value.get("end")
    for ep in range(start_value,end_value+1):
        blu_eye_dict[f"blu_ep{ep}"]["ed_type"] = key
        blu_eye_dict[f"blu_ep{ep}"]["ed_start"] = blu_ed_dict[key]["time"]

## 저장
with open(f"{blu_ep_type}_merged_time.json", "w") as f:
    # sorted_keys = sorted(blu_eye_dict.keys(), key=lambda x: int(re.search(r'\d+', x).group()))
    # sorted_data = {key: blu_eye_dict[key] for key in sorted_keys}
    # #print(sorted_keys)
    json.dump(blu_eye_dict, f, indent=4)