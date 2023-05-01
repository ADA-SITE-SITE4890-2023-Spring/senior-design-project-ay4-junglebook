import cv2
import os
import requests

bot_token = "5888189744:AAGTKt566xOOgKTqs_YsM-RIzGLGC6XUAmM"
chat_id = "-996859396"
<<<<<<< HEAD
text='Here is the New Photo!'
=======
>>>>>>> b147948461c6acdeb104fd7fa7e26f74dbed6a42
folder_path = "/home/junglebook/Desktop/Object_Detection_Files/jungle_book_photos_detected"
sent_photos_file = "/home/junglebook/Desktop/Object_Detection_Files/jungle_book_photos_detected/sent_photos.txt"

valid_extensions = [".jpg", ".jpeg", ".png", ".gif", ".bmp"]

if os.path.exists(sent_photos_file):
    with open(sent_photos_file, "r") as f:
        sent_photos = set(f.read().splitlines())
else:
    sent_photos = set()

classNames = []
classFile = "./coco.names"
with open(classFile,"rt") as f:
    classNames = f.read().rstrip("\n").split("\n")

configPath = "./ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt"
weightsPath = "./frozen_inference_graph.pb"

net = cv2.dnn_DetectionModel(weightsPath,configPath)
net.setInputSize(320,320)
net.setInputScale(1.0/ 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

def send_photo_to_telegram(photo_path):
    with open(photo_path, 'rb') as f:
<<<<<<< HEAD
        photo = {'photo':f,'caption' : 'New photo'}
        url_photo = f"https://api.telegram.org/bot{bot_token}/sendPhoto?chat_id={chat_id}"
        response_photo = requests.post(url_photo, files=photo)
        print(f"Photo is sent: {response_photo}")

def send_message_to_telegram():
    photo = {'photo':'smth','caption' : 'New photo'}
    url_message = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={text}"
    response_photo = requests.post(url_message, files=photo)
    print(f"Photo is sent: {response_photo}")
=======
        photo = {'photo': f 'caption': 'Here is a new photo'}
        url_photo = f"https://api.telegram.org/bot{bot_token}/sendPhoto?chat_id={chat_id}"
        response_photo = requests.post(url_photo, files=photo)
        print(f"Photo is sent: {response_photo.content}")
>>>>>>> b147948461c6acdeb104fd7fa7e26f74dbed6a42

def getObjects(img, thres, nms, draw=True, objects=[]):
    classIds, confs, bbox = net.detect(img,confThreshold=thres,nmsThreshold=nms)
    #print(classIds,bbox)
    if len(objects) == 0: objects = classNames
    objectInfo =[]
    if len(classIds) != 0:
        for classId, confidence,box in zip(classIds.flatten(),confs.flatten(),bbox):
            className = classNames[classId - 1]
            if className in objects:
                objectInfo.append([box,className])
                if (draw):
                    cv2.rectangle(img,box,color=(0,255,0),thickness=2)
                    cv2.putText(img,classNames[classId-1].upper(),(box[0]+10,box[1]+30),
                    cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
                    cv2.putText(img,str(round(confidence*100,2)),(box[0]+200,box[1]+30),
                    cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)

    return img,objectInfo


if _name_ == "_main_":

    cap = cv2.VideoCapture(0)
    cap.set(3,640)
    cap.set(4,480)
    #cap.set(10,70)
    i = 0
    while True:
        success,img = cap.read()
<<<<<<< HEAD
        result, objectInfo = getObjects(img,0.45,0.2)
=======
        img,objectInfo = getObjects(img,thres=0.5,nms=0.2,draw=False,objects=["person"])
>>>>>>> b147948461c6acdeb104fd7fa7e26f74dbed6a42
        cv2.imshow("Output",img)

        # Save image to disk if person detected
        for box, class_name in objectInfo:
<<<<<<< HEAD
            if class_name == 'chair':

                filename = f'jungle_book_photos_detected/junglebook_photo_detected_{i}.jpg'
                i += 1
                cv2.imwrite(filename, img)
                print(f"Image saved as {filename}")
                send_photo_to_telegram(filename)
                send_message_to_telegram()
=======
            if class_name == 'person':
                filename = 'jungle_book_photos_detected/junglebook13_detected.jpg'
                cv2.imwrite(filename, img)
                print(f"Image saved as {filename}")
                send_photo_to_telegram(filename)
>>>>>>> b147948461c6acdeb104fd7fa7e26f74dbed6a42
                break

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
