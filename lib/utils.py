from bitstring import BitArray, BitStream


class Utils:
    @staticmethod
    def encode_char(symbol: str) -> str:
        return ''.join(format(ord(i), 'b') for i in symbol)

    @staticmethod
    def get_largest_char_size(hash_table: dict) -> int:
        bigger_char_size = 0
        for char in list(hash_table.keys()):
            char_size = len(Utils.encode_char(char))
            if  char_size > bigger_char_size:
                bigger_char_size = char_size

        return bigger_char_size

    @staticmethod
    def get_encoded_file_char_size(bitStream: 'BitStream') -> int:
        return int(bitStream.read(5).bin, 2)

    @staticmethod
    def save_char_size_bits(bitArray: 'BitArray', char_size: int) -> 'BitArray':
        bitArray.append((char_size).to_bytes(2, byteorder='big'))
        return bitArray[-5:]
