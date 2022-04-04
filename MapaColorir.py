import cv2 as cv
import numpy as np

imagem_original = cv.imread('VBrazil.jpg')
imagem_original = cv.resize(imagem_original,(320,240))

rodape = np.zeros((50,960,3),dtype = np.uint8)
cv.putText(rodape,'Rainbow: Heron TF Gomes',(580,25),cv.FONT_HERSHEY_SCRIPT_SIMPLEX ,1,(190,190,190),1,cv.LINE_AA )
cv.putText(rodape,'02/02/2020',(850,45),cv.FONT_HERSHEY_SCRIPT_SIMPLEX ,0.5,(190,190,190),1,cv.LINE_AA )




imagem_vet = []


for color in [1,2,4,8,9,11,18,19]:#
    imagem_color=cv.applyColorMap(imagem_original,color)
    imagem_vet.append(imagem_color)
    #cv.imshow('Imagem'+str(color),imagem_color)
    

#cv.waitKey()
#cv.destroyAllWindows()

imagem_vet.append(imagem_original)
imagem_cima = cv.hconcat([imagem_vet[7],imagem_vet[1],imagem_vet[5]])
imagem_meio = cv.hconcat([imagem_vet[3],imagem_vet[8],imagem_vet[4]])
imagem_baixo = cv.hconcat([imagem_vet[2],imagem_vet[6],imagem_vet[0]])



imagem_completa = cv.vconcat([imagem_cima,imagem_meio,imagem_baixo])
imagem_completa = cv.vconcat([imagem_completa,rodape])




cv.imshow('Imagem',imagem_completa)
cv.waitKey()
cv.destroyAllWindows()

cv.imwrite('VBrazil.png',imagem_completa)






