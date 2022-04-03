import random


def corruption(data):

    for pos_one in range(0, len(data)):
        pos_two = random.randint(0, 11)

        if(data[pos_one][pos_two] == 0):
            data[pos_one][pos_two] = 1
        else:
            data[pos_one][pos_two] = 0
    return data
