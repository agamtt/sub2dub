import json
import re
from collections import OrderedDict


blu_ep_type = "blu"
blu_eye_dict = {}

## 블루레이 아이캐치 딕셔너리 불러오기

with open(f"{blu_ep_type}_eye_time.json", "r") as f:
    blu_eye_dict = json.load(f, object_pairs_hook=OrderedDict)

## 테스트
#print(blu_eye_dict["blu_ep1"])

blu_opep_time_dict_filename = "blu_opep_time"
blu_opep_time_dict = {}

with open(f"{blu_opep_time_dict_filename}.json", "r") as f:
    blu_opep_time_dict = json.load(f, object_pairs_hook=OrderedDict)

merged_blu_dict = {}

for ep in range(1,2):
    print(blu_eye_dict[f"blu_ep{ep}"])
    print()
    print(blu_opep_time_dict[f"blu_ep{ep}"])




## 저장
# with open(f"{ep_type}_eye_time.json", "w") as f:
#     sorted_keys = sorted(episode_time_dict.keys(), key=lambda x: int(re.search(r'\d+', x).group()))
#     sorted_data = {key: episode_time_dict[key] for key in sorted_keys}
#     #print(sorted_keys)
#     json.dump(sorted_data, f, indent=4)