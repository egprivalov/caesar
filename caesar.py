ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet = "abcdefghijklmnopqrstuvwxyz"
ALFAVIT = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
alfavit = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

n=int(input("Введите 1 для шифрования шифром Цезаря или 2 для дешифровки: "))-1

str_in=input("Введите строку для шифрования: ") if not n else input("Введите строку для дешифрования: ")
str_out=""

sdvig=abs(int(input("Введите сдвиг: ")))
sdvig=sdvig if not n else -1*sdvig+1

for i in str_in:
    if i>="A" and i<="Z":
        sdvig=sdvig % 26
        str_out+=ALPHABET[(ALPHABET.find(i)+sdvig)%26]
    elif i>="А" and i<="Я" or i=="Ё":
        sdvig=sdvig % 32
        str_out += ALFAVIT[(ALFAVIT.find(i)+sdvig)%33]
    elif i>="a" and i<="z":
        sdvig=sdvig % 26
        str_out+=alphabet[(alphabet.find(i)+sdvig)%26]
    elif i>="а" and i<="я" or i=="ё":
        sdvig=sdvig % 32
        str_out += alfavit[(alfavit.find(i)+sdvig)%33]
    else:
        str_out+=i
print("Зашифрованная строка: "+str_out)
