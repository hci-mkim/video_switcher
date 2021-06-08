import cv2

VIDEO_LIST = ['', '../data/testvideo/2020-08-21-10.00.30.mp4', '../data/testvideo/2020-08-21-10.00.31.mp4']

def video_switch(video_list, frameStart):
    cap = cv2.VideoCapture(video_list[1])
    cap.set(1, frameStart)

    while cap.isOpened():
        ret, img = cap.read()
        if ret:
            cv2.imshow("Frame", img)

        key = cv2.waitKey(1) # wait 1ms

        if key == ord('0'):  # end s/w
            break

        if key == ord('p'):  # pause
            cv2.waitKey(-1)

        if key == ord('2'):  # TODO: check if key is between 1-9 using regular expression
            cap.release()
            cap = cv2.VideoCapture(video_list[2])

        if key == ord('1'):
            cap.release()
            cap = cv2.VideoCapture(video_list[1])       
  
    cap.releaes()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    video_switch(video_list=VIDEO_LIST, frameStart=1000)
    print('end')