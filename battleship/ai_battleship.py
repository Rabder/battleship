import random 

x_axis = ['1','2','3','4','5','6','7','8','9']
y_axis = ['a','b','c','d','e','f','g','h','i']
player2_ships = {'carrier': [True, 5], 'battleship': [True, 4], 'cruiser': [True, 3], 'submarine': [True, 3], 'destroyer': [True, 2]}
p2_shipscoord = []


def chooseShip_ai():
    for ship in player2_ships:
        if player2_ships[ship][0] == True:
            print(ship)
    sel_ship = random.choice(player2_ships.keys())
    return(sel_ship)


# def sketch(p2_shipscoord):
#     for y in y_axis:
#         print(y, end=" ")
#         for x in x_axis:
#             xd = False
#             for ship in p2_shipscoord:
#                 for coord in ship:
#                     if coord == str(y+x):
#                         print("◙", end=" ")
#                         xd = True
#             if (xd == False):
#                 print("□",end=" ")

#         print("")
#     print("  ", end="")
#     for x in x_axis:
#         print(x, end=" ")

def random_coord(ship_len):
    start = str(random.choice(y_axis) + random.choice(x_axis))
    if (10 - int(start[1])) >= int(ship_len):
        end = start[0] + str(int(start[1])+(ship_len-1))
        return [start, end]
    else:
        return random_coord(ship_len)
    


print(random_coord(5))



