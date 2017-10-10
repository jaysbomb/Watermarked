import cv2
import numpy as np
import time

start = time.clock()
current_pos = None
tl = None
br = None

#mouse
def get_rect(im, title='get_rect'):   #   (a,b) = get_rect(im, title='get_rect')
    mouse_params = {'tl': None, 'br': None, 'current_pos': None,
        'released_once': False}

    cv2.namedWindow(title)
    cv2.moveWindow(title, 100, 100)

    def onMouse(event, x, y, flags, param):

        param['current_pos'] = (x, y)

        if param['tl'] is not None and not (flags & cv2.EVENT_FLAG_LBUTTON):
            param['released_once'] = True

        if flags & cv2.EVENT_FLAG_LBUTTON:
            if param['tl'] is None:
                param['tl'] = param['current_pos']
            elif param['released_once']:
                param['br'] = param['current_pos']

    cv2.setMouseCallback(title, onMouse, mouse_params)
    cv2.imshow(title, im)

    while mouse_params['br'] is None:
        im_draw = np.copy(im)

        if mouse_params['tl'] is not None:
            cv2.rectangle(im_draw, mouse_params['tl'],
                mouse_params['current_pos'], (255, 0, 0))

        cv2.imshow(title, im_draw)
        _ = cv2.waitKey(10)

    cv2.destroyWindow(title)

    tl = (min(mouse_params['tl'][0], mouse_params['br'][0]),
        min(mouse_params['tl'][1], mouse_params['br'][1]))
    br = (max(mouse_params['tl'][0], mouse_params['br'][0]),
        max(mouse_params['tl'][1], mouse_params['br'][1]))

    return (tl, br)  #tl=(y1,x1), br=(y2,x2)

#read_video,capture_rect
def Video(pathName, skipFrame):
    cap = cv2.VideoCapture(pathName)
    print('======Succeed load:',pathName,'======')
    c=skipFrame
    ret,frame = cap.read()
    if (c >= skipFrame):
        if (c == skipFrame):
            print('------Plase marked watermark------')
            (a, b) = get_rect(frame, title='get_rect')


    # Get the width and height of frame
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) + 0.5)
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) + 0.5)

    i = 0
    print('======Start cutting ROI======')
    while (cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            mouth = frame[a[1]:b[1], a[0]:b[0]]
            cv2.imwrite("./result_cut_frames/" + str(i) + ".jpg", mouth)
            i += 1
            cv2.imshow('frame', frame)
            if (cv2.waitKey(1) & 0xFF) == ord('q'):  # Hit `q` to exit
                break
        else:
            break

        a_len = len(mouth)

    cap.release()
    cv2.destroyAllWindows()
    i+=1
    return i,a_len

def image_grad(numbers,length):
    temp_bx = []
    temp_gx = []
    temp_rx = []
    temp_by = []
    temp_gy = []
    temp_ry = []

    medium_bx = []
    medium_gx = []
    medium_rx = []
    medium_by = []
    medium_gy = []
    medium_ry = []
    print('======Start calculate gradient======')

    j = 0
    while j < length:
        for i in range(0, numbers):
            img = cv2.imread('./result_cut_frames/' + str(i) + '.jpg')
            b = cv2.split(img)[0]
            g = cv2.split(img)[1]
            r = cv2.split(img)[2]

            imgb = cv2.GaussianBlur(b, (3, 3), 0)
            sobelbx = cv2.Sobel(imgb, cv2.CV_64F, 1, 0, ksize=5)  # apertureSize默认为3
            sobelbx = sobelbx.tolist()
            temp_bx.append(sobelbx[j])

            sobelby = cv2.Sobel(imgb, cv2.CV_64F, 0, 1, ksize=5)  # apertureSize默认为3
            sobelby = sobelby.tolist()
            temp_by.append(sobelby[j])

            imgg = cv2.GaussianBlur(g, (3, 3), 0)
            sobelgx = cv2.Sobel(imgg, cv2.CV_64F, 1, 0, ksize=5)  # apertureSize默认为3
            sobelgx = sobelgx.tolist()
            temp_gx.append(sobelgx[j])

            sobelgy = cv2.Sobel(imgg, cv2.CV_64F, 0, 1, ksize=5)  # apertureSize默认为3
            sobelgy = sobelgy.tolist()
            temp_gy.append(sobelgy[j])

            imgr = cv2.GaussianBlur(r, (3, 3), 0)
            sobelrx = cv2.Sobel(imgr, cv2.CV_64F, 1, 0, ksize=5)  # apertureSize默认为3
            sobelrx = sobelrx.tolist()
            temp_rx.append(sobelrx[j])

            sobelry = cv2.Sobel(imgr, cv2.CV_64F, 0, 1, ksize=5)  # apertureSize默认为3
            sobelry = sobelry.tolist()
            temp_ry.append(sobelry[j])

        np_temp_bx = np.array(temp_bx)
        np_temp_bx.sort(0)
        np_temp_bx = np_temp_bx.tolist()
        medium_bx.append(np_temp_bx[numbers//2])

        np_temp_by = np.array(temp_by)
        np_temp_by.sort(0)
        np_temp_by = np_temp_by.tolist()
        medium_by.append(np_temp_by[numbers//2])

        np_temp_gx = np.array(temp_gx)
        np_temp_gx.sort(0)
        np_temp_gx = np_temp_gx.tolist()
        medium_gx.append(np_temp_gx[numbers//2])

        np_temp_gy = np.array(temp_gy)
        np_temp_gy.sort(0)
        np_temp_gy = np_temp_gy.tolist()
        medium_gy.append(np_temp_gy[numbers//2])

        np_temp_rx = np.array(temp_rx)
        np_temp_rx.sort(0)
        np_temp_rx = np_temp_rx.tolist()
        medium_rx.append(np_temp_rx[numbers//2])

        np_temp_ry = np.array(temp_ry)
        np_temp_ry.sort(0)
        np_temp_ry = np_temp_ry.tolist()
        medium_ry.append(np_temp_ry[numbers//2])

        temp_bx = []
        temp_gx = []
        temp_rx = []
        temp_by = []
        temp_gy = []
        temp_ry = []
        j += 1

    medium_b = np.array(medium_bx) + np.array(medium_by)
    medium_g = np.array(medium_gx) + np.array(medium_gy)
    medium_r = np.array(medium_rx) + np.array(medium_ry)

    merged = cv2.merge([medium_b, medium_g, medium_r])
    cv2.imwrite('./Results/Water_Result_color_full.jpg', merged)
    print('======Finished gradient!======')
    end = time.clock()
    print("The function run time is : %.03f seconds" % (end - start))

if __name__ == '__main__':
    (img_num,img_length)=Video("./Original/test.mp4",1)
    print(img_num,img_length)
    image_grad(img_num,img_length)

