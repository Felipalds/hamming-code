import math


def hamming_encode(file_binary_string, parity_amount):
    original_string = list(file_binary_string)
    original_string_len_position = math.ceil(math.log2(len(original_string)))
    original_string.reverse()
    original_dictionary = {}
    xors = []

    for i in range(parity_amount):
        for char_string_position in range(len(original_string)):
            position_in_binary = str(bin(char_string_position))[2:].rjust(original_string_len_position + 1, '0')
            original_dictionary[position_in_binary] = original_string[char_string_position]
    print(original_dictionary)
    
    for i in range(parity_amount):
        position = i
        print(position)
        xor = 0

        keys = original_dictionary.keys()
        for key in keys:
            str_key = list(key)
            str_key.reverse()
            print(position, " => ", str_key, " => ", original_dictionary[key])
            if(str_key[position] == '1'):
                if(original_dictionary[key]) == '1':
                    xor += 1
        print("xor = ", xor)
        xors.append(xor)

    original_string.reverse()
    for i in range(len(xors)):
        position = 2 ** i
        toBeInserted = 0
        if(xors[i] % 2 != 0):
            toBeInserted = 1
        original_string.insert(position, str(toBeInserted))

    original_string.reverse()
    print(original_string)

    sum = 0
    for char in original_string:
        sum += int(char)
    
    if(sum % 2 == 0):
        original_string.insert(len(original_string) + 1, '0')
    else:
        original_string.insert(len(original_string) + 1, '1')
        
    print("xors = ", xors)
    print(original_string)
    print(original_dictionary)

    char_string = ""
    f = open("zoz_nice_dick.wham", "wb")
    for char in original_string:
        char_string += char

    print(char_string)

    char1=int(char_string[0:8], 2)
    char2=int(char_string[8:16], 2)

    bin1 = bin(char1)
    bin2 = bin(char2)

    print(bin1, bin2)
    print(char1, char2)

    char_list = bytearray([char1, char2])
    print(char_list)

    f.write(char_list)