#Verilen bir string'in pangram olup olmadığını bulan fonksiyon yazın.
#Pangram: Alfabedeki bütün harfleri içeren cümle.
import string
def pangram(cumle):
    alfabe = "abcçdefgğhiıjklmnoöprsştuüvyz"
    sayac = {}
    for karakter in alfabe:
        sayac[karakter] = 0
    for karakter in cumle:
        if karakter != " ":
            sayac[karakter] += 1
    return 0 not in sayac.values()
cumle = "Cılız ve duygulu japon balığı Fethi sıçcarken ölmüş"
print(pangram(cumle.lower()))
