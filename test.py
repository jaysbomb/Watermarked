import cv2

img=cv2.imread('0.jpg',1)
b = cv2.split(img)[0]
g = cv2.split(img)[1]
r = cv2.split(img)[2]

print(b)