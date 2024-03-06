from custom_lib import video_editor as ve

#print(ve.ctos("18:53:20:06"))


# print(ve.frame_to_timecode(158)) # 일치
# print(ve.frame_to_timecode(67)) # 일치

# print(ve.frame_to_timecode(85)) # 1 불일치
'''
for i in range(75,100):
    print(f"{i} : {ve.frame_to_timecode(i)}") # 1 불일치
'''
p=None
for frame in range(0,120):
    if(p==ve.frame_to_timecode_decimal(frame)):
        print(f"ya! : {frame}")
    print(f"frame : {frame} / {ve.frame_to_timecode_decimal(frame)}")
    p = ve.frame_to_timecode(frame)

