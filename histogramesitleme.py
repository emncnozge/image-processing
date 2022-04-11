import matplotlib.pyplot as plt
import cv2

min = 9999999
max = 0
filepath = "cameraman.tif"
image = plt.imread(filepath)

for i in image:
    for j in i:
        if j < min:
            min = j
        if j > max:
            max = j

counter = probability = [0] * (max+1)

for i in image:
    for j in i:
        counter[j] += 1

probability[0] = counter[0]/image.size

for i in range(1, max+1):
    probability[i] = probability[i-1]+(counter[i]/image.size)

for i in range(len(probability)):
    probability[i] = round(probability[i]*(max-min))

for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        image[i, j] = probability[image[i, j]]

plt.imshow(image, cmap="gray")
plt.show()

plt.hist(image.flatten(), bins=256)
plt.show()

cv2.imwrite('resultesitleme.tif', image)
