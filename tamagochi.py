name = input("masukan nama monster: ")
monster = {
    "name": name,
    "power": 100
}
def startGame():
    choise = input("Mau Apa? 1.makan 2.lihatStatus 3.exit ")
    if choise == "1":
        goEat()
    elif choise == "2":
        goStatus()
    else:
        goExit()

def goEat():
    print("nyam.. nyam..")
    monster['power'] += 100
    startGame()

def goStatus():
    print("Check.. Check..")
    print(monster)
    startGame()

def goExit():
    print("bye.. bye..")

startGame()