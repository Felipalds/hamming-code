import math

def hamming_encode(file_binary_string, parity_amount):
    parity_amount += 1
    original_string = file_binary_string[::-1]
    xors = []
    spaced_string = insertSpaceBits(original_string, parity_amount)
    xors = getParityBits(spaced_string, parity_amount)
    xors.reverse()
    inserted_string = insertParityBits(xors, spaced_string)
    last_bit_string = insertLastParityBit(inserted_string)
    print(last_bit_string)
    #insertInFile(last_bit_string)

def getParityBits(spaced_string, parity_amount):
    xors = []
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


    return xors

def insertParityBits(xors, spaced_string):
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

def insertLastParityBit(inserted_string):
    xor = 0
    last_bit_string = ""
    for c in inserted_string:
        if c == '1':
            xor += 1

    if xor % 2 == 0:
        last_bit_string = "0" + inserted_string[1:]
    else:
        last_bit_string = "1" + inserted_string[1:]
    return last_bit_string


def insertInFile(last_bit_string):
    char_string = ""
    f = open("z.wham", "wb")
    for char in last_bit_string:
        char_string += char

    char1=int(char_string[0:8], 2)
    char2=int(char_string[8:16], 2)

    bin1 = bin(char1)
    bin2 = bin(char2)


    char_list = bytearray([char1, char2])

    f.write(char_list)