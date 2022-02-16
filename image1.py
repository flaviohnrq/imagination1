from PIL import Image
import numpy as np
import sys
import random

def tipoRGB(cor,r,g,b): #função que vai trocar os valores das cores. ex. Colocar o valor do VERMELHO no VERDE
    if(cor=='vm'):
        if(rgbtipo==0):
            return r
        elif(rgbtipo==1):
            return g
        else:
            return b
    if(cor=='vd'):
        if(rgbtipo==0):
            return g
        elif(rgbtipo==1):
            return b
        else:
            return r
    if(cor=='az'):
        if(rgbtipo==0):
            return b
        elif(rgbtipo==1):
            return r
        else:
            return g

arg = None
rgbtipo = 0
r1 = random.random()

if(r1<0.33): #RANDOM tipo de troca de cores que sera feita, ou normal
    rgbtipo=1
elif(r1<0.66):
    rgbtipo=2
else:
    rgbtipo=0

if(len(sys.argv) > 1): #verifica se uma imagem foi passada como argumento
    arg = sys.argv[1]
if(arg==None): #se nao passou nenhum argumento abre imagem1
    arg = 'imgs/dog1.jpeg'

img = Image.open(arg) #Abre imagem PILLOW

a = np.asarray(img) #Cria ARRAY a partir da imagem (NUMPY)

tam = img.size #Tamanho da imagem
x = tam[1]
y = tam[0]

#Nova array que vai receber os valores alterados dos pixels e depois sera exibida
arr2 = np.array([[[0,0,0]]*y]*x)

#algoritimo
for x1 in range(x):
    for y1 in range(y):
        try:
            r = int(a[x1,y1,0]) #recolhendo valores RGB
            g = int(a[x1,y1,1])
            b = int(a[x1,y1,2])

            arr2[x1][y1][0] = tipoRGB('vm', r, g, b) #trocar os valores das cores
            arr2[x1][y1][1] = tipoRGB('vd', r, g, b)
            arr2[x1][y1][2] = tipoRGB('az', r, g, b)

        except:
            print('erro')

img2 = Image.fromarray(arr2.astype('uint8'),mode='RGB')
img2.show()
