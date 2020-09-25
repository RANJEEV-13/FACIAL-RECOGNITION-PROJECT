import cv2
import numpy as np
import datetime

faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam=cv2.VideoCapture(0);
rec=cv2.createLBPHFaceRecognizer();
rec.load("recognizer\\trainingData.yml")
id,c1,c2,c3,c4=0,0,0,0,0
abc=""
font=cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_DUPLEX,1,2,0,3)
while (True):
    ret,img=cam.read();
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceDetect.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        id,conf=rec.predict(gray[y:y+h,x:x+w])
        if(id==2):
            id="rohit"
            c2=c2+1;
            cv2.cv.PutText(cv2.cv.fromarray(img),str(id),(x,y+h),font,255);
            if(c2>20):
                abc="rohit IS PRESENT..."
                cv2.cv.PutText(cv2.cv.fromarray(img),str(abc),(x,y),font,255);

        elif(id==1):
            id="Saif"
            c1=c1+1;
            cv2.cv.PutText(cv2.cv.fromarray(img),str(id),(x,y+h),font,255);
            if(c1>20):
                abc="Saif IS PRESENT..."
                cv2.cv.PutText(cv2.cv.fromarray(img),str(abc),(x,y),font,255);

        elif(id==3):
            id="vivek"
            c3=c3+1;
            cv2.cv.PutText(cv2.cv.fromarray(img),str(id),(x,y+h),font,255);
            if(c3>20):
                abc="vivek IS PRESENT..."
                cv2.cv.PutText(cv2.cv.fromarray(img),str(abc),(x,y),font,255);   
        elif(id==4):
            id="inderjeet"
            c4=c4+1;
            cv2.cv.PutText(cv2.cv.fromarray(img),str(id),(x,y+h),font,255);
            if(c4>20):
                abc="inderjeet SIR IS PRESENT..."
                cv2.cv.PutText(cv2.cv.fromarray(img),str(abc),(x,y),font,255);
        elif(id==5):
            id="saif"
            c2=c2+1;
            cv2.cv.PutText(cv2.cv.fromarray(img),str(id),(x,y+h),font,255);
            if(c2>20):
                abc="saif IS PRESENT..."
                cv2.cv.PutText(cv2.cv.fromarray(img),str(abc),(x,y),font,255);
        elif(id==6):
            id="gaurav"
            c2=c2+1;
            cv2.cv.PutText(cv2.cv.fromarray(img),str(id),(x,y+h),font,255);
            if(c2>20):
                abc="gaurav  IS PRESENT..."
                cv2.cv.PutText(cv2.cv.fromarray(img),str(abc),(x,y),font,255);
        elif(id==7):
            id="Manpreet mam"
            c4=c4+1;
            cv2.cv.PutText(cv2.cv.fromarray(img),str(id),(x,y+h),font,255);
            if(c4>20):
                abc="Manpreet mam IS PRESENT..."
                cv2.cv.PutText(cv2.cv.fromarray(img),str(abc),(x,y),font,255);       
        else:
            if(c1>20):
                abc="None..."
                cv2.cv.PutText(cv2.cv.fromarray(img),str(abc),(x,y),font,255);

    cv2.imshow("Face",img)
    fileat=open("C:\\Users\\Ravi\\Desktop\\work\\facereg\\attend.txt","w+")
    fileat.write(abc)
    now = datetime.datetime.now()
    fileat.write("\nDate and time :\n")
    fileat.write(now.strftime("%Y-%m-%d %H:%M:%S\n"))
    if(c1>50):
        ab="\nSaif is present\n"
        fileat.write(ab)
    if(c2>50):
        bc="kirti is present\n"
        fileat.write(bc)
    if(c3>50):
        cd="NONE is present\n"
        fileat.write(cd)
    if(c4>50):
        cd="SUSHIL is present\n"
        fileat.write(cd)
    if(cv2.waitKey(1)==ord('q')):
        break;

#ko=open('attend.txt','r')
#dataof=ko.read()
#print(dataof)
#ko.close()
fileat.close()
cam.release()
cv2.destroyAllWindows()
