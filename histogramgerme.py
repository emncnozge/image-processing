import matplotlib.pyplot as plt
import cv2

eskimin = 40
eskimax = 103
yenimin = 90
yenimax = 200
max = 0

filepath = "lena-std.tif"
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
            
graylevel=0
# Fotoğrafın gri seviyesi
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
