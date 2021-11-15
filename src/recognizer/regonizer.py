import os
projectPath = os.path.abspath('main.py').replace('\main.py', '')
import sys
sys.path.append(projectPath)
import cv2 as cv
from src.model.FuncionarioDomModel import FuncionarioDomModel

class Recognizer:
    def __init__(self, ):
        self._camera = cv.VideoCapture(0)
        self._detectorFace = cv.CascadeClassifier('rsc/haarcascade_frontalface_default.xml')
        self._reconhecedor = cv.face.FisherFaceRecognizer_create()
    

    # -> Realiza autenticação por facial ao aprertar o botão "Q" 
    def getAutenticacao(self, func:FuncionarioDomModel):
        self._reconhecedor.read(r'rsc/classificadorFisher.yml')
        largura, altura = 220, 220
        font = cv.FONT_HERSHEY_DUPLEX
        nome = ''

        while(True):
            conectado, imagem = self._camera.read()
            imagemCinza = cv.cvtColor(imagem, cv.COLOR_BGR2GRAY)
            facesDetectadas = self._detectorFace.detectMultiScale(imagemCinza,
                                                            scaleFactor=1.5,
                                                            minSize=(150,150))

            for (x, y, l, a) in facesDetectadas:
                
                imagemFace = cv.resize(imagemCinza[y: y + a, x: x + l], (largura, altura))
                cv.rectangle(imagem, (x, y), (x + l, y + a), (0, 255, 0), 2)
                
                id, confinca = self._reconhecedor.predict(imagemFace)
                
                if(int(id) == int(func.getId())):
                    nome = func.getNome()

                cv.putText(imagem, nome, (x,y + (a + 50)), font, 1, (0, 255, 0))

            if (cv.waitKey(1) & 0xFF == ord('q')):
                if(nome == func.getNome()):
                    return True, confinca
                                    
                else:
                    return False, 0

            cv.imshow("FaceEigen", imagem)
            cv.waitKey(1)

        self.camera.release()
        cv.destroyAllWindows