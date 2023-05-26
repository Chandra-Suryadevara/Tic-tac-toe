from Tile import Tile

class Board:
    def __init__(self):
        self.tiles=[[Tile for _ in range(3)]for _ in range(3)]
    

    def Mark(self, Coordinates, str):
     self.Coordi_x = Coordinates[0]
     self.Coordi_y = Coordinates[1]
     return (self.tiles[self.Coordi_x][self.Coordi_y]).Mark(str)

     def Reset(self):
         for x in range(3):
             for y in range(3):
                (self.tiles[x][y]).Erase()

    def PrintBoard(self):
     print(" ")
     for i in range(3):
        for j in range(3):
            if self.tiles[i][j].value() == None:
                print("  ", end="")  
                print(f"{self.tiles[i][j].Print():2d}", end="")
            if j != 2:
                print(" | ", end="")  
        if i != 2:
            print("--------------")  

    def CheckWinner(self):
        if (self.tiles[0][0]).Check_Mark():
            markedtile = (self.tiles[0][0]).Print()
            if ((self.tiles[0][1]).Print()) == markedtile:
                if ((self.tiles[0][2]).Print()) == markedtile:
                    print("Winner is ", markedtile)
                    return True
            elif ((self.tiles[1][1]).Print()) == markedtile:
                if ((self.tiles[2][2]).Print()) == markedtile:
                    print("Winner is ", markedtile)
                    return True      
            elif ((self.tiles[1][0]).Print()) == markedtile:
                if ((self.tiles[2][0]).Print()) == markedtile:
                    print("Winner is ", markedtile)
                    return True
        if (self.tiles[0][1]).Check_Mark():
             markedtile = (self.tiles[0][1]).Print()
             if ((self.tiles[1][1]).Print()) == markedtile:
                if ((self.tiles[2][1]).Print()) == markedtile:
                    print("Winner is ", markedtile)
                    return True
        if (self.tiles[0][2]).Check_Mark():
            markedtile = (self.tiles[0][2]).Print()
            if ((self.tiles[1][2]).Print()) == markedtile:
                if ((self.tiles[2][2]).Print()) == markedtile:
                    print("Winner is ", markedtile)
                    return True
            elif ((self.tiles[1][1]).Print()) == markedtile:
                if ((self.tiles[2][0]).Print()) == markedtile:
                    print("Winner is ", markedtile)
                    return True   
        if (self.tiles[1][0]).Check_Mark():
            markedtile = (self.tiles[1][0]).Print()
            if ((self.tiles[1][1]).Print()) == markedtile:
                if ((self.tiles[1][2]).Print()) == markedtile:
                    print("Winner is ", markedtile)
                    return True
        if (self.tiles[2][0]).Check_Mark():
            markedtile = (self.tiles[2][0]).Print()
            if ((self.tiles[2][1]).Print()) == markedtile:
                if ((self.tiles[2][2]).Print()) == markedtile:
                    print("Winner is ", markedtile)
                    return True
        return False