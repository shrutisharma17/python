import cv2
import numpy as np
cap = cv2.VideoCapture(0)#here in bracket device id is written, 0 means your own webcam
#cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

#url = "http://192.168.1.3:8080"
#cap = cv2.VideoCapture(url)
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
skip=0
face_data=[]
dataset_path = './'

file_name = input("Enter the name of the person: ")
while True:
    ret,frame = cap.read()
    
    if ret == False:#i.e. the capture is not clear etc
        continue
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(frame, 1.3, 5)
    if len(faces)==0:
	    continue

    faces = sorted(faces, key = lambda f:f[2]*f[3])
    ##face_section_list = [] # Define a new empty list!
    for face in faces[-1:]:#PICK THE LAST FACE SINCE IT IS LARGEST ACCORDING TO AREA
        x,y,w,z = face
        cv2.rectangle(frame,(x,y),(x+w,y+z),(0,255,255),2)

        #extract(crop the required the face i.e. the region of interest)
        offset = 10   #padding
        face_section = frame[y-offset:y+z+offset, x - offset: x+w+offset]
        face_section = cv2.resize(face_section, (100,100))
        #face_section_list.append(face_section) # Append EVERY face!
        #store every 10th face
        skip +=1
        if (skip%10==0):
            face_data.append(face_section)
            print(len(face_data))

    cv2.imshow("frame", frame)
    cv2.imshow("Face section frame",face_section)
    '''
    for im in face_section_list:
       
        cv2.waitKey(0)
        '''
        


   # cv2.imshow("Gray videoo",gray_frame)
#    for (x,y,w,h) in faces:
 #       cv2.rectangle(frame,(x,y),(x+w, y+h),(255,0,0),2)
    
    
    key_pressed = cv2.waitKey(1) & 0xFF #converting a 32 bit number into 8 bit number 
    if key_pressed == ord('q'):
        break

face_data = np.asarray(face_data)
face_data = face_data.reshape((face_data.shape[0],-1))
print(face_data.shape)

#save
np.save(dataset_path + file_name +'.npy', face_data)
print("Data saved successfully")
cap.release()
cv2.destroyAllWindows()
'''
wait key(1) means program will waint for 1 ms
waitkey(0)means it will wait for infinite time and program will stop when any key is pressed
'''
