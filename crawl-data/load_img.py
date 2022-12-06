import cv2
import os
import json
import requests
import shutil
import time
import glob
from PIL import Image
from tqdm import tqdm

def load_image_from_json():
    f = open('./image_srcs.json')
    data = json.load(f)
    
    name = 0
    for i in tqdm(data):
        img_src = i['src']
        res = requests.get(img_src, stream = True)
        if res.status_code == 200:
            ext = img_src.split('/')[-1].split('.')[-1]
            file_name = f'../data/data_051222/img_{name}.{ext}'
            with open(file_name, 'wb') as f:
                shutil.copyfileobj(res.raw, f)
            print('Image sucessfully Downloaded: ',file_name)
            name += 1
        else:
            print('Image Couldn\'t be retrieved')

def get_list_video(folder):
    videos = glob.glob(f'{folder}/*.mp4')
    return videos

def load_image_from_video():
    videos = get_list_video('../../../../Desktop')
    img_name = 72

    for video in tqdm(videos):
        # used to record the time when we processed last frame
        prev_frame_time = 0
    
        # used to record the time at which we processed current frame
        new_frame_time = 0
    
        cap = cv2.VideoCapture(video)
        no_of_frames = 0
    
        while True:
            ret, frame = cap.read()
            no_of_frames += 1
            
            if not ret:
                break

            if no_of_frames == 3:
                cv2.imwrite(f'../data/data_051222/img_{img_name}.jpg', frame)
                img_name += 1

            if no_of_frames > 5:
                no_of_frames = 0
    
            #new_frame_time = time.time()
            #fps = 1 / (new_frame_time - prev_frame_time)
            #prev_frame_time
            #fps = str(int(fps))
    
            cv2.imshow('video', frame)
            if cv2.waitKey(1) == ord('q'):
                break
    
        cap.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    load_image_from_video()
