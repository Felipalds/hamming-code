import math

def hamming_encode(file_binary_string, parity_amount):
    parity_amount += 1
    original_string = list(file_binary_string)
    original_string.reverse()
    xors = []

    insertSpaceBits(original_string, parity_amount)
    original_dictionary = generateDictionaryByBitString(original_string, parity_amount)
    xors = getParityBits(original_dictionary, parity_amount)
    insertParityBits(xors, original_string)
    insertLastParityBit(original_string)
    insertInFile(original_string)

def generateDictionaryByBitString(original_string, parity_amount):
        
        original_string_len_position = math.ceil(math.log2(len(original_string))) - 1
        original_dictionary = {}
        for i in range(parity_amount - 1):
            for char_string_position in range(len(original_string)):
                position_in_binary = str(bin(char_string_position))[2:].rjust(original_string_len_position + 1, '0')
                original_dictionary[position_in_binary] = original_string[char_string_position]
        return original_dictionary

def getParityBits(original_dictionary, parity_amount):
    xors = []
    for i in range(parity_amount - 1):
        position = i
        xor = 0
        keys = original_dictionary.keys()
        for key in keys:
            str_key = list(key)
            str_key.reverse()
            if(str_key[position] == '1'):
                if(original_dictionary[key]) == '1':
                    xor += 1
        xors.append(xor)
    return xors

def insertParityBits(xors, original_string):
    for i in range(len(xors)):
        position = 2 ** i
        toBeInserted = 0
        if(xors[i] % 2 != 0):
            toBeInserted = 1
        original_string[position] = str(toBeInserted)

    original_string.reverse()
    original_string.pop()

def insertSpaceBits(original_string, parity_amount):
    original_string.insert(0, "P")
    for i in range(parity_amount - 1):
        position = 2 ** i
        original_string.insert(position, "P")

def insertLastParityBit(original_string):
    original_string.reverse()
    xor = 0
    for c in original_string:
        if c == '1':
            xor += 1

    if xor % 2 == 0:
        original_string[0] = '0'
    else:
        original_string[0] = '1'

    original_string.reverse()


def insertInFile(original_string):
    char_string = ""
    f = open("zoz_nice_dick.wham", "wb")
    for char in original_string:
        char_string += char
    print("CHAR STRING: ", char_string)

    char1=int(char_string[0:8], 2)
    char2=int(char_string[8:16], 2)

    bin1 = bin(char1)
    bin2 = bin(char2)

    print(bin1, bin2)
    print(char1, char2)

    char_list = bytearray([char1, char2])
    print(char_list)

    f.write(char_list)