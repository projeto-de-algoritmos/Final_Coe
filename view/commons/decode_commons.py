from typing import List
from bitstring import BitArray, BitStream
from lib.decode import Decode
from lib.utils import Utils

decode = Decode()


class DecodeCommons:

    @staticmethod
    def get_decoded_text(file):
        decCont = BitArray()
        for line in file:
            decCont.append(line)

        x = BitStream(decCont)
        char_size = Utils.get_encoded_file_char_size(x)
        decoded_header_2 = decode.decode_headers(x, char_size)

        hash_table = {}
        decoded_header_2.generate_hashT(hash_table, "")
        inv_map = {v: k for k, v in hash_table.items()}

        return decode.decode_text(decCont.bin[x.bitpos:x.len], inv_map)