#!/usr/bin/env python3
'''Assignment 4 Part 2'''
print(__doc__)

TABNUM = 1
FILENAME: str = "SVGArt.html"
WINART: str = "Python SVG Art"
H1ART: str = "Python SVG Art"
SHCNT: int = 0
CNT: int = 20000 
CIR: int = 1
REC: int = 0
XMIN: int = 0
YMIN: int = 0 
XMAX: int = 1920 
YMAX: int = 1080 

RADMIN: int = 0
RADMAX: int = 1000 
RXMIN: int = XMIN + 10
RXMAX: int = XMAX - 10
RYMIN: int = XMIN + 10
RYMAX: int = XMAX - 10

WIDMIN: int = 0 
WIDMAX: int = 1000
HETMIN: int = 0 
HETMAX: int = 1000

REDMIN: int = 0
REDMAX: int = 255
GREENMIN: int = 0
GREENMAX: int = 255
BLUEMIN: int = 0
BLUEMAX: int = 255
OPMIN: float = 0.0
OPMAX: float = 1.0


from typing import IO
import random
import pandas as pd

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
        data.append(GenRandom(XMIN, XMAX).randInt())
        data.append(GenRandom(YMIN, YMAX).randInt())
        data.append(GenRandom(RADMIN, RADMAX).randInt())
        data.append(GenRandom(RXMIN, RXMAX).randInt())
        data.append(GenRandom(RYMIN, RYMAX).randInt())
        data.append(GenRandom(WIDMIN, WIDMAX).randInt())
        data.append(GenRandom(HETMIN, HETMAX).randInt())
        data.append(GenRandom(REDMIN, REDMAX).randInt())
        data.append(GenRandom(GREENMIN, GREENMAX).randInt())
        data.append(GenRandom(BLUEMIN, BLUEMAX).randInt())
        data.append(round(random.uniform(OPMIN, OPMAX), 1))
        list_data.append(data)
        data = []
    df = pd.DataFrame(list_data, columns=['SHA', 'X', 'Y', 'RAD', 'RX', 'RY',\
            'W', 'H', 'R', 'G', 'B', 'OP'])
    print(df)

main()
