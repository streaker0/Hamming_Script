def encode(c):
    # create 12-bit array to hold encoded hamming code and initalize
    bitsequence = [0] * 12

    # create 8-bit array to hold actual data
    bin = [0] * 8

    ######################## DETERMINE DATA ARRAY #########################
    # convert char to ascii representation
    asciichar = ord(c)

    # Convert ascii to binary (manual technique)
    j = 7

    while asciichar > 0:
        if asciichar % 2 == 1:
            bin[j] = 1
        else:
            bin[j] = 0

        asciichar = asciichar // 2
        j = j - 1


    # Set the data bits
    bitsequence[2] = bin[0]
    bitsequence[4] = bin[1]
    bitsequence[5] = bin[2]
    bitsequence[6] = bin[3]
    bitsequence[8] = bin[4]
    bitsequence[9] = bin[5]
    bitsequence[10] = bin[6]
    bitsequence[11] = bin[7]
    reverse_bin = bin[::-1]
    parity_control = 0
    reverse_control = 0
    for i in range(1, 13):
        if i == 2**parity_control:
            bitsequence[i-1] = 0
            parity_control += 1
        else:
            bitsequence[i-1] = reverse_bin[reverse_control]
            reverse_control += 1
    bitsequence = bitsequence[::-1]


    ######################## CALCULATE THE REMAINING HAMMING SEQUENCE #########################
    # CALCULATE N1
    #+ (int(bitsequence[10]))
    if ((int(bitsequence[11])) + ((int(bitsequence[9])) + (int(bitsequence[7])) + (int(bitsequence[5])) + (int(bitsequence[3])) + (
            int(bitsequence[1]))) % 2 == 1):
        bitsequence[11] = 1
    else:
        bitsequence[11] = 0

    # CALCULATE N2
    if (((int(bitsequence[10])) + (int(bitsequence[9])) + (int(bitsequence[6])) + (int(bitsequence[5])) + (
            int(bitsequence[2])) + (int(bitsequence[1]))) % 2 == 1):
        bitsequence[10] = 1
    else:
        bitsequence[10] = 0

    # CALCULATE N4
    if (((int(bitsequence[8])) + (int(bitsequence[7])) + (int(bitsequence[6])) + (int(bitsequence[5])) + (
            int(bitsequence[0]))) % 2 == 1):
        bitsequence[8] = 1
    else:
        bitsequence[8] = 0

    # CALCULATE N8
    if (((int(bitsequence[4])) + (int(bitsequence[3])) + (int(bitsequence[2])) + (int(bitsequence[1])) + (
            int(bitsequence[0]))) % 2 == 1):
        bitsequence[4] = 1
    else:
        bitsequence[4] = 0

    return bitsequence


######################## DECODER #########################
def decode(bitSequence):
    asciivalue = (((int(bitSequence[0])) * 128) + ((int(bitSequence[1])) * 64) + ((int(bitSequence[2])) * 32) + (
            (int(bitSequence[3])) * 16) + ((int(bitSequence[5])) * 8) + ((int(bitSequence[6])) * 4) + (
                          (int(bitSequence[7])) * 2) + ((int(bitSequence[9])) * 1))
    return asciivalue


def encode_text(word):
    output = []
    for letter in word:
        output.append(encode(letter))
    return output


def decode_text(encoding):
    output = ""
    for byte in encoding:
        output += (chr(decode(byte)))
    return output


######################## MAIN #########################
text = "HELLO WORLD"
#

#
#
# encode('h')
# text = 'E'
full = encode_text(text)

# Full sequence of string above in binary
print(full)

string = decode_text(full)

# Decoded (Just for testing)
print(string)
