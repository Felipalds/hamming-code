def bitstring_to_bytes(s):
    v = int(s, 2)
    b = bytearray()
    while v:
        print(bin(v))
        print(bin(v & 0xff))
        b.append(v & 0xff)
        v >>= 8
    return b

x = bitstring_to_bytes("010101100101010010101010100001")
print(x)
