import cv2
import numpy as np
from matplotlib import pyplot as plt

def readimage(name,num):
    if num==1:
        img=cv2.imread(name,1)
    else:
        img=cv2.imread(name,0)
    return img

def writeimage(name,img):
    cv2.imwrite(name,img)

def splitRGB(img):
    b = cv2.split(img)[0]
    g = cv2.split(img)[1]
    r = cv2.split(img)[2]
    return b,g,r




if __name__ == '__main__':
    img=readimage('watermark.jpg',1)
    b = cv2.split(img)[0]
    g = cv2.split(img)[1]
    r = cv2.split(img)[2]
    # sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
    # sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
    # sobelxy= cv2.Sobel(img,cv2.CV_64F,1,1,ksize=5)
    # sobelxy3= cv2.Sobel(img,cv2.CV_64F,1,1,ksize=3)

    sobel_xb= cv2.Sobel(b,cv2.CV_64F,1,0,ksize=5)
    sobel_yb= cv2.Sobel(b,cv2.CV_64F,0,1,ksize=5)

    sobel_xg = cv2.Sobel(g, cv2.CV_64F, 1, 0, ksize=5)
    sobel_yg = cv2.Sobel(g, cv2.CV_64F, 0, 1, ksize=5)

    sobel_xr = cv2.Sobel(r, cv2.CV_64F, 1, 0, ksize=5)
    sobel_yr = cv2.Sobel(r, cv2.CV_64F, 0, 1, ksize=5)

    img_mixb = cv2.addWeighted(sobel_xb, 0.5, sobel_yb, 0.5, 0)
    img_mixg = cv2.addWeighted(sobel_xg, 0.5, sobel_yg, 0.5, 0)
    img_mixr = cv2.addWeighted(sobel_xr, 0.5, sobel_yr, 0.5, 0)

    merged = cv2.merge([img_mixb, img_mixg, img_mixr])

    cv2.imwrite('watermarkedR.jpg',img_mixr)

    # plt.subplot(2,3,1),plt.imshow(img,cmap = 'gray')
# plt.title('Original'), plt.xticks([]), plt.yticks([])
# plt.subplot(2,3,2),plt.imshow(laplacian,cmap = 'gray')
# plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
# plt.subplot(2,3,3),plt.imshow(sobelx,cmap = 'gray')
# plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
# plt.subplot(2,3,4),plt.imshow(sobely,cmap = 'gray')
# plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
# plt.subplot(2,3,5),plt.imshow(sobelxy,cmap = 'gray')
# plt.title('Sobel XY'), plt.xticks([]), plt.yticks([])
# plt.subplot(2,3,6),plt.imshow(sobelxy3,cmap = 'gray')
# plt.title('Sobel XY3'), plt.xticks([]), plt.yticks([])
# plt.show()