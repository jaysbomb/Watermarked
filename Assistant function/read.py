import os
import cv2

img_root = ''#这里写你的文件夹路径，比如：/home/youname/data/img/,注意最后一个文件夹要有斜杠
fps = 30    #保存视频的FPS，可以适当调整

#可以用(*'DVIX')或(*'X264'),如果都不行先装ffmepg: sudo apt-get install ffmepg
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
videoWriter = cv2.VideoWriter('outcarnight2.mp4',fourcc,fps,(1104,492))#最后一个是保存图片的尺寸

for i in range(0,5000):
    frame = cv2.imread('./outcarni/'+str(i)+'.jpg')
    videoWriter.write(frame)

videoWriter.release()