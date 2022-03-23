from encodedecode import encode_text
from encodedecode import decode_text



def error_detection(data):
    output = []
    for byte in data:
        res = 0
        for i in range(4):
            val = 0
            for j in range(1, 12 + 1):
                if j & (2 ** i) == (2 ** i):
                    val = val ^ byte[-1 * j]
            res = res + val*(10**i)
        output.append(int(str(res), 2))
    return output





def error_correction(data, errors):
    for i in range(len(errors)):
        if errors[i] == 0:
            print("there is no error for this byte")
        else:
            errors[i] = 12 - errors[i]
            print("error is at location " + str(errors[i]))
            if data[i][errors[i]] == 0:
                data[i][errors[i]] = 1
            else:
                data[i][errors[i]] = 0
    return data


