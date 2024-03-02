'''
프로세스 : 영상 내에서 특정 이미지(eyecatch) 가  위치한 프레임을 출력한다.
requirement : video_seperator
'''

import video_sepatator
import img_compare
import csv
import os
import sys



# for i in range(1,3):
#     VIDEO_FILENAME = f"{i}dub.mp4"
#     SEP_DIRNAME = f"{VIDEO_FILENAME}+sepImgDir"
#     ## 비디오 검출
#     video_sepatator.video_sepatate_to_dir(VIDEO_FILENAME,SEP_DIRNAME)

VIDEO_FILENAME = f"{sys.argv[1]}blu.mkv"
SEP_DIRNAME = f"{VIDEO_FILENAME}+sepImgDir"
## 비디오 검출
video_sepatator.video_sepatate_to_dir(VIDEO_FILENAME,SEP_DIRNAME)
