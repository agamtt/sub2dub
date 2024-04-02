import json

type = "blu"

json_file = f"{type}_time.json"

for ep_num in range(2,167):
    # 딕셔너리에 에피소드와 시간 저장
    try:
        with open(json_file, "r") as f:
            episode_time_dict = json.load(f)
    except FileNotFoundError:
        episode_time_dict = {}


    # 변환된 시간 저장
    episode_key = f"{type}_ep{ep_num}"

    # if episode_key not in episode_time_dict:
    #     episode_time_dict[episode_key] = {}

    # try:
    #     del episode_time_dict[episode_key]["eye_end_match"]
    # except:
    #     pass
    #episode_time_dict[f"blu_ep{ep_num}"]["ed_start"] = episode_time_dict[f"blu_ep{ep_num}"]["op_end"]
    #episode_time_dict[episode_key]["eye_type"] = "sword"
    # if episode_time_dict[episode_key].get("ed_type") == "DeepWoods":
    #     episode_time_dict[episode_key]["ed_start"]="00:22:10.640"
    #     print("set!")

    with open(json_file, "w") as f:
        json.dump(episode_time_dict, f, indent=4) 