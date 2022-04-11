# 1306190022 - Emin Can ÖZGE
# Python 3.10.4

import matplotlib.pyplot as plt
import cv2


eskimin = int(input("Eski aralıktaki minimum değer: "))
eskimax = int(input("Eski aralıktaki maksimum değer: "))
yenimin = int(input("Yeni aralıktaki minimum değer: "))
yenimax = int(input("Yeni aralıktaki maksimum değer: "))

max = 0

filepath = "lena.tif"
image = plt.imread(filepath)

# RGB fotoğrafı grayscale yapma
if image.ndim!=2: 
    try:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    except:
        print("Fotoğraf RGB ya da grayscale değil!")

# Fotoğraftaki en büyük renk değeri
for i in image:
    for j in i:
        if j > max:
            max = j
            
# Fotoğrafın gri seviyesi (Genellikle 8)
graylevel=0
while True:
    if 2**graylevel>max:
        break
    else:
        graylevel+=1
    
yeni = [0] * (2**graylevel)

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
plt.hist(image.flatten(), bins=2**graylevel)
plt.show()

# Yeni fotoğrafın kaydedilmesi
cv2.imwrite('histstr_'+filepath, image)
