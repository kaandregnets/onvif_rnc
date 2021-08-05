import cv2
import os
#Below code will capture the video frames and will sve it a folder (in current working directory)

dirname = 'cams_screen'
cams_to_screen = [
{'id': '145438_8sch', 'url': 'rtsp://admin:1user183@10.35.16.183:554/live/0/main'},
{'id': '145439_14sch', 'url': 'rtsp://admin:1user184@10.35.16.184:554/live/main'},
{'id': '145440_9_vlad', 'url': 'rtsp://admin:1user185@10.35.16.185:554/live/main'},
{'id': '145441_9_kass', 'url': 'rtsp://admin:1user186@10.35.16.186:554/live/main'},
{'id': '145443_10_osnova', 'url': 'rtsp://admin:1user188@10.35.16.188:554/live/main'},
{'id': '145444_13_scho', 'url': 'rtsp://admin:1user189@10.35.16.189:554/live/main'},
{'id': '145445_13_scho_mlad', 'url': 'rtsp://admin:1user190@10.35.16.190:554/live/main'},
{'id': '146319_12_scho', 'url': 'rtsp://admin:1user193@10.35.16.193:554/live/main'},
{'id': '144139_pos', 'url': 'rtsp://admin:ucdytujhmtdcr1@10.35.32.2:554/live/main'},
{'id': '145140_meh', 'url': 'rtsp://admin:ucdytujhmtdcr1@10.35.32.3:554/live/main'},
{'id': '144141_6_9a', 'url': 'rtsp://admin:ucdytujhmtdcr1@10.35.32.4:554/live/main'},
]

print(type(cams_to_screen))
#video path
def get_shot(cams_to_screen):
    print(cams_to_screen)
    cap = cv2.VideoCapture(cams_to_screen['url'])
    count = 0
    if count < 3:
        while(cap.isOpened()):
            ret, frame = cap.read()
            if not ret:
                break
            else:
                # cv2.imshow('frame', frame)
                #The received "frame" will be saved. Or you can manipulate "frame" as per your needs.
                name = cams_to_screen['id'] +"_rec_frame_"+str(count)+".jpg"
                cv2.imwrite(os.path.join(dirname,name), frame)
                count += 1
            if cv2.waitKey(20) & 0xFF == ord('q'):
                break
            cap.release()
    else:
        cv2.destroyAllWindows()

for cam_to_screen in cams_to_screen:
    get_shot(cam_to_screen)
