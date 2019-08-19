# module
"""
# import data
# print(data.person)
# print(data.printName('artha'))
# from data import printName
# print(printName('pratama'))
# built in module
import datetime
now = datetime.datetime.now()
print(now)
print(now.strftime("%Y, %B, %d"))
date = datetime.datetime(2019, 2, 5)
print(date)
"""

# local & global var
"""
nama = "wied"
def printNama():
    global nama#hasus pake ini klo mau ganti lokal var
    nama = nama + "artha"
    print("akses dari dalam " + nama)
printNama()
print("akses dari luar "+nama)
"""