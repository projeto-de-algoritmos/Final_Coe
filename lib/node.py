from typing import Tuple, Dict

class Node:

    def __init__(self, left: 'Node' = None, right: 'Node' = None, symbol: str = None, count: int = 0):
        self.symbol = symbol or "+"
        self.left = left
        self.right = right
        self.count = count or self.getCount()

    def isLeaf(self) -> bool:
        return self.left == None and self.right == None

    def getCount(self) -> int:
        if (self.isLeaf()):
            return self.count
        return self.left.getCount() + self.right.getCount()

    def generate_hashT(self, table: Dict, key: str):
        if(self.isLeaf()):
            table.update({self.symbol :key})
            return

        self.left.generate_hashT(table, key + "0")
        self.right.generate_hashT(table, key + "1")
    
