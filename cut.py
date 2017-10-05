import cv2

for i in range(0,1012):
    print(i)
    try:
        frame = cv2.imread('./frames/'+str(i)+'.jpg')
        mouth = frame[31:98, 1135:1304]
        cv2.imwrite("./cutframe/" + str(i) + ".jpg", mouth)
    except:
        print(str(i)+'error')

# frame = cv2.imread('./'+'0'+'.jpg')
# mouth = frame[31:98, 1135:1304]#（左上角坐标(1135,31),右下角坐标(1304,98)）
# cv2.rectangle(frame,(1135,31),(1304,98),(55,255,155),0)
# cv2.imshow('cut',frame)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.imwrite("./" + '1' + ".jpg", mouth)