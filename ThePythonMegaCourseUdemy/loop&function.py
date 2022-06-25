def celciousToKelvin(temp):
    return temp + 273.15

for x in [0, 2, 5, 10, 100, -270.15]:
    print(celciousToKelvin(x))