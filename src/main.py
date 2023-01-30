from sys import argv
from hamming.detect import hamming_detect
from hamming.encode import hamming_encode
import math

if __name__ == "__main__":
    file_name = argv[1]
    option = argv[2]
    file = open(file_name, "rb")
    string = file.read()
    
    file_binary_string = ''
    
    for char in string:
        byte = bin(char)[2:].rjust(8, '0')
        file_binary_string += byte
    parity_amount = math.ceil(math.log2(len(file_binary_string)) + 1)
    if argv[2] == '-r': # lê arquivo detecta erros
        hamming_detect(file_binary_string, file_name=file_name)
    elif argv[2] == '-w': # recebe arquivo e codifica
        hamming_encode(file_binary_string, parity_amount)