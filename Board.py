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