import cv2
import numpy as np

temp_x=[]
temp_y=[]

medium_x=[]
medium_y=[]

img = cv2.imread('./cutframe/0.jpg')
num=int(len(img))
j=0
while j < num:

    for i in range(0, 1011):
        img = cv2.imread('./cutframe/' + str(i) + '.jpg',0)

        img = cv2.GaussianBlur(img, (3, 3), 0)
        sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
        sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)

        sobelx=sobelx.tolist()
        sobely=sobely.tolist()

        temp_x.append(sobelx[j])
        temp_y.append(sobely[j])

    np_temp_x = np.array(temp_x)
    np_temp_x.sort(0)
    np_temp_x = np_temp_x.tolist()
    medium_x.append(np_temp_x[505])

    np_temp_y = np.array(temp_y)
    np_temp_y.sort(0)
    np_temp_y = np_temp_y.tolist()
    medium_y.append(np_temp_y[505])

    temp_x = []
    temp_y = []
    j+=1



img_gra = np.array(medium_x)+np.array(medium_y)
cv2.imshow('IMG_GRAD',img_gra)
cv2.imwrite('./Results/Water_result.jpg',img_gra)
cv2.waitKey(0)
cv2.destroyAllWindows()





