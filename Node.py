from Board import Board


class Node:
    def __init__(self, PuzzBoard, ParentNode = None, depth = None):
        self.Board = PuzzBoard
        self.depth = depth
        self.ParentNode = ParentNode
        if self.ParentNode is None:
            self.depth = 0
        else:
            self.depth = self.ParentNode.depth+1


    def get_next_node(self):
         return self.next_node

    def get_Board(self):
        return self.Board