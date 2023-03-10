from math import log2, ceil

def bitstring_to_bytes(s):
    b = bytearray()
    for i, c in enumerate(reversed(s)):
        if (i+1) % 8 == 0:
            bo = s[::-1][i-7:i+1][::-1]
            b.insert(0, int(bo, 2))
    return b

def hamming_detect(binary_string : str, file_name : str = "file.txt"):
    file_name = file_name.split('.')[0] + "_recovered." + file_name.split('.')[1]
    error_count = 0
    print(f"CADEIA BINÁRIA:\n{binary_string[:100]}\n")
    binary_string = binary_string[::-1]
    parity_bits = []
    general_parity_bit = binary_string[0]
    for i, bit in enumerate(binary_string):
        if (i & (i - 1)) == 0 and i != 0:
            parity_bits.append((f"{bit}",[],))
    for i in range(len(parity_bits)):
        for j, bit in enumerate(binary_string):
            binary_position = bin(j)[2:].rjust(i+1, '0')
            if binary_position[-(i+1)] == '1':
                parity_bits[i][1].append(j)
    visual_parity_bits = parity_bits.copy()
    for e, i in enumerate(visual_parity_bits):
        visual_parity_bits[e] = list(i)
    for e, i in enumerate(visual_parity_bits):
        visual_parity_bits[e][1] = [binary_string[b] for b in i[1]]
    #print("BIT DE PARIDADE // BITS REPRESENTADO")
    #for i in visual_parity_bits:
       #print(i)
    #print('\n', end='')
    error_indexes = set({})
    clean_indexes = set({})
    error_index = None
    general_parity = False
    one_count = 0
    for i in binary_string:
        if i == '1':
            one_count += 1
    if one_count % 2 == 0:
        general_parity = True
    for i in parity_bits:
        parity_bit = i[0]
        represented_bits = i[1]
        one_count = 0
        for represented_index in represented_bits:
            if int(binary_string[represented_index]):
                one_count += 1
        if one_count % 2 != 0 and error_count == 0:
            error_count += 1
            if general_parity:
                break
            error_indexes.update(represented_bits)
        elif one_count % 2 != 0 and error_count:
            error_indexes.intersection_update(represented_bits)
        elif one_count % 2 == 0:
            clean_indexes.update(represented_bits)
        # if len(error_indexes) > 0: print(f"ERROR INDEXES: {error_indexes}")
    #print(f"CLEAN INDEXES: {clean_indexes}")
    error_indexes.difference_update(clean_indexes)
    # if len(error_indexes) > 0: print(f"ERROR INDEXES: {error_indexes}")
    if general_parity and error_count:
        error_count = 2
    syndrom_word = []
    for i in parity_bits:
        syndrom_word.append(i[0])
    syndrom_word.reverse()
    # print(f"SYNDROME WORD: {syndrom_word}")
    print(f"Erros achados: {error_count}")
    for ia in error_indexes:
        error_index = ia
    if error_count == 1:
        print(f"Posição (SEC): {error_index}\nBit: {binary_string[error_index]}")
        print("Recuperando arquivo e salvando...")
        recover_bit = '1'
        print(binary_string)
        if binary_string[error_index] == '1':
            recover_bit = '0'
        binary_string = binary_string[:error_index] + recover_bit + binary_string[error_index+1:]
        print(binary_string)
        print(bitstring_to_bytes(binary_string).hex())
        my_file = open(file_name.replace("_recovered", ''), "wb")
        my_file.write(bitstring_to_bytes(binary_string))
        my_file.close()
        ans = None
        while ans != 'n':
            print("Decodificar? [y/n]")
            ans = input(">")
            if ans == 'y':
                for ia, i in enumerate(binary_string):
                    if (ia & (ia - 1)) == 0 and ia != 0:
                        binary_string = binary_string[:ia] + 'P' + binary_string[ia+1:]
                binary_string = 'P' + binary_string[1:]
                binary_string = binary_string.replace('P', '')
                my_file = open(file_name, "wb")
                my_file.write(bitstring_to_bytes(binary_string))
                my_file.close()
                break
    elif error_count == 2:
        print("Posição não pode ser identificada (DED).")
    elif not general_parity:
        print(f"Posição (SEC): 0\nBit: {binary_string[0]}")
        print("Recuperando arquivo e salvando...")
        recover_bit = '1'
        if binary_string[0] == '1':
            recover_bit = '0'
        binary_string = recover_bit + binary_string[1:]
        for ia, i in enumerate(binary_string):
            if (ia & (ia - 1)) == 0 and ia != 0:
                binary_string = binary_string[:ia] + binary_string[ia+1:]
        my_file = open(file_name.replace("_recovered", ''), "wb")
        my_file.write(bitstring_to_bytes(binary_string))
        my_file.close()
        ans = None
        while ans != 'n':
            print("Decodificar? [y/n]")
            ans = input(">")
            if ans == 'y':
                for ia, i in enumerate(binary_string):
                    if (ia & (ia - 1)) == 0 and ia != 0:
                        binary_string = binary_string[:ia] + 'P' + binary_string[ia+1:]
                binary_string = 'P' + binary_string[1:]
                binary_string = binary_string.replace('P', '')
                my_file = open(file_name, "wb")
                my_file.write(bitstring_to_bytes(binary_string))
                my_file.close()
                break
    else: 
        print("Código limpo em termos de hamming.")
        
        ans = None
        while ans != 'n':
            print("Decodificar? [y/n]")
            ans = input(">")
            if ans == 'y':
                for ia, i in enumerate(binary_string):
                    if (ia & (ia - 1)) == 0 and ia != 0:
                        binary_string = binary_string[:ia] + 'P' + binary_string[ia+1:]
                binary_string = 'P' + binary_string[1:]
                binary_string = binary_string.replace('P', '')
                my_file = open(file_name, "wb")
                my_file.write(bitstring_to_bytes(binary_string))
                my_file.close()
                break

