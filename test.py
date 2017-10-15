import cv2

img=cv2.imread('./Results/Water_Result_color_full.jpg',0)
# img=cv2.imread('./result_cut_frames/591.jpg',0)
imgb = cv2.GaussianBlur(img,(3,3),0)
canny = cv2.Canny(imgb, 40, 100,L2gradient=True)

cv2.imwrite('./tt.jpg',canny)
cv2.imshow('Canny', canny)
cv2.waitKey(0)
cv2.destroyAllWindows()
