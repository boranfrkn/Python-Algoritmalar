#Verilen stringin palindrom olup olmadığını bulan fonksiyonu yazın.
string = input("Metin giriniz:")
def palindrom(string):
    if string == string[::-1]:
        print("Girdiğiniz metin palindromdur.")
    else:
        print("Girdiğiniz metin palindrom değildir.")
palindrom(string)
