from custom_lib import file_handler as fh
from custom_lib import image_compare as ic


folder_path =  r'C:\Users\girin\Desktop\sub2dub\movies\test_ep38'
filename_only_src = "blu_img1.png"
filename_only_target = "dub_img1.png"
filename_only_target_little_diff = "dub_img1_little_diff.png"
filename_only_target_total_diff = "dub_img1_total_diff.png"


src = fh.get_full_path(folder_path,filename_only_src)
target = fh.get_full_path(folder_path,filename_only_target)
target_little_diff = fh.get_full_path(folder_path,filename_only_target_little_diff)
target_total_diff = fh.get_full_path(folder_path,filename_only_target_total_diff)

print(ic.get_sim_sift_print(src,src))
print(ic.get_sim_sift_print(src,target))
print(ic.get_sim_sift_print(src,target_little_diff))
print(ic.get_sim_sift_print(src,target_total_diff))