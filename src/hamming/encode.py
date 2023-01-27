import math

def hamming_encode(file_binary_string, parity_amount):
    parity_amount += 1
    print(len(file_binary_string))
    original_string = file_binary_string[::-1]
    xors = []
    spaced_string = insertSpaceBits(original_string, parity_amount)
    xors = getParityBits(spaced_string, parity_amount)
    xors.reverse()
    inserted_string = insertParityBits(xors, spaced_string)
    last_bit_string = insertLastParityBit(inserted_string)
    #print(last_bit_string)
    insertInFile(last_bit_string, parity_amount)


            

def getParityBits(spaced_string, parity_amount):
    xors = []
    for i in range(parity_amount - 1):
        print(i)
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
    #print(original_string)
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


def insertInFile(last_bit_string, parity_amount):
    x = last_bit_string[::-1]
    last_bit = x.rjust(2**parity_amount, "0")
    v = int(last_bit, 2)
    b = bytearray()
    f = open("output.wham", "wb")
    while v:
        #print(bin(v))
        #print(bin(v & 0xff))
        b.append(v & 0xff)
        v >>= 8
    f.write(b)
