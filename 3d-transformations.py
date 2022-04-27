from math import sin, cos, radians


def calcMatrixProduct(transformation_matrix, koordinatlar):
    result = []
    for i in range(len(transformation_matrix[0])):
        total = 0
        for j in range(len(koordinatlar)):
            total += float(koordinatlar[j]) * float(transformation_matrix[i][j])
        result.append(total)
    return [result[0], result[1], result[2]]


kenar = int(input("Şeklin kenar sayısını giriniz: "))
koordinatlar = []

for i in range(kenar):
    x = float(input(str(i+1)+". noktanın x koordinatını giriniz: "))
    y = float(input(str(i+1)+". noktanın y koordinatını giriniz: "))
    z = float(input(str(i+1)+". noktanın z koordinatını giriniz: "))
    koordinatlar.append([x, y, z])

islem = 0

while islem != 4:
    print("\nYapılacak işlemi seçiniz.\n\n1. Translation (Öteleme)\n2. Scaling (Ölçeklendirme)\n3. Rotation (Döndürme)\n4. Çıkış Yap")
    islem = int(input("İşlem: "))
    print()
    if islem == 1:  # Translation (Öteleme)
        x_t = float(input("x ekseninde öteleme miktarını giriniz: "))
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
        x_s = float(input("x ekseninde ölçeklendirme miktarını giriniz: "))
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
            "Döndürülecek ekseni giriniz (x, y, z): ").strip().upper()

        if eksen == "X":
            r = float(input("x ekseninde döndürme açısını giriniz: "))
            rotating_matrix = [[1, 0, 0, 0],
                               [0, cos(radians(r)), -sin(radians(r)), 0],
                               [0, sin(radians(r)), cos(radians(r)), 0],
                               [0, 0, 0, 1]]

        if eksen == "Y":
            r = float(input("y ekseninde döndürme açısını giriniz: "))
            rotating_matrix = [[cos(radians(r)), 0, sin(radians(r)), 0],
                               [0, 1, 0, 0],
                               [-sin(radians(r)), 0, cos(radians(r)), 0],
                               [0, 0, 0, 1]]

        if eksen == "Z":
            r = float(input("z ekseninde döndürme açısını giriniz: "))
            rotating_matrix = [[cos(radians(r)), -sin(radians(r)), 0, 0],
                               [sin(radians(r)), cos(radians(r)), 0, 0],
                               [0, 0, 1, 0],
                               [0, 0, 0, 1]]

        for i in range(kenar):
            koordinatlar[i] = calcMatrixProduct(
                rotating_matrix, [koordinatlar[i][0], koordinatlar[i][1], koordinatlar[i][2], 1])

    for i in range(len(koordinatlar)):

        print("\n", str(i+1)+". koordinat -->",
              "x:", koordinatlar[i][0],
              " y:", koordinatlar[i][1],
              " z:", koordinatlar[i][2])
