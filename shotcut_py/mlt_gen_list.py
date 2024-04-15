
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
blu_dict_file = r"C:\Users\girin\Desktop\sub2dub\blu_merged_time.json"
with open(blu_dict_file, "r") as f:
  blu_dict = json.load(f)

dub_dict_file = r"C:\Users\girin\Desktop\sub2dub\dub_merged_time.json"
with open(dub_dict_file, "r") as f:
  dub_dict = json.load(f)

zero_time = "00:00:00.000"
big_time = "00:99:99.000"

### Mlt Gen ###

for ep in range(1,168):
  blu_op_end = blu_dict[f"blu_ep{ep}"]["op_end"]

  blu_eye_start = blu_dict[f"blu_ep{ep}"]["eye_start_time"]+".000"
  blu_eye_start_obj = datetime.strptime(blu_eye_start,"%H:%M:%S.%f")
  blu_eye_len = blu_dict[f"blu_ep{ep}"]["eye_len_sec"]
  blu_eye_end_obj = blu_eye_start_obj + timedelta(seconds=blu_eye_len)
  blu_eye_end = blu_eye_end_obj.strftime("%H:%M:%S.%f")[:-3]

  blu_ed_start = blu_dict[f"blu_ep{ep}"]["ed_start"]

  dub_op_end = dub_dict[f"dub_ep{ep}"]["op_end"]

  dub_eye_start = dub_dict[f"dub_ep{ep}"]["eye_start_time"]+".000"
  dub_eye_start_obj = datetime.strptime(dub_eye_start,"%H:%M:%S.%f")

  dub_eye_start = dub_eye_start_obj.strftime("%H:%M:%S.%f")[:-3]

  dub_eye_len = dub_dict[f"dub_ep{ep}"]["eye_len_sec"]
  dub_eye_end_obj = dub_eye_start_obj + timedelta(seconds=dub_eye_len)
  dub_eye_end = dub_eye_end_obj.strftime("%H:%M:%S.%f")[:-3]

  dub_ed_start = dub_dict[f"dub_ep{ep}"]["ed_start"]

  blu_video_name = blu_video[f"ep{ep}"]["file_name"]
  blu_video_path = blu_video[f"ep{ep}"]["path"]

  dub_video_name = dub_video[f"ep{ep}"]["file_name"]
  dub_video_path = dub_video[f"ep{ep}"]["path"]

  ### eyecatch fade effect

  dub_fadeout_forward_start = f'{(datetime.strptime(dub_eye_start,"%H:%M:%S.%f") + timedelta(seconds=-1)).strftime("%H:%M:%S.%f")[:-3]}'
  dub_fadeout_forward_end = f"{dub_eye_start}"

  dub_fadeout_backword_start = f"{dub_eye_start}"
  dub_fadeout_backword_end = f'{(datetime.strptime(dub_eye_start,"%H:%M:%S.%f") + timedelta(seconds=+1)).strftime("%H:%M:%S.%f")[:-3]}'


  print("#############")
  print(blu_video_name)
  print(dub_video_name)
  print("#############")

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
      <property name="shotcut:hash"></property>
      <property name="shotcut:caption">{dub_video_name}</property>
      <property name="xml">was here</property>
      <filter id="filter0" out="{dub_fadeout_forward_end}">
        <property name="start">1</property>
        <property name="level">{dub_fadeout_forward_start}=1;{dub_fadeout_forward_end}=0</property>
        <property name="mlt_service">brightness</property>
        <property name="shotcut:filter">fadeOutBrightness</property>
        <property name="alpha">1</property>
        <property name="shotcut:animOut">70</property>
      </filter>
      <filter id="filter1" out="{dub_fadeout_forward_end}">
        <property name="window">75</property>
        <property name="max_gain">20dB</property>
        <property name="level">{dub_fadeout_forward_start}=0;{dub_fadeout_forward_end}=-60</property>
        <property name="mlt_service">volume</property>
        <property name="shotcut:filter">fadeOutVolume</property>
        <property name="shotcut:animOut">70</property>
      </filter>
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
      <property name="shotcut:hash"></property>
      <property name="shotcut:caption">{dub_video_name}</property>
      <property name="xml">was here</property>
      <filter id="filter2" in="00:15:53.520" out="00:20:32.000">
        <property name="start">1</property>
        <property name="level">00:00:00.000=0;00:00:02.640=1</property>
        <property name="mlt_service">brightness</property>
        <property name="shotcut:filter">fadeInBrightness</property>
        <property name="alpha">1</property>
        <property name="shotcut:animIn">67</property>
      </filter>
      <filter id="filter3" in="00:15:53.520" out="00:20:32.000">
        <property name="window">75</property>
        <property name="max_gain">20dB</property>
        <property name="level">00:00:00.000=-60;00:00:02.640=0</property>
        <property name="mlt_service">volume</property>
        <property name="shotcut:filter">fadeInVolume</property>
        <property name="shotcut:animIn">67</property>
      </filter>
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
      <property name="shotcut:hash"></property>
      <property name="shotcut:caption">{blu_video_name}</property>
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
      <property name="shotcut:hash"></property>
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
      <track producer="playlist1" hide="audio"/>
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

  with open(f"C:\\Users\\girin\Desktop\\이누야샤_영상\shotcut_프로젝트\\자동편집\\ep_{ep}.mlt", "w", encoding="utf-8") as f:
      f.write(data)