import matplotlib.pyplot as plt
import cv2
from math import sqrt
import numpy as np

filepath = "lena-std.tif"
image = cv2.imread(filepath, 0)

xsize = image.shape[0]
ysize = image.shape[1]

result = np.empty((xsize, ysize), int)

# Üst, alt, sağ ve sol kısmı boş olan değerlerde bu yönler aynı değer kabul edilmiştir.
# 2x2lik matriste sol en üst merkez nokta seçilmiştir

# 2x2lik alanda her bir pikselin belirlenmesi
for i in range(xsize):
    for j in range(ysize):

        if i == 0 and j == ysize-1:  # sağ en üst
            P1 = P2 = P4 = int(image[i, j])
            P3 = int(image[i+1, j])

        elif i == xsize-1 and j == 0:  # sol en alt
            P1 = P3 = P4 = int(image[i, j])
            P2 = int(image[i, j+1])

        elif i == xsize-1 and j < ysize-1:  # sol en alt sağ en alt arası
            P1 = P3 = P4 = int(image[i, j])
            P2 = int(image[i, j+1])

        elif i == xsize-1 and j == ysize-1:  # sağ en alt
            P1 = P2 = P3 = P4 = int(image[i, j])

        elif 0 < i < xsize-1 and j == ysize-1:  # sağ en üst sağ en alt arası
            P1 = P2 = P4 = int(image[i, j])
            P3 = int(image[i+1, j])

        else:  # geri kalan tüm kısımlar
            P1 = int(image[i, j])
            P2 = int(image[i, j+1])
            P3 = int(image[i+1, j])
            P4 = int(image[i+1, j+1])

        # Eksenlere göre G hesabı
        Gx = P1 - P4
        Gy = P2 - P3

        # Bileşke büyüklük hesabı
        G = sqrt(Gx**2+Gy**2)

        # Sonucun atanması
        result[i, j] = G

# Yeni fotoğrafın gösterilmesi
plt.imshow(result, cmap="gray")
plt.show()

# Yeni fotoğrafın kaydedilmesi
cv2.imwrite('robert_'+filepath, result)
