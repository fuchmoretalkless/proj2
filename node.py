class Node:
    children = []
    board = [][]
    humanOrNah = False
    depthcount = 0
    hVal = 0
    aVal = 0;
    bVal = 0;

    def __init__(self,b,d,humanBool):
        self.board = b
        self.depthcount = d
        self.humanOrNah = humanBool
    
