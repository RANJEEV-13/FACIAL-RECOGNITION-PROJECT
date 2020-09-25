import os
import cv2
import numpy as np
from PIL import Image
recognizer=cv2.createLBPHFaceRecognizer();
path='dataSet'

def getImagesWithID(path):
    #this is sorting elements and taking all pictures
    #and storing all in the list
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
    faces=[]
    IDs=[]
    # looping for images
    for imagePath in imagePaths:
        #open cv works with numpy array so convert image into numpy array
        faceImg=Image.open(imagePath).convert('L');
        faceNp=np.array(faceImg,'uint8')
        ID=int(os.path.split(imagePath)[-1].split('.')[1])
        faces.append(faceNp)
        print(ID)
        IDs.append(ID)
        cv2.imshow("Training",faceNp)
        cv2.waitKey(10)
    return IDs,faces
Ids,faces=getImagesWithID(path)
recognizer.train(faces,np.array(Ids))
recognizer.save('recognizer/trainingData.yml')
cv2.destroyAllWindows()