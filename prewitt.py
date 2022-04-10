import matplotlib.pyplot as plt
import cv2
from math import sqrt
import numpy as np
filepath = "lena-std.tif"
image = cv2.imread(filepath, 0)

xsize = image.shape[0]
ysize = image.shape[1]

result = np.empty((xsize, ysize), int)

# üst, alt, sağ ve sol kısmı boş olan değerlerde bu yönler aynı değer kabul edilmiştir.

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

        Gx = -P1 + P3 - P4 + P6 - P7 + P9
        Gy = P1 + P2 + P3 - P7 - P8 - P9
        G = sqrt(Gx**2+Gy**2)
        result[i, j] = G

plt.imshow(result, cmap="gray")
plt.show()
cv2.imwrite('resultprewitt.tif', result)
