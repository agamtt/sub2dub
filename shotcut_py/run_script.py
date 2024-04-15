import subprocess
import os

# 실행할 스크립트 파일 경로
script_path = r"C:\Users\girin\Desktop\sub2dub\sub2dub\shotcut_py\shotcut_automation.py"

# 명령줄 인자로 사용할 에피소드 번호 범위 설정
episode_numbers = range(1, 5)  # 예를 들어, 1부터 167까지

# 각 에피소드 번호에 대해 스크립트 실행
for ep_num in episode_numbers:
    command = ["python", script_path, str(ep_num)]
    subprocess.run(command)

input("모든 에피소드 처리 완료. 대기")
