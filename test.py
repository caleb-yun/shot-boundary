import cv2
import numpy as np
import matplotlib.pyplot as plt

video = cv2.VideoCapture('dataset/Videos/video18.mp4')
# video = cv2.VideoCapture('dataset/Queries/video_6_1_filtered.mp4')
# 45, 79, 107, 120, 135, 163, 191, 219, 235, 247, 275, 303, 352

i = 0
index = []
x = []  # for plotting
y = []
frame_diffs = []
boundaries = []
last_boundary = -1

success, frame = video.read()
curr_frame = None
prev_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)  # LAB color space
success, frame = video.read()

# calculate diff between each frame
while success and i < 1000:
    curr_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
    
    diff = cv2.absdiff(curr_frame, prev_frame)
    norm = np.linalg.norm(diff, axis=2)  # use norm to find euclidian distance
    val = np.mean(norm)

    index.append(i)
    frame_diffs.append(val)

    # std = np.std(frame_diffs[last_boundary+1 :])
    # mean = np.mean(frame_diffs[last_boundary+1 :])

    # if abs(val - mean) > 2 * std:
    #     y.append(val)
    #     last_boundary = i
    #     boundaries.append(i)

    #     print(i, val)
    #     # fig = plt.figure()
    #     # fig.add_subplot(1, 2, 1)
    #     # plt.imshow(prev_frame)
    #     # fig.add_subplot(1, 2, 2)
    #     # plt.imshow(curr_frame)
    #     # plt.show(block=True)
    # else:
    #     y.append(0)

    prev_frame = curr_frame
    success, frame = video.read()
    i += 1

video.release()

# process diffs in 17 frame window
for i in range(8, len(frame_diffs)-7):
    x.append(i)
    mean = np.mean(frame_diffs[i-8:i] + frame_diffs[i+1:i+8])
    if frame_diffs[i] > 5 and frame_diffs[i] > 3 * mean:
        y.append(frame_diffs[i])
        print(i, frame_diffs[i])
        i += 7
    else:
        y.append(0)

# plt.plot(index, frame_diffs)
# plt.show()

plt.plot(x, y)
plt.show()
