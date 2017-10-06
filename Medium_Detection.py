import cv2
import numpy as np

temp_b=[]
temp_g=[]
temp_r=[]

medium_b=[]
medium_g=[]
medium_r=[]
img = cv2.imread('./cutframe/0.jpg')
num=int(len(img))
j=0
while j < num:
    for i in range(0,100):
        img = cv2.imread('./cutframe/'+str(i)+'.jpg')
        b = cv2.split(img)[0]
        g = cv2.split(img)[1]
        r = cv2.split(img)[2]

        # imgb = cv2.GaussianBlur(b,(3,3),0)
        cannyb = cv2.Sobel(b,cv2.CV_64F,0,1,ksize=5)  # apertureSize默认为3
        cannyb = cannyb.tolist()
        temp_b.append(cannyb[j])


        # imgg = cv2.GaussianBlur(g, (3, 3), 0)
        cannyg = cv2.Sobel(g,cv2.CV_64F,0,1,ksize=5)  # apertureSize默认为3
        cannyg = cannyg.tolist()
        temp_g.append(cannyg[j])

        # imgr = cv2.GaussianBlur(r, (3, 3), 0)
        cannyr = cv2.Sobel(r,cv2.CV_64F,0,1,ksize=5)  # apertureSize默认为3
        cannyr = cannyr.tolist()
        temp_r.append(cannyr[j])



    np_temp_b=np.array(temp_b)
    np_temp_b.sort(0)
    np_temp_b=np_temp_b.tolist()
    medium_b.append(np_temp_b[50])



    np_temp_g = np.array(temp_g)
    np_temp_g.sort(0)
    np_temp_g=np_temp_g.tolist()
    medium_g.append(np_temp_g[50])

    np_temp_r = np.array(temp_r)
    np_temp_r.sort(0)
    np_temp_r=np_temp_r.tolist()
    medium_r.append(np_temp_r[50])

    j+=1



medium_b=np.array(medium_b)
print(medium_b)
medium_g=np.array(medium_g)
medium_r=np.array(medium_r)

merged = cv2.merge([medium_b,medium_g,medium_r])
print(merged)
cv2.imshow('Canny', merged)
cv2.imwrite('Result_img.jpg',merged)
cv2.waitKey(0)
cv2.destroyAllWindows()

