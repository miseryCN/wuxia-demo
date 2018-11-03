from server.equipment import Equipment,Item
from server.character import Player
import server.constants as constants
import random

players = []

for i in range(0,100):
    player = Player()
    player.set_name(constants.names[random.randint(0,len(constants.names)-1)])
    for j in range(0,100):
        player.level_up()
        if j > random.randint(1, 100):
            break

    player.get_all()
    players.append(player)
