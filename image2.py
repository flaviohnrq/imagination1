from PIL import Image
import sys
import numpy as np
import random

def codasci(z): #funcao para transformar pixel em texo
    if (z>215):
        return '#'
    if (z>175):
        return '@'
    elif (z>150):
        return 'y'
    elif (z>125):
        return ';'
    elif (z>100):
        return '~'
    elif (z>50):
        return '.'
    else:
        return ' '

fazerASCI = False
arquivo = ''
arg = None

if(len(sys.argv) > 1): #verifica se uma imagem foi passada como argumento
    arg = sys.argv[1]

if(arg==None): #se nenhuma imagem foi passada como argumento abrir alguma imagem qualquer
    k=random.random()
    if(k>0.75):
        arg = 'imgs/dog1.jpeg'
    elif(k>0.5):
        arg = 'imgs/dog2.jpeg'
    elif(k>0.25):
        arg = 'imgs/dog3.jpeg'
    else:
        arg = 'imgs/dog4.jpeg'

img = Image.open(arg)

a = np.asarray(img) #Carrega imagem como ARRAY

tam = img.size #tamanho da imagem
x = tam[1]
y = tam[0]

if(x<126 and y<126): #ver se a imagem é pequena para gerar ela em txt
    print('gerar codigo ASCI no final!')
    fazerASCI=True

#nova array que vai receber os valores RGB da array 'a'
#através dos dados transformarei a imagem em PRETO E BRANCO, aplicando um simples algoritimo
arr2 = np.array([[[0,0,0]]*y]*x)

#array que usarei para fazer 'uma imagem' ASCI da imagem,
#é isso mesmo, tentarei transformar imagens pequenas em texto
#caso a imagem tenha até 120x120 de tamanho
arr4 = np.array([[['a']]*y]*x)

for x1 in range(x): #correr todas as colunas(embora estamos usando a variavel X)
    for y1 in range(y): #correr todas as linhas das arrays
        try: #para evitar algo fora de valor
            #recuero as variaveis RGB de cada pixel
            r = int(a[x1,y1,0])
            g = int(a[x1,y1,1])
            b = int(a[x1,y1,2])
            c = r + g + b           #somo R + G + B
            z = int(c/3)            #divido por 3 e temos a imagem em tons de cinza

            arr2[x1][y1][0] = z
            arr2[x1][y1][1] = z
            arr2[x1][y1][2] = z

            if(fazerASCI):
                arr4[x1][y1][0] = codasci(z) #função que transforma o valor RGB em TEXTO

        except:
            print('erro')

if(fazerASCI):
    arquivo = (arg.split('/')[1]).split('.')[0] + '.txt'
    arquivo = 'txtImgs/'+arquivo
    print(arquivo)

    with open(arquivo, 'w') as output:
        for x1 in range(x):
            txt = ''
            for y1 in range(y):
                txt += str(arr4[x1][y1][0])
            print(txt)
            txt += '\n'
            output.write(txt)
        print('arquivo txt salvo')

#Abrir imagem em tons de cinza
img2 = Image.fromarray(arr2.astype('uint8'),mode='RGB')
img2.show()

