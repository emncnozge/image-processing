from math import sin, cos, radians
import matplotlib.pyplot as plt # grafik çizdirmek için
from mpl_toolkits.mplot3d.art3d import Poly3DCollection # grafik çizdirmek için


def calcMatrixProduct(transformation_matrix, koordinatlar):
    result = []
    for i in range(len(transformation_matrix[0])):
        total = 0
        for j in range(len(koordinatlar)):
            total += float(koordinatlar[j]) * float(transformation_matrix[i][j])
        result.append(total)
    return [result[0], result[1], result[2]]


kenar = int(input("Şeklin kenar sayısını giriniz: "))
koordinatlar = list()

for i in range(kenar):
    x = float(input(str(i+1)+". noktanın x koordinatını giriniz: "))
    y = float(input(str(i+1)+". noktanın y koordinatını giriniz: "))
    z = float(input(str(i+1)+". noktanın z koordinatını giriniz: "))
    koordinatlar.append((x, y, z))

islem = 0

while islem != 5:
    print("\nYapılacak işlemi seçiniz.\n\n1. Translation (Öteleme)\n2. Scaling (Ölçeklendirme)\n3. Rotation (Döndürme)\n4. Şekli çizdir. \n5. Çıkış Yap")
    islem = int(input("İşlem: "))
    if islem == 1:  # Translation (Öteleme)
        x_t = float(input("\nx ekseninde öteleme miktarını giriniz: "))
        y_t = float(input("y ekseninde öteleme miktarını giriniz: "))
        z_t = float(input("z ekseninde öteleme miktarını giriniz: "))
        translation_matrix = [[1, 0, 0, x_t],
                              [0, 1, 0, y_t],
                              [0, 0, 1, z_t],
                              [0, 0, 0, 1]]

        for i in range(kenar):
            koordinatlar[i] = calcMatrixProduct(
                translation_matrix, [koordinatlar[i][0], koordinatlar[i][1], koordinatlar[i][2], 1])

    if islem == 2:  # Scaling (Ölçeklendirme)
        x_s = float(input("\nx ekseninde ölçeklendirme miktarını giriniz: "))
        y_s = float(input("y ekseninde ölçeklendirme miktarını giriniz: "))
        z_s = float(input("z ekseninde ölçeklendirme miktarını giriniz: "))
        scaling_matrix = [[x_s, 0, 0, 0],
                          [0, y_s, 0, 0],
                          [0, 0, z_s, 0],
                          [0, 0, 0, 1]]
        for i in range(kenar):
            koordinatlar[i] = calcMatrixProduct(
                scaling_matrix, [koordinatlar[i][0], koordinatlar[i][1], koordinatlar[i][2], 1])

    if islem == 3:  # Rotation(Döndürme)
        eksen = input(
            "\nDöndürülecek ekseni giriniz (x, y, z): ").strip().upper()

        if eksen == "X":
            r = float(input("\nx ekseninde döndürme açısını giriniz: "))
            rotating_matrix = [[1, 0, 0, 0],
                               [0, cos(radians(r)), -sin(radians(r)), 0],
                               [0, sin(radians(r)), cos(radians(r)), 0],
                               [0, 0, 0, 1]]

        if eksen == "Y":
            r = float(input("\ny ekseninde döndürme açısını giriniz: "))
            rotating_matrix = [[cos(radians(r)), 0, sin(radians(r)), 0],
                               [0, 1, 0, 0],
                               [-sin(radians(r)), 0, cos(radians(r)), 0],
                               [0, 0, 0, 1]]

        if eksen == "Z":
            r = float(input("\nz ekseninde döndürme açısını giriniz: "))
            rotating_matrix = [[cos(radians(r)), -sin(radians(r)), 0, 0],
                               [sin(radians(r)), cos(radians(r)), 0, 0],
                               [0, 0, 1, 0],
                               [0, 0, 0, 1]]

        for i in range(kenar):
            koordinatlar[i] = calcMatrixProduct(
                rotating_matrix, [koordinatlar[i][0], koordinatlar[i][1], koordinatlar[i][2], 1])

    if islem == 4:
        xmax = -999999
        xmin = 999999
        ymax = -999999
        ymin = 999999
        zmax = -999999
        zmin = 999999

        for i in range(len(koordinatlar)):
            if xmax < koordinatlar[i][0]:
                xmax = koordinatlar[i][0]
            if xmin > koordinatlar[i][0]:
                xmin = koordinatlar[i][0]
            if ymax < koordinatlar[i][1]:
                ymax = koordinatlar[i][1]
            if ymin > koordinatlar[i][1]:
                ymin = koordinatlar[i][1]
            if zmax < koordinatlar[i][2]:
                zmax = koordinatlar[i][2]
            if zmin > koordinatlar[i][2]:
                zmin = koordinatlar[i][2]

        fig = plt.figure()
        ax = fig.add_subplot(projection="3d")
        ax.add_collection(Poly3DCollection([koordinatlar]))
        ax.set_xlim([xmin-2, xmax+2])
        ax.set_ylim([ymin-2, ymax+2])
        ax.set_zlim([zmin-2, zmax+2])
        plt.show()

    for i in range(len(koordinatlar)):

        print("\n", str(i+1)+". koordinat -->",
              "x:", koordinatlar[i][0],
              " y:", koordinatlar[i][1],
              " z:", koordinatlar[i][2])
