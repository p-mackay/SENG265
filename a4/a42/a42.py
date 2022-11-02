#!/usr/bin/env python3
'''Assignment 4 Part 1 template'''
print(__doc__)

from typing import IO
import random
import pandas as pd
import constants as c

class GenRandom:
    def __init__(self, mn: int, mx: int):
        self.mn: int = mn
        self.mx: int = mx

    def randInt(self):
        return random.randrange(self.mn, self.mx)

def main():
    data = []
    list_data = []
    for num in range(10):
        data.append(GenRandom(0, 2).randInt())
        data.append(GenRandom(c.XMIN, c.XMAX).randInt())
        data.append(GenRandom(c.YMIN, c.YMAX).randInt())
        data.append(GenRandom(c.RADMIN, c.RADMAX).randInt())
        data.append(GenRandom(c.RXMIN, c.RXMAX).randInt())
        data.append(GenRandom(c.RYMIN, c.RYMAX).randInt())
        data.append(GenRandom(c.WIDMIN, c.WIDMAX).randInt())
        data.append(GenRandom(c.HETMIN, c.HETMAX).randInt())
        data.append(GenRandom(c.REDMIN, c.REDMAX).randInt())
        data.append(GenRandom(c.GREENMIN, c.GREENMAX).randInt())
        data.append(GenRandom(c.BLUEMIN, c.BLUEMAX).randInt())
        data.append(round(random.uniform(c.OPMIN, c.OPMAX), 1))
        list_data.append(data)
        data = []
    df = pd.DataFrame(list_data, columns=['SHA', 'X', 'Y', 'RAD', 'RX', 'RY',\
            'W', 'H', 'R', 'G', 'B', 'OP'])
    print(df)

main()
