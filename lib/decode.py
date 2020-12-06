from lib.node import Node
from bitstring import BitStream

class Decode:

    def decode_text(self, encoded_text: str, hash_table: dict) -> str:
        decoded_text = ""
        temp_char = ""
        for char in encoded_text:
            temp_char += char

            if decoded_char := hash_table.get(temp_char):
                decoded_text += decoded_char
                temp_char = ""
        
        return decoded_text

    def decode_headers(self, bitStream: 'BitStream', char_size: int):
        if bitStream.read(1).bin == '1':
            encoded_char: str = bitStream.read(char_size).bin
            int_char: int = int(encoded_char,2)
            return Node(symbol=chr(int_char)[0], count=1)
        else:
            left = self.decode_headers(bitStream, char_size)
            right = self.decode_headers(bitStream, char_size)
            return Node(left=left, right=right, count=1)