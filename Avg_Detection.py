import cv2
import numpy as np

img = cv2.imread('./cutframe/0.jpg')
sumlistb = np.zeros((img.shape[0],img.shape[1]),dtype=img.dtype)
sumlistg = np.zeros((img.shape[0],img.shape[1]),dtype=img.dtype)
sumlistr = np.zeros((img.shape[0],img.shape[1]),dtype=img.dtype)
sumb = np.array(sumlistb)
sumg = np.array(sumlistg)
sumr = np.array(sumlistr)
# print(sumb.shape)
for i in range(0,1012):
    img = cv2.imread('./cutframe/'+str(i)+'.jpg')
    b = cv2.split(img)[0]
    g = cv2.split(img)[1]
    r = cv2.split(img)[2]

    imgb = cv2.GaussianBlur(b,(3,3),0)
    cannyb = cv2.Canny(imgb, 40, 100,L2gradient=True)  # apertureSize默认为3
    canny_b=np.array(cannyb)
    # print(canny_b.shape)
    sumb=sumb+canny_b

    imgg = cv2.GaussianBlur(g, (3, 3), 0)
    cannyg = cv2.Canny(imgg, 40, 100, L2gradient=True)  # apertureSize默认为3
    canny_g = np.array(cannyg)

    sumg = sumg + canny_g

    imgr = cv2.GaussianBlur(r, (3, 3), 0)
    cannyr = cv2.Canny(imgr, 40, 100, L2gradient=True)  # apertureSize默认为3
    canny_r = np.array(cannyr)

    sumr = sumr + canny_r

sumb=sumb/1012
sumg=sumg/1012
sumr=sumr/1012

# newb=sumb.tolist()
# newg=sumg.tolist()
# newr=sumr.tolist()

merged = cv2.merge([sumb,sumg,sumr])
cv2.imshow('Canny', merged)
cv2.imwrite('Result_img.jpg',merged)
cv2.waitKey(0)
cv2.destroyAllWindows()



# !/usr/bin/env python
# encoding: utf-8
# import cv2
# import numpy as np
#
#
# def CannyThreshold(lowThreshold):
#     detected_edges = cv2.GaussianBlur(gray, (3, 3), 0)
#     detected_edges = cv2.Canny(detected_edges, lowThreshold, lowThreshold * ratio, apertureSize=kernel_size)
#     dst = cv2.bitwise_and(img, img, mask=detected_edges)  # just add some colours to edges from original image.
#     cv2.imshow('canny demo', dst)
#
#
# lowThreshold = 0
# max_lowThreshold = 100
# ratio = 3
# kernel_size = 3
#
# img = cv2.imread('./Results/water_y.jpg')
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
# cv2.namedWindow('canny demo')
#
# cv2.createTrackbar('Min threshold', 'canny demo', lowThreshold, max_lowThreshold, CannyThreshold)
#
# CannyThreshold(0)  # initialization
# if cv2.waitKey(0) == 27:
#     cv2.destroyAllWindows()