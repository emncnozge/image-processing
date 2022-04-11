import matplotlib.pyplot as plt
import cv2

eskimin = 110
eskimax = 250
yenimin = 45
yenimax = 200
max = 0
filepath = "cameraman.tif"
image = plt.imread(filepath)

# Fotoğraftaki en büyük renk değeri
for i in image:
    for j in i:
        if j > max:
            max = j

yeni = [0] * (max+1)

# Her pikselin hesaplanması
for i in image:
    for j in i:
        if eskimin <= j <= eskimax:
            yeni[j] = round(((yenimax-yenimin)/(eskimax-eskimin))
                            * (j-eskimin)+yenimin)

# Eski değerlerin üstüne yeni değerlerin yazılması
for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        if eskimin <= image[i, j] <= eskimax:
            image[i, j] = yeni[image[i, j]]

# Yeni fotoğrafın gösterilmesi
plt.imshow(image, cmap="gray")
plt.show()

# Yeni fotoğrafın histogramının gösterilmesi
plt.hist(image.flatten(), bins=256)
plt.show()

# Yeni fotoğrafın kaydedilmesi
cv2.imwrite('histstr_'+filepath, image)
