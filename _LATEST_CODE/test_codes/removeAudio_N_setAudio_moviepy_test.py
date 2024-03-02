'''
moviepy 를 이용하여 영상에서 mp3 를 추출할 수 있는지 테스트.
AudioFileClip() 을 이용하여 mp4 -> mp3 로 convert 하면 된다.

'''


from moviepy.editor import *

video = VideoFileClip("이누야샤더빙1_짧은.mp4")
video = video.set_audio(None)

new_audio = AudioFileClip("더빙음성1테스트.mp3")

final_clip = video.set_audio(new_audio)
final_clip.write_videofile("음성합성테스트1.mp4")

#음성이 더 길면, 동영상 마지막으로 가면 영상이 멈추고 소리가 계속 나온다(최종길이 : 큰 파일 기준)
