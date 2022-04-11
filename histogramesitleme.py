import matplotlib.pyplot as plt
import cv2

min = 9999999
max = 0

filepath = "lena.tif"
image = plt.imread(filepath)

# RGB fotoğrafı grayscale yapma
if image.ndim!=2:
    try:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    except:
        print("Fotoğraf RGB ya da grayscale değil!")

# Fotoğraftaki en büyük ve en küçük renk değerleri
for i in image:
    for j in i:
        if j < min:
            min = j
        if j > max:
            max = j
            
# Fotoğrafın gri seviyesi (Genellikle 8)
graylevel=0
while True:
    if 2**graylevel>max:
        break
    else:
        graylevel+=1
        
counter = probability = [0] * (2**graylevel)

# Her renk değerinin sayıları
for i in image:
    for j in i:
        counter[j] += 1

# Her pikselin hesaplanması
probability[0] = counter[0]/image.size
for i in range(1, 2**graylevel):
    probability[i] = probability[i-1]+(counter[i]/image.size)

for i in range(len(probability)):
    probability[i] = round(probability[i]*((2**graylevel)-1))

# Yeni değerlerin eski değerler üzerine yazılması
for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        image[i, j] = probability[image[i, j]]

# Yeni fotoğrafın gösterilmesi
plt.imshow(image, cmap="gray")
plt.show()

# Yeni fotoğrafın histogramının gösterilmesi
plt.hist(image.flatten(), bins=2**graylevel)
plt.show()

# Yeni fotoğrafın kaydedilmesi
cv2.imwrite('histeq_'+filepath, image)
