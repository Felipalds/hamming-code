import math

def hamming_encode(file_binary_string, parity_amount):
    new_length = math.ceil(math.log2(len(file_binary_string))) + 1
    if math.ceil(math.log2((len(file_binary_string) + new_length))) >= new_length:
        new_length += 1
    while (len(file_binary_string)+new_length) % 8 != 0:
        file_binary_string = '0' + file_binary_string
    parity_amount += 1
    original_string = file_binary_string
    xors = []
    spaced_string = insertSpaceBits(original_string, new_length)
    xors = getParityBits(spaced_string, parity_amount)
    xors.reverse()
    print("Inserindo bits de paridade na cadeia...")
    inserted_string = insertParityBits(xors, spaced_string)
    last_bit_string = insertLastParityBit(inserted_string)
    print("Escrevendo cadeia no arquivo...")
    insertInFile(last_bit_string, parity_amount)


            

def getParityBits(spaced_string, parity_amount):
    print("Achando bits de paridade...")
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

    print("Bits de paridade: ", xors)
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


def insertInFile(last_bit_string, parity_amount):
    x = last_bit_string[::-1]
    b = bytearray()
    for i, c in enumerate(x):
        if (i+1) % 8 == 0:
            bo = x[::-1][i-7:i+1][::-1]
            b.insert(0, int(bo, 2))
    f = open("output.wham", "wb")
    f.write(b)
