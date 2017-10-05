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

