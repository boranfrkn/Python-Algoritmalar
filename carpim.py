#Verlin listedeki bütün numaraları birbiriyle çarpıp sonucu döndüren bir fonksiyon yazın.
liste = [1, 2, 3, 4, 5, 6]
def hepsini_carp(liste):
    sonuc = 1
    for i in liste:
        sonuc *= i
    return sonuc
print(hepsini_carp(liste))
