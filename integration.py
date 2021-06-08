import time
import VAS_system
import asyncio
import video_switch
import os
import cv2

VAS = VAS_system.VAS_system()

Video_path = "../data/testvideo/"
cam_names = ["2020-08-21-10.00.30","2020-08-21-10.00.31"]
Start_frame = ["3600", "3200"]  

VIDEO_LIST = []
for i in range(len(cam_names)):
    VIDEO_LIST.append(os.path.join(Video_path,cam_names[i]))


for idx, name in enumerate(VIDEO_LIST):
    # video_start = time.time()

    # print("[ Video Idx: ", name, " ]")
    video_last_name = name + ".mp4"
    print('debug point 1')
    
    Video_Info = [Video_path, video_last_name, Start_frame[idx]]
    # print(Video_Info)
    print('debug point 2')
    VAS.system_Operation(Video_Info)

    
    video_switch(video_list=VIDEO_LIST, frameStart=Start_frame[idx])
    stop_key = cv2.waitKey(1)
    if stop_key == ord('p'):  # pause
        break

    # print(time.strftime("%H:%M:%S", time.gmtime(time.time() - video_start)))