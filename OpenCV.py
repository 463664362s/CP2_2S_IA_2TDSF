import cv2
from matplotlib import pyplot as plt
import numpy as np
import math



def image_da_webcam(img):

    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    image_lower_hsv1 = np.array([120,100,100])
    image_upper_hsv1 = np.array([180,200,255])

    mask_hsv1 = cv2.inRange(img_hsv, image_lower_hsv1, image_upper_hsv1)

    image_lower_hsv2 = np.array([80, 50, 100])  
    image_upper_hsv2 = np.array([105, 255, 255])

    mask_hsv2 = cv2.inRange(img_hsv, image_lower_hsv2, image_upper_hsv2)

    saida = cv2.bitwise_or(mask_hsv1,mask_hsv2)

    contornos, _ = cv2.findContours(saida, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    mask_rgb = cv2.cvtColor(saida, cv2.COLOR_GRAY2RGB) 
    contornos_img = mask_rgb.copy() 
    cv2.drawContours(contornos_img, contornos, -1, [255, 0, 0], 3)



    contornosRed, _ = cv2.findContours(mask_hsv1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
    mask_rgb = cv2.cvtColor(mask_hsv1, cv2.COLOR_GRAY2RGB) 
    contornos_img_red = mask_rgb.copy()
    cv2.drawContours(contornos_img_red, contornosRed, -1, [255, 0, 0], 3)

    contornosCian, _ = cv2.findContours(mask_hsv2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
    mask_rgb = cv2.cvtColor(mask_hsv2, cv2.COLOR_GRAY2RGB) 
    contornos_img_cian = mask_rgb.copy() 
    cv2.drawContours(contornos_img_cian, contornosCian, -1, [255, 0, 0], 3)


    maior = None
    maior_area = 0
    maior2 = None
    maior_area2 = 0
    for c in contornosRed:
        area = cv2.contourArea(c)
        if area > maior_area:
            maior_area = area
            maior = c
    for a in contornosCian:
        area = cv2.contourArea(a)
        if area > maior_area2:
            maior_area2 = area
            maior2 = a

    

    cv2.drawContours(contornos_img_red, [maior], -1, [0, 255, 0], 15)
    cv2.drawContours(contornos_img_cian, [maior2], -1, [0, 255, 0], 15)

    saida = cv2.bitwise_or(contornos_img_cian,contornos_img_red)

    MRed = cv2.moments(maior)
    MCian = cv2.moments(maior2)

    cxRed = int(MRed['m10']/MRed['m00'])
    cyRed = int(MRed['m01']/MRed['m00'])

    cxCian = int(MCian['m10']/MCian['m00'])
    cyCian = int(MCian['m01']/MCian['m00'])

    size = 30
    color = (255,0,0)

    cv2.line(contornos_img_cian,(cxCian - size,cyCian),(cxCian + size,cyCian),color,5)
    cv2.line(contornos_img_cian,(cxCian,cyCian - size),(cxCian, cyCian + size),color,5)

    font = cv2.FONT_HERSHEY_SIMPLEX
    text = maior_area2, cyCian , cxCian
    origem = (1500,30)

    cv2.putText(contornos_img_cian, str(text), origem, font,1,[255, 0, 0],2,cv2.LINE_AA)


    cv2.line(contornos_img_red,(cxRed - size,cyRed),(cxRed + size,cyRed),color,5)
    cv2.line(contornos_img_red,(cxRed,cyRed - size),(cxRed, cyRed + size),color,5)

    font = cv2.FONT_HERSHEY_SIMPLEX
    text = maior_area, cyRed , cxRed
    origem = (0,30)


    cv2.putText(contornos_img_red, str(text), origem, font,1,[255, 0, 0],2,cv2.LINE_AA)


    saida = cv2.bitwise_or(contornos_img_cian,contornos_img_red)

    
    color = (0, 100, 0)

    cv2.line(saida,(cxCian , cyCian),(cxRed , cyRed),color,5)

    p_interno = (cxCian*cxRed)+(cyCian*cyRed)
    modulo_cian= math.sqrt(((cxCian**2) + (cyCian**2)))
    modulo_red = math.sqrt(((cxRed**2) + (cyRed**2)))
    angulo= p_interno/(modulo_cian*modulo_red)

    angulo_final= math.acos(angulo) 
    final= round(math.degrees(angulo_final),2)


    font = cv2.FONT_HERSHEY_SIMPLEX
    text = final 
    origem = (800,500)
    cv2.putText(saida, str(text), origem, font,1,(200,0,0),2,cv2.LINE_AA)
    cv2.line(saida,(cxCian , cyCian),(cxRed , cyRed),color,3)

    return saida

cv2.namedWindow("preview")
vc = cv2.VideoCapture('video.mp4')

vc.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
vc.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)


if vc.isOpened(): 
    rval, frame = vc.read()
else:
    rval = False

while rval:

    img = image_da_webcam(frame) 
    cv2.imshow("preview", img)
    cv2.imshow("original", frame)
    rval, frame = vc.read()
    key = cv2.waitKey(20)
    if key == 27: 
        break

cv2.destroyWindow("preview")
vc.release()