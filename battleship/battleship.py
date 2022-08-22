x_axis = ['1','2','3','4','5','6','7','8','9']
y_axis = ['a','b','c','d','e','f','g','h','i']
player1_ships = {'carrier': [True, 5], 'battleship': [True, 4], 'cruiser': [True, 3], 'submarine': [True, 3], 'destroyer': [True, 2]}
player2_ships = {'carrier': True, 'battleship': True, 'cruiser': True, 'submarine': True, 'destroyer': True}
p1_shipscoord = []


def chooseShip():
    check = False
    print("Available ships")
    for ship in player1_ships:
        if player1_ships[ship][0] == True:
            print(ship)
    sel_ship = input("Choose a ship: ")
    for key in player1_ships.keys():
        if sel_ship == key:
            check = True
    if check == True:
        if player1_ships[sel_ship.lower()][0] == False:
            print("Error 404")
            chooseShip()
        else:
            print(f"You have selected a {sel_ship.lower()}")
            player1_ships[sel_ship.lower()][0] = False
            return sel_ship
    else:
        print("Invalid selection")
        print("")
        return chooseShip()


def sketch(p1_shipscoord):
    for y in y_axis:
        print(y, end=" ")
        for x in x_axis:
            xd = False
            for ship in p1_shipscoord:
                for coord in ship:
                    if coord == str(y+x):
                        print("◙", end=" ")
                        xd = True
            if (xd == False):
                print("□",end=" ")

        print("")
    print("  ", end="")
    for x in x_axis:
        print(x, end=" ")


def p1_board():
    
    def graph(coord1, coord2, ship_len):
        ship_coord = []
        #If on same row but different column
        if coord1[0].lower() == coord2[0].lower():          
            for i in range(int(coord1[1]), int(coord2[1])+1):
                ship_coord.append(coord1[0] + str(i))
                print(ship_coord)
        #If different row but same column
        elif coord1[1] == coord2[1]:                
            for i in y_axis:
                if (i >= coord1[0]) and (i <= coord2[0]):
                    ship_coord.append(i + coord1[1])
        
        if len(ship_coord) != ship_len[1]:
            print("Invalid selection")
            ship_len[0] = True
            ship_coord = []
            p1_board()
        for list in p1_shipscoord:
            for item in list:
                for coord in ship_coord: 
                    if coord == item:
                        print("Invalid selection")
                        ship_len[0] = True
                        ship_coord = []
                        p1_board()
        p1_shipscoord.append(ship_coord)

        for y in y_axis:
            print(y, end=" ")
            for x in x_axis:
                xd = False
                for ship in p1_shipscoord:
                    for coord in ship:
                        if coord == str(y+x):
                            print("◙", end=" ")
                            xd = True
                if (xd == False):
                    print("□",end=" ")

            print("")
        print("  ", end="")
        for x in x_axis:
            print(x, end=" ")
        
    
    print("")
    ship_sel = chooseShip()
    print("")
    sketch(p1_shipscoord)
    print("")
    start = input("Starting position: ")
    end = input("Ending position: ")
    print("")
    graph(start, end, player1_ships[ship_sel])
    print(p1_shipscoord)
    

def gameplay(total_hits):
    check_hit = False
    print("")
    guess = input("Guess a coordinate: ")
    if len(guess) != 2 or not ((guess[0].lower() in y_axis) and (guess[1] in x_axis)):
        gameplay(total_hits)
    else:
        for ship_coords in p1_shipscoord:
            if total_hits == 17:
                print("You win!")
                return 0
            if guess in ship_coords:
                check_hit = True
                sketch(p1_shipscoord)
                print("")
                print("HIT")
                print("")
                total_hits += 1
                ship_coords.remove(guess)
                gameplay(total_hits)
        if check_hit == False:     
            print("")
            print("MISS")
            print("")
            sketch(p1_shipscoord)
            gameplay(total_hits)
    


for i in range(0, 5):
    p1_board()
    print("")
gameplay(0)


