import cv2
import numpy as np
import time

temp_bx=[]
temp_gx=[]
temp_rx=[]
temp_by=[]
temp_gy=[]
temp_ry=[]

medium_bx=[]
medium_gx=[]
medium_rx=[]
medium_by=[]
medium_gy=[]
medium_ry=[]
start = time.clock()

img = cv2.imread('./cutframe/0.jpg')
num=int(len(img))
j=0
while j < num:
    for i in range(0,1011):
        img = cv2.imread('./cutframe/'+str(i)+'.jpg')
        b = cv2.split(img)[0]
        g = cv2.split(img)[1]
        r = cv2.split(img)[2]

        imgb = cv2.GaussianBlur(b,(3,3),0)
        sobelbx = cv2.Sobel(imgb,cv2.CV_64F,1,0,ksize=5)  # apertureSize默认为3
        sobelbx = sobelbx.tolist()
        temp_bx.append(sobelbx[j])

        sobelby = cv2.Sobel(imgb, cv2.CV_64F, 0, 1, ksize=5)  # apertureSize默认为3
        sobelby = sobelby.tolist()
        temp_by.append(sobelby[j])

        imgg = cv2.GaussianBlur(g, (3, 3), 0)
        sobelgx = cv2.Sobel(imgg,cv2.CV_64F,1,0,ksize=5)  # apertureSize默认为3
        sobelgx = sobelgx.tolist()
        temp_gx.append(sobelgx[j])

        sobelgy = cv2.Sobel(imgg, cv2.CV_64F, 0, 1, ksize=5)  # apertureSize默认为3
        sobelgy = sobelgy.tolist()
        temp_gy.append(sobelgy[j])

        imgr = cv2.GaussianBlur(r, (3, 3), 0)
        sobelrx = cv2.Sobel(imgr,cv2.CV_64F,1,0,ksize=5)  # apertureSize默认为3
        sobelrx = sobelrx.tolist()
        temp_rx.append(sobelrx[j])

        sobelry = cv2.Sobel(imgr, cv2.CV_64F, 0, 1, ksize=5)  # apertureSize默认为3
        sobelry = sobelry.tolist()
        temp_ry.append(sobelry[j])


    np_temp_bx=np.array(temp_bx)
    np_temp_bx.sort(0)
    np_temp_bx=np_temp_bx.tolist()
    medium_bx.append(np_temp_bx[505])

    np_temp_by = np.array(temp_by)
    np_temp_by.sort(0)
    np_temp_by = np_temp_by.tolist()
    medium_by.append(np_temp_by[505])

    np_temp_gx = np.array(temp_gx)
    np_temp_gx.sort(0)
    np_temp_gx = np_temp_gx.tolist()
    medium_gx.append(np_temp_gx[505])

    np_temp_gy = np.array(temp_gy)
    np_temp_gy.sort(0)
    np_temp_gy = np_temp_gy.tolist()
    medium_gy.append(np_temp_gy[505])

    np_temp_rx = np.array(temp_rx)
    np_temp_rx.sort(0)
    np_temp_rx = np_temp_rx.tolist()
    medium_rx.append(np_temp_rx[505])

    np_temp_ry = np.array(temp_ry)
    np_temp_ry.sort(0)
    np_temp_ry = np_temp_ry.tolist()
    medium_ry.append(np_temp_ry[505])

    temp_bx = []
    temp_gx = []
    temp_rx = []
    temp_by = []
    temp_gy = []
    temp_ry = []
    j+=1



medium_b=np.array(medium_bx)+np.array(medium_by)
medium_g=np.array(medium_gx)+np.array(medium_gy)
medium_r=np.array(medium_rx)+np.array(medium_ry)

merged = cv2.merge([medium_b,medium_g,medium_r])
end = time.clock()
print("The function run time is : %.03f seconds" % (end - start))

cv2.imshow('Canny', merged)
cv2.imwrite('Water_Result_color.jpg',merged)
cv2.waitKey(0)
cv2.destroyAllWindows()

