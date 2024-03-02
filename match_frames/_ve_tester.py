import video_editor as ve

folder_path =  r'C:\Users\girin\Desktop\sub2dub\movies\test_ep38'
filename_only_origin = "dup38.mp4"
filename_only_edited = "dup38_edited.mp4"

video_filename_origin = ve.get_full_path(folder_path,filename_only_origin)
video_filename_edited = ve.get_full_path(folder_path,filename_only_edited)

ve.cd(folder_path)

ve.cut_and_combine(video_filename_origin,video_filename_edited,483,500,1000,4000)

