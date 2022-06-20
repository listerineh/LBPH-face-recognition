import cv2
import os
import numpy as np

dataPath = 'Data'
peopleList = os.listdir(dataPath)
print('People listing: ', peopleList)

labels = []
facesData = []
label = 0

for nameDir in peopleList:
    personPath = dataPath + '/' + nameDir
    print('Reading images:')

    for fileName in os.listdir(personPath):
        print('Rostros: ', nameDir + '/' + fileName)
        labels.append(label)
        facesData.append(cv2.imread(personPath+'/'+fileName, 0))
    label = label + 1

face_recognizer = cv2.face.LBPHFaceRecognizer_create()

print("Training...")
face_recognizer.train(facesData, np.array(labels))

face_recognizer.write('modeloLBPHFace.xml')
print("Model saved as modeloLBPHFace.xml ...")
