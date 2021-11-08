import os
projectPath = os.path.abspath('main.py').replace('\main.py', '')
import sys
sys.path.append(projectPath)
import cv2 as cv

class Captura:
    classificador = cv.CascadeClassifier('rsc/haarcascade_frontalface_default.xml')
    camera = cv.VideoCapture(0)
    amostra = 1
    numeroDeAmostras = 25
    largura, altura = 220, 220

    # -> Realiza captura e salva as imagens das faces na pasta de fotos
    def capturaCadastro(self, id):
        while(True):
            conectado, imagem = self.camera.read()
            imagemCinza = cv.cvtColor(imagem, cv.COLOR_BGR2GRAY)
            facesDetect = self.classificador.detectMultiScale(imagemCinza,
                                                        scaleFactor = 1.5,
                                                        minSize = (150, 150))
            for(x, y, l, a) in facesDetect:
                cv.rectangle(imagem, (x, y), (x + l, y + a), (0, 255, 0), 2)

                if (cv.waitKey(1) & 0xFF == ord('q')):
                    
                    imagemFace = cv.resize(imagemCinza[y: y + a, x: x + l], (self.largura, self.altura))
                    imgPath = 'fotos/pessoa.' + str(id) + '.' + str(self.amostra) + '.jpg'
                    
                    cv.imwrite(imgPath, imagemFace)
                    
                    print('[SISTEMA] --- Foto salva no caminho:....' + str(imgPath))
                    
                    self.amostra += 1

            cv.imshow("Face Capture", imagem)
            cv.waitKey(1)

            if((self.amostra >= self.numeroDeAmostras) | (cv.waitKey(1) & 0xFF == ord('e'))):
                break

        print('[INFO] --- Faces capturadas com sucesso!')
        self.camera.release()
        cv.destroyAllWindows()
        return imgPath
                