from custom_lib import video_editor as ve

#print(ve.ctos("18:53:20:06"))


# print(ve.frame_to_timecode(158)) # 일치
# print(ve.frame_to_timecode(67)) # 일치

# print(ve.frame_to_timecode(85)) # 1 불일치
'''
for i in range(75,100):
    print(f"{i} : {ve.frame_to_timecode(i)}") # 1 불일치
'''


num = [93,94,81,82]
for i in num:
    #print(f"{num} : {ve.frame_to_timecode(num)}")
    ve.frame_to_timecode_tester(i)
