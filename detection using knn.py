import cv2
import numpy as np
import os

def distance(x1,x2):
    return np.sqrt(sum((x1-x2)**2))

# Test Time 
def knn(train, test, k=5):
	dist = []
	
	for i in range(train.shape[0]):
		# Get the vector and label
		ix = train[i, :-1]
		iy = train[i, -1]
		# Compute the distance from test point
		d = distance(test, ix)
		dist.append([d, iy])
	# Sort based on distance and get top k
	dk = sorted(dist, key=lambda x: x[0])[:k]
	# Retrieve only the labels
	labels = np.array(dk)[:, -1]
	
	# Get frequencies of each label
	output = np.unique(labels, return_counts=True)
	# Find max frequency and corresponding label
	index = np.argmax(output[1])
	return output[0][index]

#Init Camera
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

#url = "http://192.168.1.3:8080"
#cap = cv2.VideoCapture(url)
# Face Detection
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

skip = 0
dataset_path = './'
face_data = []#x values of data
labels = [] #y values of data
class_id =0 #labels for given file
names = {} #mapping between id and names

#data preparation
for fx in os.listdir(dataset_path): #shows all the files of the data folder
    if fx.endswith('.npy'):
        names[class_id] = fx[:-4] #create a mapping between class id and names
        print("loaded"+fx)
        data_item = np.load(dataset_path+fx) #giving filename along path
        face_data.append(data_item)

        #create labels
        target = class_id*np.ones((data_item.shape[0],))
        class_id+=1
        labels.append(target)
        
face_dataset = np.concatenate(face_data, axis=0)
face_label = np.concatenate(labels, axis=0).reshape((-1,1))

print(face_dataset.shape)
print(face_label.shape)

trainset = np.concatenate((face_dataset, face_label),axis=1)
print(trainset.shape)
#testing
while True:
    ret,frame = cap.read()
    if ret==False:
	    continue
    faces = face_cascade.detectMultiScale(frame,1.3,5)
    for face in faces:
        x,y,w,z = face
        
        offset = 10   #padding
        face_section = frame[y-offset:y+z+offset, x - offset: x+w+offset]
        face_section = cv2.resize(face_section, (100,100))
        #predicted label out
        out = knn(trainset,face_section.flatten())
        #display on the screen the name and rectcangle around it
        pred_name = names[int(out)]

        cv2.putText(frame,pred_name,(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2,cv2.LINE_AA)
        cv2.rectangle(frame,(x,y),(x+w,y+z),(0,255,255),2)
    cv2.imshow("Faces",frame)
    key_pressed = cv2.waitKey(1) & 0xFF #converting a 32 bit number into 8 bit number 
    if key_pressed == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()


        