import matplotlib.pyplot as plt
import cv2
import numpy as np

filepath = "lena.tif"
image = cv2.imread(filepath, 0)

xsize = image.shape[0]
ysize = image.shape[1]

result = np.empty((xsize, ysize), int)

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

        # 45 derece döndürülerek hesaplanan tüm G değerleri
        G0 = -P1-P2-P3+P4-2*P5+P6+P7+P8+P9
        G45 = -P1-P2+P3-P4-2*P5+P6+P7+P8+P9
        G90 = -P1+P2+P3-P4-2*P5+P6-P7+P8+P9
        G135 = P1+P2+P3-P4-2*P5+P6-P7-P8+P9
        G180 = P1+P2+P3+P4-2*P5+P6-P7-P8-P9
        G225 = P1+P2+P3+P4-2*P5-P6+P7-P8-P9
        G270 = P1+P2-P3+P4-2*P5-P6+P7+P8-P9
        G315 = P1-P2-P3+P4-2*P5-P6+P7+P8+P9

        # İçlerinden en büyük olan değerin alınması
        G = max(G0, G45, G90, G135, G180, G225, G270, G315)

        # Sonucun atanması
        result[i, j] = G

# Yeni fotoğrafın gösterilmesi
plt.imshow(result, cmap="gray")
plt.show()

# Yeni fotoğrafın kaydedilmesi
cv2.imwrite('compass_'+filepath, result)
