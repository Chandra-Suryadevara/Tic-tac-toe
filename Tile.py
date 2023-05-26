


class Tile:
     def __init__(self):
         self.Marked = False
         self.Mark=None

     def Mark(self, str):
         if str == 'X' or str == 'O':
             self.Marked = True
             self.Mark = str
             return 1
         else:
             return 0

     def Erase(self):
         self.Mark = None
         self.Marked = False

     def Print(self):
         if self.Marked:
           return self.Mark
         else:
             return 0

     def Check_Mark(self):
         if self.Marked:
             return True
         else:
             return False
