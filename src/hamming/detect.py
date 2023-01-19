from math import log2, ceil

def hamming_detect(binary_string : str):
    error_count = 0
    print(f"CADEIA BINÁRIA:\n{binary_string}\n")
    #for i, ia in enumerate(binary_string):
    #    if i % 4 == 0:
    #        print(' ', end='')
    #    print(ia, end='')
    #print('\n')
    parity_bits = []
    general_parity_bit = binary_string[0]
    for i, bit in enumerate(binary_string):
        if (i & (i - 1)) == 0 and i != 0:
            parity_bits.append((f"{bit}",[],))
    for i in range(len(parity_bits)):
        for j, bit in enumerate(binary_string):
            binary_position = bin(j)[2:].rjust(i+1, '0')
            #print("J:", j)
            #print(f"BINARY POSITION: {binary_position}, I: {i}")
            if binary_position[-(i+1)] == '1':
                parity_bits[i][1].append(j)
    visual_parity_bits = parity_bits.copy()
    for e, i in enumerate(visual_parity_bits):
        visual_parity_bits[e] = list(i)
    for e, i in enumerate(visual_parity_bits):
        visual_parity_bits[e][1] = [binary_string[b] for b in i[1]]
    print("BIT DE PARIDADE // BITS REPRESENTADO")
    for i in visual_parity_bits:
        print(i)
    print('\n', end='')
    error_indexes = set({})
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
    if general_parity and error_count:
        error_count = 2
    print(f"Erros achados: {error_count}")
    for ia in error_indexes:
        error_index = ia
    if error_count == 1:
        print(f"Posição (SEC): {error_index}\nBit: {binary_string[error_index]}")
    elif error_count == 2:
        print("Posição não pode ser identificada (DED).")
    else: 
        print("Código limpo em termos de hamming.")