import random
import time


def probability(counter, denominator):
    dic = {}
    k = 0
    rul = False
    if counter >= denominator or counter <= 0:
        exit()

    for i in range(denominator):

        for l in range(counter):

            if i in range(counter):
                k = 1
            else:
                k = 0
        dic[i] = k

    ra = random.randint(0, denominator - 1)

    for f in dic:
        if dic.get(ra) == 1:
            return True
        else:
            return False
