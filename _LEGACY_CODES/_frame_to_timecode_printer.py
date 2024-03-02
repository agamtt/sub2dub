

def frames_to_TC(frames, fps=25):
    total_seconds = int(frames / fps)
    h = int(total_seconds / 3600)
    m = int((total_seconds % 3600) / 60)
    s = int(total_seconds % 60)
    f = frames % fps
    return ("%02d:%02d:%02d:%02d" % (h, m, s, f))

print(frames_to_TC(27259))


#21292 -> 00:14:47:05 # 현재 알고리즘
#21292 -> 00:14:48:01 # 이렇게 되도록 수정해야함

#31457 -> 00:21:50:18 # 현재 알고리즘
#31457 -> 00:21:52:00 # 이렇게 되도록 수정해야함
