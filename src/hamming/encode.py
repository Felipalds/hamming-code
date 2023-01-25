import math

def hamming_encode(file_binary_string, parity_amount):
    print(file_binary_string)
    parity_amount += 1
    original_string = file_binary_string[::-1]
    xors = []
    spaced_string = insertSpaceBits(original_string, parity_amount)
    print(spaced_string)
    print(len(spaced_string))
    xors = getParityBits(spaced_string, parity_amount)
    xors.reverse()
    inserted_string = insertParityBits(xors, spaced_string)
    print(inserted_string)
    insertLastParityBit(inserted_string)
    #insertInFile(original_string)

def getParityBits(spaced_string, parity_amount):
    xors = []
    print(parity_amount)
    for i in range(parity_amount - 1):
        xor = 0
        position = 2**i
        for j, char in enumerate(spaced_string):
            bin_char = bin(j)[2:].rjust(parity_amount - 1, '0')
            for pk, k in enumerate(bin_char):
                if(pk == i and k == '1' and char == '1'):
                    xor += 1

        if(xor % 2 == 0):
            xors.append(0)
        else:
            xors.append(1)

        print(xors)

    return xors

def insertParityBits(xors, spaced_string):
    print(spaced_string)
    inserted_string = spaced_string[0]
    k = 0
    for n, c in enumerate(spaced_string):
        if(n!=0):
            if(c == "P"):
                inserted_string += str(xors[k])
                k += 1
            else:
                inserted_string += c

    return inserted_string

def insertSpaceBits(original_string, parity_amount):
    original_string = "P" + original_string
    for i in range(parity_amount - 1):
        position = 2 ** i
        original_string = original_string[0:position] + "P" + original_string[position:]
        if(original_string[len(original_string) - 1]) == "P":
            original_string = original_string[0:len(original_string)-2]
    return original_string


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