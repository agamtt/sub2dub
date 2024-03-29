
import json
from datetime import datetime, timedelta
import os
import re

### VIDEO READ ###

dub_path = r"C:\Users\girin\Desktop\이누야샤_영상\이누야샤_원본_한국어\이누야샤더빙(투니버스_토렌트)"
dub_video = {}
i = 1

for file_name in os.listdir(dub_path):  # 폴더 내 파일들에 대해 반복
    if os.path.isfile(os.path.join(dub_path, file_name)):  # 파일인지 확인
        dub_video[f"ep{i}"] = {"file_name": file_name, "path": os.path.join(dub_path,file_name)}
        i+=1

blu_path = r"C:\Users\girin\Desktop\이누야샤_영상\이누야샤_원본_일본어\이누야샤일어_블루레이(fullmetal)"
blu_video = {}
i = 1
files = os.listdir(blu_path)
pattern = re.compile(r"Inuyasha - (\d+)")
sorted_files = sorted(files, key=lambda x: int(pattern.search(x).group(1)))
for file_name in sorted_files:  # 폴더 내 파일들에 대해 반복
    if os.path.isfile(os.path.join(blu_path, file_name)):  # 파일인지 확인
        blu_video[f"ep{i}"] = {"file_name": file_name, "path": os.path.join(blu_path,file_name)}
        i+=1


    
### JSON READ ###

for ep_num in range(1,55+1):
    with open(r"C:\Users\girin\Desktop\sub2dub\blu_time.json", "r") as f:
      blu_eye_dict = json.load(f)

for ep_num in range(1,55+1):
    with open(r"C:\Users\girin\Desktop\sub2dub\dub_time.json", "r") as f:
      dub_eye_dict = json.load(f)

op_ed_dict = {
   "blu":{
      "op_end_ep1-ep55":"00:01:17.120",
      "ed_start_ep1-ep55":"00:21:51.640",
      },
   "dub":{
      "op_end_ep1-ep55":"00:01:29.960",
      "ed_start_ep1-ep55":"00:22:01.680",
      },
}

zero_time = "00:00:00.000"
big_time = "00:99:99.000"

blu_op_end = op_ed_dict["blu"]["op_end_ep1-ep55"]

blu_eye_start = blu_eye_dict["blu_ep1"]["eye_start"]+".000"
blu_eye_start_obj = datetime.strptime(blu_eye_start,"%H:%M:%S.%f")
blu_eye_len = 5.2 # sec
blu_eye_end_obj = blu_eye_start_obj + timedelta(seconds=blu_eye_len)
blu_eye_end = blu_eye_end_obj.strftime("%H:%M:%S.%f")[:-3]

blu_ed_start = op_ed_dict["blu"]["ed_start_ep1-ep55"]

dub_op_end = op_ed_dict["dub"]["op_end_ep1-ep55"]

dub_eye_start = dub_eye_dict["dub_ep1"]["eye_start"]+".000"
dub_eye_start_obj = datetime.strptime(dub_eye_start,"%H:%M:%S.%f")
dub_eye_start_obj += timedelta(seconds=0.5)
dub_eye_start = dub_eye_start_obj.strftime("%H:%M:%S.%f")[:-3]

dub_eye_len = 2.47 # sec
dub_eye_end_obj = dub_eye_start_obj + timedelta(seconds=dub_eye_len) 
dub_eye_end = dub_eye_end_obj.strftime("%H:%M:%S.%f")[:-3]

dub_ed_start = op_ed_dict["dub"]["ed_start_ep1-ep55"]

blu_video_name = blu_video[f"ep{1}"]["file_name"]
blu_video_path = blu_video[f"ep{1}"]["path"]

dub_video_name = dub_video[f"ep{1}"]["file_name"]
dub_video_path = dub_video[f"ep{1}"]["path"]


data = f'''<?xml version="1.0" standalone="no"?>
<mlt LC_NUMERIC="C" version="7.13.0" title="Shotcut version 22.12.21" producer="main_bin">
  <profile description="PAL 4:3 DV or DVD" width="1920" height="1080" progressive="1" sample_aspect_num="1" sample_aspect_den="1" display_aspect_num="16" display_aspect_den="9" frame_rate_num="25" frame_rate_den="1" colorspace="709"/>
  <playlist id="main_bin">
    <property name="xml_retain">1</property>
  </playlist>
  <producer id="black" in="{zero_time}" out="{big_time}">
    <property name="length">{big_time}</property>
    <property name="eof">pause</property>
    <property name="resource">0</property>
    <property name="aspect_ratio">1</property>
    <property name="mlt_service">color</property>
    <property name="mlt_image_format">rgba</property>
    <property name="set.test_audio">0</property>
  </producer>
  <playlist id="background">
    <entry producer="black" in="{zero_time}" out="{big_time}"/>
  </playlist>
  <chain id="chain0" out="{big_time}">
    <property name="length">{big_time}</property>
    <property name="eof">pause</property>
    <property name="resource">{dub_video_path}</property>
    <property name="mlt_service">avformat-novalidate</property>
    <property name="seekable">1</property>
    <property name="audio_index">1</property>
    <property name="video_index">0</property>
    <property name="mute_on_pause">0</property>
    <property name="shotcut:hash">8a43dda34c2826291200fe134d41c52b</property>
    <property name="shotcut:caption">{dub_video_name}</property>
    <property name="xml">was here</property>
  </chain>
  <chain id="chain1" out="{big_time}">
    <property name="length">{big_time}</property>
    <property name="eof">pause</property>
    <property name="resource">{dub_video_path}</property>
    <property name="mlt_service">avformat-novalidate</property>
    <property name="seekable">1</property>
    <property name="audio_index">1</property>
    <property name="video_index">0</property>
    <property name="mute_on_pause">0</property>
    <property name="shotcut:hash">8a43dda34c2826291200fe134d41c52b</property>
    <property name="shotcut:caption">{dub_video_name}</property>
    <property name="xml">was here</property>
  </chain>
  <playlist id="playlist0">
    <property name="shotcut:video">1</property>
    <property name="shotcut:name">V1</property>
    <blank length="00:00:00.160"/>
    <entry producer="chain0" in="{dub_op_end}" out="{dub_eye_start}"/>
    <entry producer="chain1" in="{dub_eye_end}" out="{dub_ed_start}"/>
  </playlist>
  <chain id="chain2" out="{big_time}">
    <property name="length">{big_time}</property>
    <property name="eof">pause</property>
    <property name="resource">{blu_video_path}</property>
    <property name="mlt_service">avformat-novalidate</property>
    <property name="seekable">1</property>
    <property name="audio_index">1</property>
    <property name="video_index">0</property>
    <property name="mute_on_pause">0</property>
    <property name="creation_time">2020-05-19T09:51:18</property>
    <property name="shotcut:hash">c3ddf5c49929f26db212675b18e285fb</property>
    <property name="shotcut:caption">[Fullmetal] Inuyasha - 01 [1080p][HEVC 10bits].mkv</property>
    <property name="xml">was here</property>
    <filter id="filter0" in="{blu_op_end}" out="{blu_eye_start}">
      <property name="background">color:#00000000</property>
      <property name="mlt_service">affine</property>
      <property name="shotcut:filter">affineSizePosition</property>
      <property name="transition.fill">1</property>
      <property name="transition.distort">0</property>
      <property name="transition.rect">998.679 0 683.321 511.071 1</property>
      <property name="transition.valign">middle</property>
      <property name="transition.halign">center</property>
      <property name="shotcut:animIn">00:00:00.000</property>
      <property name="shotcut:animOut">00:00:00.000</property>
      <property name="transition.threads">0</property>
    </filter>
  </chain>
  <chain id="chain3" out="{big_time}">
    <property name="length">{big_time}</property>
    <property name="eof">pause</property>
    <property name="resource">{blu_video_path}</property>
    <property name="mlt_service">avformat-novalidate</property>
    <property name="seekable">1</property>
    <property name="audio_index">1</property>
    <property name="video_index">0</property>
    <property name="mute_on_pause">0</property>
    <property name="creation_time">2020-05-19T09:51:18</property>
    <property name="shotcut:hash">c3ddf5c49929f26db212675b18e285fb</property>
    <property name="shotcut:caption">{blu_video_name}</property>
    <property name="xml">was here</property>
    <filter id="filter1" in="{blu_eye_end}" out="{blu_ed_start}">
      <property name="background">color:#00000000</property>
      <property name="mlt_service">affine</property>
      <property name="shotcut:filter">affineSizePosition</property>
      <property name="transition.fill">1</property>
      <property name="transition.distort">0</property>
      <property name="transition.rect">998.679 0 683.321 511.071 1</property>
      <property name="transition.valign">middle</property>
      <property name="transition.halign">center</property>
      <property name="shotcut:animIn">00:00:00.000</property>
      <property name="shotcut:animOut">00:00:00.000</property>
      <property name="transition.threads">0</property>
    </filter>
  </chain>
  <playlist id="playlist1">
    <property name="shotcut:video">1</property>
    <property name="shotcut:name">V2</property>
    <entry producer="chain2" in="{blu_op_end}" out="{blu_eye_start}"/>
    <entry producer="chain3" in="{blu_eye_end}" out="{blu_ed_start}"/>
  </playlist>
  <tractor id="tractor0" title="Shotcut version 22.12.21" in="00:00:00.000" out="00:20:29.480">
    <property name="shotcut">1</property>
    <property name="shotcut:projectAudioChannels">2</property>
    <property name="shotcut:projectFolder">1</property>
    <property name="shotcut:scaleFactor">0.074</property>
    <track producer="background"/>
    <track producer="playlist0"/>
    <track producer="playlist1"/>
    <transition id="transition0">
      <property name="a_track">0</property>
      <property name="b_track">1</property>
      <property name="mlt_service">mix</property>
      <property name="always_active">1</property>
      <property name="sum">1</property>
    </transition>
    <transition id="transition1">
      <property name="a_track">0</property>
      <property name="b_track">1</property>
      <property name="version">0.1</property>
      <property name="mlt_service">frei0r.cairoblend</property>
      <property name="threads">0</property>
      <property name="disable">1</property>
    </transition>
    <transition id="transition2">
      <property name="a_track">0</property>
      <property name="b_track">2</property>
      <property name="mlt_service">mix</property>
      <property name="always_active">1</property>
      <property name="sum">1</property>
    </transition>
    <transition id="transition3">
      <property name="a_track">1</property>
      <property name="b_track">2</property>
      <property name="version">0.1</property>
      <property name="mlt_service">frei0r.cairoblend</property>
      <property name="threads">0</property>
      <property name="disable">0</property>
    </transition>
  </tractor>
</mlt>'''

with open(r"C:\Users\girin\Desktop\이누야샤_영상\shotcut_프로젝트\자동편집\test.mlt", "w", encoding="utf-8") as f:
    f.write(data)