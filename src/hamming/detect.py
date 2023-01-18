def hamming_detect(binary_string : str):
    parity_bits = []
    general_parity_bit = binary_string[0]
    for i, bit in enumerate(binary_string):
        if (i & (i - 1)) == 0 and i != 0:
            parity_bits.append((f"{bit}",[],))
    for i in range(len(parity_bits)):
        for j, bit in enumerate(binary_string):
            binary_position = bin(j).rjust(8, '0')
            if binary_position[-i] == '1':
                parity_bits[i][1].append(bit)
    print(parity_bits)
    
        