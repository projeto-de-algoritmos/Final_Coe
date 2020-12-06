from lib.node import Node
from lib.priority_queue import PriorityQueue
from collections import Counter
from bitstring import BitArray
from typing import List, TextIO
from lib.utils import Utils

class Encode:

    def get_node_tree(self, frequencies: List['Node']) -> 'Node':
        priority_queue = PriorityQueue(frequencies)

        while True:
            left_node = priority_queue.get_and_remove_first_element()
            right_node = priority_queue.get_and_remove_first_element()

            parent = Node(left=left_node, right=right_node)

            if (len(priority_queue) == 0):
                return parent
            
            priority_queue.add(parent)
    
    def get_frequencies(self, file_content: str) -> List['Nodes']:
        return [Node(count = count, symbol = elem) for elem, count in Counter(file_content).most_common()]

    def encode_text(self, text: str, encode_table: dict) -> str:
        encoded_text = ""
        for char in text:
            encoded_text += encode_table[char]
        
        return encoded_text

    # Faz a criação da árvore In-place. Logo não tem retorno
    def encode_headers(self, node: 'Node', bitarray: 'BitArray', char_size: int) -> None:
        if node.isLeaf():
            bitarray.append('0b1')

            encoded_char = Utils.encode_char(node.symbol)
            encoded_char = "".join("0" for n in range(char_size - len(encoded_char))) + encoded_char
            bitarray.append(f"0b{encoded_char}")
        else:
            bitarray.append('0b0')
            self.encode_headers(node.left, bitarray, char_size)
            self.encode_headers(node.right, bitarray, char_size) 