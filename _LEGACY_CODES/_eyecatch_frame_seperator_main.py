'''
프로세스 : 영상 내에서 특정 이미지(eyecatch) 가  위치한 프레임을 출력한다.
를 멀티 스레드로 실행하는 main.py
'''

import video_sepatator
import img_compare
import csv
import os
import subprocess
import threading

def run_command(cmd):
    # 명령어 실행
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE)

    # 명령어 실행 결과를 실시간으로 출력
    for line in iter(process.stdout.readline, b''):
        print(line.decode('utf-8').strip())

    # 명령어 실행 결과를 모두 출력한 후 프로세스 종료
    process.stdout.close()
    process.wait()

os.chdir(os.path.dirname(os.path.abspath(__file__)))

cmds=[]
for i in range(1,3):
    cmds.append(f'python _eyecatch_frame_seperator_thread.py {i}')

# 각 명령어를 별도의 쓰레드로 실행
threads = []
for cmd in cmds:
    thread = threading.Thread(target=run_command, args=(cmd,))
    threads.append(thread)
    thread.start()

# 모든 쓰레드의 종료를 기다림
for thread in threads:
    thread.join()