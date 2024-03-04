import os
import cv2
import json

'''
get image file and return similarity
'''

def calc_sim_sift(src_img_path,target_img_path):
    # get img_file as grayscale (sift algorithm require grayscale img)
    src_img = cv2.imread(src_img_path, cv2.IMREAD_GRAYSCALE)
    target_img = cv2.imread(target_img_path, cv2.IMREAD_GRAYSCALE)

    # get kp and des by sift algorithm
    sift = cv2.SIFT_create()
    kp1, des1 = sift.detectAndCompute(src_img, None)
    kp2, des2 = sift.detectAndCompute(target_img, None)

    # match the points by BFMatcher algorithm
    bf = cv2.BFMatcher()
    matches = bf.knnMatch(des1, des2, k=2)

    good_matches = []
    for m, n in matches:
        if m.distance < 0.75 * n.distance:
            good_matches.append(m)

    # estimete sim by num of good_matches
    similarity = len(good_matches) / max(len(des1), len(des2)) * 100
    return similarity, kp1, kp2, good_matches

# wrapper of get_sim_sift, print BFMatcher Map
def get_sim_sift_imshow(src_img_path, target_img_path, img_size):
    similarity, kp1, kp2, good_matches = calc_sim_sift(src_img_path, target_img_path)

    # print BFMatcher Map
    src_img = cv2.imread(src_img_path)
    target_img = cv2.imread(target_img_path)
    result = cv2.drawMatches(src_img, kp1, target_img, kp2, good_matches, None, flags=2)

    # 이미지 크기 조절
    scale_percent = img_size  # 크기를 조절하려는 퍼센트
    width = int(result.shape[1] * scale_percent / 100)
    height = int(result.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized_result = cv2.resize(result, dim, interpolation=cv2.INTER_AREA)

    cv2.imshow("BFMatcher Map", resized_result)
    print(f"similarity : {similarity}")

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return similarity

def get_sim_sift_noshow(src_img_path, target_img_path):
    similarity, kp1, kp2, good_matches = calc_sim_sift(src_img_path, target_img_path)
    
    return similarity

'''
rgb pixel keypoint based algorithm
'''
#def calc_sim_pixel_keypoint(src_img_path,target_img_path):
def calc_sim_pixel_keypoint(src_img_path):

    image = cv2.imread(src_img_path)

    x = 100
    y = 200
    pixel_value = image[y, x]

    print(f"{pixel_value}")
    
    # Draw a circle to mark the point on the image
    image_with_point = image.copy()
    cv2.circle(image_with_point, (x, y), 5, (0, 255, 0), -1)  # Green circle with radius 5

    # Display the image with marked point
    cv2.imshow('Image with Marked Point', image_with_point)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


'''
def get_first_img_num(dirname):
    file_list = os.listdir(dirname)
    file_number_list = [int(file_name.split(".")[0]) for file_name in file_list]
    return min(file_number_list)

def get_last_img_num(dirname):
    file_list = os.listdir(dirname)
    file_number_list = [int(file_name.split(".")[0]) for file_name in file_list]
    return max(file_number_list)

def write_json(dict,dest):
    json_data = json.dumps(dict)
    # 파일에 JSON 데이터 쓰기
    with open(dest, "w") as f:
        f.write(json_data)


def find_similar_images(template_path, target_path):
    # 이미지 파일을 grayscale로 불러오기
    template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
    target = cv2.imread(target_path, cv2.IMREAD_GRAYSCALE)

    # SIFT 알고리즘을 이용하여 특징점과 기술자 추출
    sift = cv2.SIFT_create()
    kp1, des1 = sift.detectAndCompute(template, None)
    kp2, des2 = sift.detectAndCompute(target, None)

    # BFMatcher 알고리즘을 이용하여 두 이미지의 특징점 매칭
    bf = cv2.BFMatcher()
    matches = bf.knnMatch(des1, des2, k=2)

    # 매칭된 특징점을 거리순으로 정렬
    good_matches = []
    for m, n in matches:
        if m.distance < 0.75 * n.distance:
            good_matches.append(m)

    # 일치하는 특징점의 개수로 이미지 유사도 계산
    similarity = len(good_matches) / max(len(des1), len(des2)) * 100

    # 이미지 출력
    # result = cv2.drawMatches(template, kp1, target, kp2, good_matches, None, flags=2)
    # cv2.imshow("Similarity", result)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    return similarity


INDEX_FILENAME = "dub_eyecatch_start.jpg"
THRESH_SIM=50

# 에피소드번호와 찾은 이미지번호를 저장할 dict 선언
ep_dict={}

for ep in range(1,4):
    VIDEO_FILENAME = f"{ep}dub_test.mp4"
    SEP_DIRNAME = f"{VIDEO_FILENAME}+sepImgDir"
    ep_dict[f"ep{ep}"]=[]
    ## 비디오 검출
    # 1dub answer : 21616
    # 2dub answer : 22825
    # 3dub answer : 16944
    for img in range(get_first_img_num(SEP_DIRNAME),get_last_img_num(SEP_DIRNAME)):
        try:
            sim = find_similar_images(INDEX_FILENAME,f"{SEP_DIRNAME}/{img}.jpg")
        except Exception as e:
            print(f"Except : {e}")
            sim=0
        print(f"ep:{ep},img_index:{img},sim:{sim}")
        if(sim>THRESH_SIM):
            print("matched!!!")
            ep_dict[f"ep{ep}"].append(img)
    write_json(ep_dict,f"dub_test.json")

print(ep_dict)
'''


# VIDEO_FILENAME = f"{1}blu.mkv"
# SEP_DIRNAME = f"{VIDEO_FILENAME}+sepImgDir"
# sim = find_similar_images(INDEX_FILENAME,f"{SEP_DIRNAME}/3.jpg")
# print(sim)