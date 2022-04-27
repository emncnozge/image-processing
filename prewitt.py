import cv2
from math import sqrt
import numpy as np

filepath = "lena.tif"
image = cv2.imread(filepath, 0)

xsize = image.shape[0]
ysize = image.shape[1]
prewitt = np.empty((xsize, ysize), int)

# Üst, alt, sağ ve sol kısmı boş olan değerlerde bu yönler aynı değer (image[i,j]) kabul edilmiştir.

# 3x3lük alanda her bir pikselin belirlenmesi
for i in range(xsize):
    for j in range(ysize):
        if i == 0 and j == 0:  # sol en üst
            P1 = P2 = P3 = P4 = P5 = P7 = int(image[i, j])
            P6 = int(image[i, j+1])
            P8 = int(image[i+1, j])
            P9 = int(image[i+1, j+1])

        elif i == 0 and j < ysize-1:  # sol en üst ile sağ en üst arası
            P1 = P2 = P3 = P5 = int(image[i, j])
            P4 = int(image[i, j-1])
            P6 = int(image[i, j+1])
            P7 = int(image[i+1, j-1])
            P8 = int(image[i+1, j])
            P9 = int(image[i+1, j+1])

        elif i == 0 and j == ysize-1:  # sağ en üst
            P1 = P2 = P3 = P5 = P6 = P9 = int(image[i, j])
            P4 = int(image[i, j-1])
            P7 = int(image[i+1, j-1])
            P8 = int(image[i+1, j])

        elif i == xsize-1 and j == 0:  # sol en alt
            P1 = P4 = P5 = P7 = P8 = P9 = int(image[i, j])
            P2 = int(image[i-1, j])
            P3 = int(image[i-1, j+1])
            P6 = int(image[i, j+1])

        elif i == xsize-1 and j < ysize-1:  # sol en alt sağ en alt arası
            P5 = P7 = P8 = P9 = int(image[i, j])
            P1 = int(image[i-1, j-1])
            P2 = int(image[i-1, j])
            P3 = int(image[i-1, j+1])
            P4 = int(image[i, j-1])
            P6 = int(image[i, j+1])

        elif i == xsize-1 and j == ysize-1:  # sağ en alt
            P3 = P5 = P6 = P7 = P8 = P9 = int(image[i, j])
            P1 = int(image[i-1, j-1])
            P2 = int(image[i-1, j])
            P4 = int(image[i, j-1])

        elif 0 < i < xsize-1 and j == 0:  # sol en üst sol en alt arası
            P1 = P4 = P5 = P7 = int(image[i, j])
            P2 = int(image[i-1, j])
            P3 = int(image[i-1, j+1])
            P6 = int(image[i, j+1])
            P8 = int(image[i+1, j])
            P9 = int(image[i+1, j+1])

        elif 0 < i < xsize-1 and j == ysize-1:  # sağ en üst sağ en alt arası
            P3 = P5 = P6 = P9 = int(image[i, j])
            P1 = int(image[i-1, j-1])
            P2 = int(image[i-1, j])
            P4 = int(image[i, j-1])
            P7 = int(image[i+1, j-1])
            P8 = int(image[i+1, j])

        else:  # geri kalan tüm kısımlar
            P1 = int(image[i-1, j-1])
            P2 = int(image[i-1, j])
            P3 = int(image[i-1, j+1])
            P4 = int(image[i, j-1])
            P5 = int(image[i, j])
            P6 = int(image[i, j+1])
            P7 = int(image[i+1, j-1])
            P8 = int(image[i+1, j])
            P9 = int(image[i+1, j+1])

        # Eksenlere göre G hesabı
        Gx = -P1 + P3 - P4 + P6 - P7 + P9
        Gy = P1 + P2 + P3 - P7 - P8 - P9
        # Bileşke büyüklük hesabı
        G = sqrt(Gx**2+Gy**2)

        #Sınırlar
        G = 255 if G > 255 else G

        # Sonucun atanması
        prewitt[i, j] = G

G = 255 if G > 255 else G

# Yeni fotoğrafın gösterilmesi
cv2.imshow("Prewitt ("+filepath+")",prewitt.astype(np.uint8))
cv2.waitKey()
# Yeni fotoğrafın kaydedilmesi
cv2.imwrite('prewitt_'+filepath, prewitt)
