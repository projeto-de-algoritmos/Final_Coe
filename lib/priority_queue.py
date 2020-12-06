from typing import List
from lib.node import Node

class PriorityQueue:
    def __init__(self, lst: List['Node']):
        self.lst = [*lst]
        self.__sort_by_count()

    def add(self, item):
        self.lst.append(item)
        self.__sort_by_count()

    def get_and_remove_first_element(self) -> 'Node':
        return self.lst.pop(0)

    def __sort_by_count(self,) -> List['Nodes']:
        return self.lst.sort(key = lambda item: item.count)

    def __len__(self):
        return len(self.lst)
