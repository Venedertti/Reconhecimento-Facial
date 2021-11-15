import os
projectPath = os.path.abspath('main.py').replace('\main.py', '')
import sys
sys.path.append(projectPath)

import cv2 as cv
import numpy as np
import os

class Treinamento():
    fisherFace = cv.face.FisherFaceRecognizer_create()

    def teste(self,):
        print('ok')

    def getImagemComId(self, ):
        paths = [os.path.join('rsc/fotos', f) for f in os.listdir('rsc/fotos')]
        faces = []
        ids = []

        for path in paths:
            imageFace = cv.cvtColor(cv.imread(path), cv.COLOR_RGB2GRAY)
            id = int(os.path.split(path)[-1].split('.')[1])
            ids.append(id)
            faces.append(imageFace)
        
        return faces, np.array(ids)

    # -> Realiza o treinamento do Algoritimo: FisherFaces 
    def treinarFisherFace(self, ):
        faces, ids = self.getImagemComId()
        print('[SISTEMA] --- Iniciando treinamento de algiritimo: [FisherFace]...')
        self.fisherFace.train(faces, ids) 
        self.fisherFace.write('rsc/classificadorFisher.yml')
        print('[SISTEMA] --- Finalizado treinamento de algiritimo: [FisherFace]')


