import cv2
import os


def get_diff(img1,img2):
    diff = cv2.subtract(img1, img2)
    result = not diff.any()
    return result

os.chdir(os.path.dirname(os.path.abspath(__file__)))
comp_img1 = cv2.imread('1blu94.jpg', cv2.IMREAD_GRAYSCALE)
comp_img2 = cv2.imread('1blu.mkv+sepImgDir/45.jpg', cv2.IMREAD_GRAYSCALE)

res = cv2.matchTemplate(comp_img1, comp_img2, cv2.TM_CCOEFF_NORMED)
similarity = res.max()
#print(f"diff : {get_diff(comp_img1,comp_img2)}")
print(f"sim : {similarity}")
