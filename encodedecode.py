def encode(c):
    # create 12-bit array to hold encoded hamming code and initalize
    bitsequence=[0]*12

    #create 8-bit array to hold actual data
    bin=[0]*8

    ######################## DETERMINE DATA ARRAY #########################
    # convert char to ascii representation
    asciichar= ord(c)

    # Convert ascii to binary (manual technique)
    j=7

    while(asciichar>0):
        if(asciichar%2 ==1 ):
            bin[j]=1
        else:
            bin[j]=0

        asciichar=asciichar//2
        j=j-1

    # Set the data bits
    bitsequence[2]=bin[0]
    bitsequence[4]=bin[1]
    bitsequence[5]=bin[2]
    bitsequence[6]=bin[3]
    bitsequence[8]=bin[4]
    bitsequence[9]=bin[5]
    bitsequence[10]=bin[6]
    bitsequence[11]=bin[7]

    ######################## CALCULATE THE REMAINING HAMMING SEQUENCE #########################
    #CALCULATE N1
    if (((int(bitsequence[0]))+(int(bitsequence[2]))+(int(bitsequence[4]))+(int(bitsequence[6]))+(int(bitsequence[8]))+(int(bitsequence[10])))%2 == 1):
        bitsequence[0]=1
    else:
        bitsequence[0]=0

    #CALCULATE N2
    if (((int(bitsequence[1]))+(int(bitsequence[2]))+(int(bitsequence[5]))+(int(bitsequence[6]))+(int(bitsequence[9]))+(int(bitsequence[10])))%2 == 1):
        bitsequence[1]=1
    else:
        bitsequence[1]=0

    #CALCULATE N4
    if (((int(bitsequence[3]))+(int(bitsequence[4]))+(int(bitsequence[5]))+(int(bitsequence[6]))+(int(bitsequence[11])))%2 ==1):
        bitsequence[3]=1
    else:
        bitsequence[3]=0

    #CALCULATE N8
    if  (((int(bitsequence[7]))+(int(bitsequence[8]))+(int(bitsequence[9]))+(int(bitsequence[10]))+(int(bitsequence[11])))%2 == 1):
        bitsequence[7]=1
    else:
        bitsequence[7]=0

    return bitsequence

######################## DECODER #########################
def decode(bitSequence) :
    asciivalue = ((( int(bitSequence[2])) * 128)+(( int(bitSequence[4])) * 64)+(( int(bitSequence[5])) * 32)+(( int(bitSequence[6])) * 16)+(( int(bitSequence[8])) * 8)+(( int(bitSequence[9])) * 4)+(( int(bitSequence[10])) * 2)+(( int(bitSequence[11])) * 1))
    return asciivalue


######################## MAIN #########################
text ="HELLOWORLD"

full=[]
for i in text:
    full.append(encode(i))

#Full sequence of string above in binary
print(full)

string=""
for i in full:
    string+=(chr(decode(i)))

#Decoded (Just for testing)
print(string)
