import matplotlib.pyplot as plt
import cv2

eskimin = 110
eskimax = 250
yenimin = 45
yenimax = 200
max = 0
filepath = "cameraman.tif"
image = plt.imread(filepath)

for i in image:
    for j in i:
        if j > max:
            max = j

yeni = [0] * (max+1)

for i in image:
    for j in i:
        if eskimin <= j <= eskimax:
            yeni[j] = round(((yenimax-yenimin)/(eskimax-eskimin))
                            * (j-eskimin)+yenimin)

for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        if eskimin <= image[i, j] <= eskimax:
            image[i, j] = yeni[image[i, j]]

plt.imshow(image, cmap="gray")
plt.show()

plt.hist(image.flatten(), bins=256)
plt.show()

cv2.imwrite('resultgerme.tif', image)
