import matplotlib.pyplot as plt
import cv2

min = 9999999
max = 0

filepath = "cameraman.tif"
image = plt.imread(filepath)

# Fotoğraftaki en büyük ve en küçük renk değerleri
for i in image:
    for j in i:
        if j < min:
            min = j
        if j > max:
            max = j

counter = probability = [0] * (max+1)

# Her renk değerinin sayıları
for i in image:
    for j in i:
        counter[j] += 1

# Her pikselin hesaplaması
probability[0] = counter[0]/image.size

for i in range(1, max+1):
    probability[i] = probability[i-1]+(counter[i]/image.size)

for i in range(len(probability)):
    probability[i] = round(probability[i]*(max-min))

# Yeni değerlerin eski değerler üzerine yazılması
for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        image[i, j] = probability[image[i, j]]

# Yeni fotoğrafın gösterilmesi
plt.imshow(image, cmap="gray")
plt.show()

# Yeni fotoğrafın histogramının gösterilmesi
plt.hist(image.flatten(), bins=256)
plt.show()

# Yeni fotoğrafın dosyaya yazılması
cv2.imwrite('histeq_'+filepath, image)
