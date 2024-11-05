#Aventura de Texto

#Room
room_des = [
    ["A", "B", "C", "D", "E"],
    ["F", "G", "H", "I", "J"],
    ["K", "L", "M", "N", "O"],
    ["P", "Q", "R", "S", "T"],
    ["U", "V", "W", "X", "Y"]
]

#Directions
NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

#where u can move
room_exits = [ 
    [(False,True,True,False), (False,True,True,True), (False,True,True,True), (False,True,True,True), (False,True,True,False)],
    [(True,True,True,False), (True,True,True,True), (True,True,True,True), (True,True,True,True), (True,True,True,False)],
    [(True,True,True,False), (True,True,True,True), (True,True,True,True), (True,True,True,True), (True,True,True,False)],
    [(True,True,True,False), (True,True,True,True), (True,True,True,True), (True,True,True,True), (True,True,True,False)],
    [(True,True,False,False), (True,True,False,True), (True,True,False,True), (True,True,False,True), (True,True,False,False)]
    ]


#Where u start
position = (0, 1)

while (True):

    x, y = position
    descrip = room_des[y][x]
    print(position, ":", descrip)


    print("What now?")
    command = input()

    if (command == "north"):
        if (room_exits[y][x][NORTH]):
            print("You move north....")
            y = y -1
        else:
            print("You can't")

    elif (command == "south"):
        if (room_exits[y][x][SOUTH]):
            print("You move south....")
            y = y +1
        else:
            print("You can't")

    elif (command == "west"):
        if (room_exits[y][x][WEST]):
            print("You move west....")
            x = x -1
        else:
            print("You can't")
            
    elif (command == "east"):
        if (room_exits[y][x][EAST]):
            print("You move east....")
            x = x +1
        else:
            print("You can't")
    else:
        print("I dont understand " + command + "!")

    #new position
    position = (x,y)