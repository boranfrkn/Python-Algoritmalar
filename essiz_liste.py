#Verilen listedeki tekrarlanan elemanları silip, sadece benzersiz elemanlardan olusan bir liste donduren bir fonksiyon yazın.
liste = [1, 1, 1, 1, 2, 2, 3, 3, 3, 'a', 'a', 'b', 'b']
def essiz_liste(liste):
    return list(set(liste))
essiz_listem = essiz_liste(liste)
print(essiz_listem)
