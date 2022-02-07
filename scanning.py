import cv2
import os
import imutils

personName = input("Ingrese su nombre: ")
dataPath = 'Data'
personPath = dataPath + '/' + personName

if not os.path.exists(personPath):
    count = 0
    os.makedirs(personPath)
    print('Carpeta creada: ',personPath)
else:
    count = len(os.listdir(personPath))
    print(f'Carpeta contiene {count} fotos, se agregaran nuevas')

breakCondition = count + 300
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

while True:
    ret, frame = cap.read()
    if ret == False: break
    frame =  imutils.resize(frame, width=640)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    auxFrame = frame.copy()

    faces = faceClassif.detectMultiScale(gray,1.3,5)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
        rostro = auxFrame[y:y+h,x:x+w]
        rostro = cv2.resize(rostro,(150,150),interpolation=cv2.INTER_CUBIC)
        cv2.imwrite(personPath + '/rostro_{}.jpg'.format(count),rostro)
        count = count + 1
        cv2.putText(frame, f"Rostros detectados: {count}", (x, y-20), 2,
                        0.8, (0, 0, 255), 1, cv2.LINE_AA)
    cv2.imshow('frame',frame)
    
    k =  cv2.waitKey(1)
    if k == 27 or count >= breakCondition:
        break

cap.release()
cv2.destroyAllWindows()
