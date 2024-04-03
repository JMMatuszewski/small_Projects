import random,sys,copy

"""Conways game of life"""

#Screen size
WIDTH = 60
HEIGHT = 20

#Cell status
ALIVE = "O"
DEAD = " "

#Methods
def Draw(database):
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(database[(x,y)],end='')
        print()

#First draw
next_cell_database = {}
for y in range(HEIGHT):
    for x in range(WIDTH):
        if random.randint(0,1) == 1:
            next_cell_database[(x,y)] = ALIVE
        else:
            next_cell_database[(x,y)] = DEAD


"""Main loop of the program"""
while True:

    Draw(next_cell_database)
    # Prepare database for next loop
    cell_database = copy.deepcopy(next_cell_database)

    #Preparation for checking neighbours

    for y in range(HEIGHT):
        for x in range(WIDTH):

            neighbour = 0
            # Coordinates for neighbours
            left = (x-1) % WIDTH
            right = (x+1) % WIDTH
            top = (y+1) % HEIGHT
            bottom = (y-1) % HEIGHT

            # Count neighbours
            if cell_database[(left,top)] == ALIVE:
                neighbour += 1
            if cell_database[(x,top)] == ALIVE:
                neighbour += 1
            if cell_database[(right,top)] == ALIVE:
                neighbour += 1
            if cell_database[(right,y)] == ALIVE:
                neighbour += 1
            if cell_database[(right,bottom)] == ALIVE:
                neighbour += 1
            if cell_database[(x,bottom)] == ALIVE:
                neighbour += 1
            if cell_database[(left,bottom)] == ALIVE:
                neighbour += 1
            if cell_database[(left,y)] == ALIVE:
                neighbour += 1

            # Update cell_database
            if  cell_database[(x,y)] == ALIVE and \
                neighbour in (2,3):
                # keep being alive due to 2-3 neighbours
                next_cell_database[(x,y)] = ALIVE
            elif cell_database[(x,y)] == DEAD and \
                neighbour == 3:
                # come back to life due to 3 neighbours
                next_cell_database[(x,y)] = ALIVE
            else:
                # rest of the cells die out
                next_cell_database[(x,y)] = DEAD
    
    print()
    button = input("(E)xit or press Enter to see the next cycle...")
    print()
    
    if button.upper() == 'E':
        sys.exit()
