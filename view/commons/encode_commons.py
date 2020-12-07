from bitstring import BitStream, Bits, BitArray
from lib.utils import Utils
from typing import List
from lib.encode import Encode

class EncodeCommons:

    @staticmethod
    def encode_file(file: List[str]) -> 'BitArray':
        encode = Encode()

        file_content = ''.join(file)
        frequencies = encode.get_frequencies(file_content)

        parent = encode.get_node_tree(frequencies)

        hash_table = {}

        parent.generate_hashT(hash_table, "")

        encoded_text = encode.encode_text(file_content, hash_table)

        char_size = Utils.get_largest_char_size(hash_table)

        encoded_header = BitArray()

        encoded_header = Utils.save_char_size_bits(encoded_header, char_size)

        encode.encode_headers(parent, encoded_header, char_size)

        bits = encoded_header.bin + encoded_text
        
        return BitArray('0b' + bits)