import random 

x_axis = ['1','2','3','4','5','6','7','8','9']
y_axis = ['a','b','c','d','e','f','g','h','i']
ai_ships = {'carrier': [True, 5], 'battleship': [True, 4], 'cruiser': [True, 3], 'submarine': [True, 3], 'destroyer': [True, 2]}
ai_shipscoord = []


def chooseShip_ai():
    for ship in ai_ships.keys():
        if ai_ships[ship][0] == True:
            ai_ships[ship][0] = False
            sel_ship = ai_ships[ship][1]
            return sel_ship

    


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
    ran_choice = random.randint(0,1)
    start = str(random.choice(y_axis) + random.choice(x_axis))
    if (ran_choice == 0) and (10 - int(start[1])) >= int(ship_len):
        end = start[0] + str(int(start[1])+(ship_len-1))
        return [start, end]
    elif (ran_choice == 1) and (ord('i')-ord(start[0])) >= int(ship_len):
        y_end = (ord(start[0]) + int(ship_len)) - 1
        end = chr(y_end) + start[1]
        return [start, end]
    else:
        return random_coord(ship_len)

def completePath(coord1, coord2):
    ship_coord = []
    if coord1[0].lower() == coord2[0].lower():          
            for i in range(int(coord1[1]), int(coord2[1])+1):
                ship_coord.append(coord1[0] + str(i))
                print(ship_coord)
        #If different row but same column
    elif coord1[1] == coord2[1]:                
        for i in y_axis:
            if (i >= coord1[0]) and (i <= coord2[0]):
                ship_coord.append(i + coord1[1])    
    return ship_coord


send = random_coord(5)
start = send[0]
end = send[1]
print(completePath(start, end))



