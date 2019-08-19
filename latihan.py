player1 = {
    "name": "luffy",
    "power": 1500
}
player2 = {
    "name": "kaido",
    "power": 5000
}

def train(player):
    player['power'] += 1000

def attack(attacker, defender):
    if(attacker['power'] > defender['power']):
        print('selamat '+attacker['name']+' menang melawan '+defender['name'])
    elif (attacker['power'] == defender['power']):
        print('waduh 22nya kalah')
    else:
        print('sayang sekali '+attacker['name']+' gagal mengalahkan '+defender['name'])

train(player1)
train(player1)
train(player1)
train(player1)
train(player2)
attack(player1, player2)