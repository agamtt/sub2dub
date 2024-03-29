import json

for ep_num in range(1,55+1):
    # 딕셔너리에 에피소드와 시간 저장
    try:
        with open("episode_time_dict.json", "r") as f:
            episode_time_dict = json.load(f)
    except FileNotFoundError:
        episode_time_dict = {}


    # 변환된 시간 저장
    episode_key = f"blu_ep{ep_num}"

    if episode_key not in episode_time_dict:
        episode_time_dict[episode_key] = {}

    episode_time_dict[episode_key]["eye_type"] = "ep1"

    with open("episode_time_dict.json", "w") as f:
        json.dump(episode_time_dict, f, indent=4) 