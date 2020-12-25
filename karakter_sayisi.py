def karakter_sayisi(string):
    sayac = {}
    for karakter in string:
        if sayac.get(karakter, None) is None:
            sayac[karakter] = 1
        else:
            sayac[karakter] += 1
    return sayac
benim_stringim = "Bu cümlede hangi harften kaç tane var?"
sayac = harf_sayisi(benim_stringim)
print(sayac)
