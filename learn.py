# input
"""
nama = input("siapa nama anda? \t")
umur = input("umur anda berapa? \t")
print("nama anda: " + nama + "\numur anda: " + umur)
"""

# true false
"""
text = "wap"
print(text.isdigit())
print(text.isalnum())
"""

# if else
"""
angka1 = 10
angka2 = 20
if angka1 > angka2 :
    print("benar")
else :
    print("salah")
"""

# if else lanjut
"""
uang = input("berapa uang anda? ")
utang = 10000
uang = int(uang)
if uang < utang:
    print("uang anda kurang")
elif uang == utang:
    print("uang anda pas")
else:
    print("uang anda banyak")
"""

# operator logika
# and or not
#  &  |  !=
"""
syarat1 = True
syarat2 = False
if syarat1 & syarat2:
    print("benar")
else:
    print("salah")
"""

# loop
# while
"""
count = 1
while count < 5:
    print("print ini")
    count = count+1
else :
    print("selesai")
"""
# for
"""
orang = ["wied", "artha", "pratama"]
for nama in orang:
    print("nama namanya adalah", nama)
"""
"""
text = "ptyhon"
for huruf in text :
    print("hurufnya", huruf)
"""

# loop bercabang
"""
a = 1
while a < 5:
    b = 0
    while b < a:
        print("*", end='')
        b = b+1
    print()
    a = a+1
"""

# list 
"""
orang = ['wied', 'artha', 'pratama']
umur = [3,6,8,4,7]
mixed = [3,'apalu',3.5,'pos']
orang.append('wap')#tambah
orang[1] = 'ata'#edit
del orang[2]#hapus
print(orang)
"""

# tuple
"""
orang = ('wied','artha','pratama')
orang2 = ['wied','artha','pratama']
print(len(orang))
print(list(orang))#tuple to list
print(tuple(orang2))#list to tuple
"""

# dictionary
"""
data = {
    "name": 'wap',
    "age": '20',
    "hobby": 'molor'
}
data['dream'] = 'harem'#add
data['name'] = 'wied'#update
del data['age']#delete
print(data)
print("namanya adalah "+data['name'])
for key, value in data.items():
    print(key + ' - ' + value)
"""

# nested dictionary
"""
data = {
    1:{
        "name": 'wied',
        "age": '20',
        "hobby": 'molor'
    },
    2:{
        "name": 'artha',
        "age": '21',
        "hobby": 'olga'
    },
}
# print(data[1]['name'])
for key, value in data.items():
    print("\nkeynya:", key)
    for key2 in value:
        print(key2 + ' - ' + value[key2])
"""

# Set
"""
# orang = {'wied','artha','pratama','wied'}
# print(orang)
angka1 = {1,2,3,4,5}
angka2 = {4,5,6,7,8}
print(angka1 | angka2)
print(angka1 & angka2)
print(angka1 ^ angka2)
"""

# function

# def printYow():
#     print('-----')
#     print(' YOW ')
#     print('-----')
# printYow()
# def printNiceText(text='kosong'):
#     print('-----')
#     print(text)
#     print('-----')
# printNiceText('wied')
# printNiceText('artha')
# printNiceText('pratama')
# printNiceText()
# def hitung(a, b):
#     print('jumlah a dan b', a + b)
# hitung(10, 20)
# hitung(3252352, 5235235)
# return
# def hitung(a, b):
#     return a + b
# hasil = hitung(10, 20)
# print(hasil)
def printData(nama, hobby):
    print('Nama: '+nama+' - Hobby: '+hobby)
printData(nama='wied', hobby='ps')