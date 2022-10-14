# Template para Checkpoint 02

Atividade avaliativa da matéria Disruptive Architectures IoT e IA 

# Python e OpenCV

**Gabriel de Nicola Gonçalves RM 88803** </br>
**Gustavo de Souza Nascimento RM 88804** </br>
**João Victor Deziderio       RM 88805** </br>
**Nathan Pagliari Augusto     RM 88806** 

**Turma: 2TDSF**

## Objetivo 

R1 - NOTA 6: Use a imagem circulo.png para implementar um código que:

Segmenta apenas as 2 maiores áreas da imagem circulo.png.

Calcule e exiba a área e o centro de massa das regiões segmentadas da imagem. O resultado esperado e uma imagem com marcação no centro indicando o Centro de Massa e o valor da área; 

R2 - NOTA 8: Faz o R1 e

Traça uma reta entre os dois centros segmentados; (máx 0,5 pontos) Calcula o ângulo de inclinação da reta em relação ao plano horizontal, inclinação em graus. O resultado esperado é uma imagem com uma reta entre centros e o valor do ângulo exibido na tela;


R3 - NOTA 10: Faz o R2 e:

Realiza o processamento com imagens dawebcam(executa um script .py). O resultado esperado é uma janela da OpenCV que exibe os contornos dos 2 areas maiores, a reta entre centros dos círculos e o valor do ângulo em relação ao plano horizontal;

R4 - BÔNUS : Faz o R3 e:

Essa é a parte legal do checkpoint. Controla um jogo da sua escolha, o programa irá emular o pressionamento das teclas do teclado em função do ângulo de inclinação (ex: ângulo positivo vira para direita, ângulo negativo vira para esquerda se for um jogo de corrida).

Essa rubrica não pode ser feita no jupyter notebook ou google Colab. Deve ser um script python .py.

## Diagrama do projeto

Imagem para o desenvolvimento da atividade.

<img src="/circulo.png" width="550">

## Como usar 

### Arquivo 
* Baixe o arquivo .ipynb
* importe o arquivo no jupyternotebook ou google Colab e execute tudo

### OpenCV 
* Clone o repositorio
* Verifique se o destinatario do video esta localizado no video capture
* No terminal execute "python OpenCV.py"


Libs para o desenvolvimento do projeto:


- import cv2
- from matplotlib import pyplot as plt
- import numpy as np
- import math

