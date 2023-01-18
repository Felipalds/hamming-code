def hamming_encode(file_binary_string, parity_amount):
    encoded_string = list(file_binary_string)

    encoded_string.insert(0, "a")

    for i in range(parity_amount):
        index = 2**(i)
        
        encoded_string.insert(index, "a")

        parity_amount -= 1

    print(encoded_string)
