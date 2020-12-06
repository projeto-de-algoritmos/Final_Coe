from collections import Counter
from lib.node import Node
from lib.priority_queue import PriorityQueue
from bitstring import Bits, BitStream, BitArray
from lib.encode import Encode
from lib.decode import Decode
from lib.file import File
from lib.utils import Utils

encode_util = Encode()
decode_util = Decode()

file = File.open_file('examples/text_3.txt', 'r', encoding='UTF-8')

file_content = ''.join(file)
binary_file_content = BitStream(Bits(file))
frequencies = encode_util.get_frequencies(file_content)


parent = encode_util.get_node_tree(frequencies)

print("Sort finalizado")
print(parent)

hash_table = {}
parent.generate_hashT(hash_table, "")
x = binary_file_content.read(8)
print(hash_table)

encoded_text = encode_util.encode_text(file_content, hash_table)
inv_map = {v: k for k, v in hash_table.items()}
decoded_text = decode_util.decode_text(encoded_text, inv_map)

char_size = Utils.get_largest_char_size(hash_table)

encoded_header = BitArray()

encoded_header = Utils.save_char_size_bits(encoded_header, char_size)

encode_util.encode_headers(parent, encoded_header, char_size)

decoded_header = decode_util.decode_headers(BitStream(encoded_header), char_size)


bits = encoded_header.bin + encoded_text
fileEnc = BitArray('0b' + bits)


File.save_file("compressed_files/test.eliaserick", file_content=fileEnc.tobytes())

decCont = BitArray()


"""
DECODE
"""
content = File.open_file("compressed_files/test.eliaserick", "rb")

for line in content:
    decCont.append(line)


x = BitStream(decCont)
char_size = Utils.get_encoded_file_char_size(x)
decoded_header_2 = decode_util.decode_headers(x, char_size)

hash_table = {}
decoded_header_2.generate_hashT(hash_table, "")
inv_map = {v: k for k, v in hash_table.items()}
decoded_text = decode_util.decode_text(decCont.bin[x.bitpos:x.len], inv_map)

print(decoded_text)

