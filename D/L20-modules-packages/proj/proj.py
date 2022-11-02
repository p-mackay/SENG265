#!/usr/bin/env python3
from pack1 import mod1
from pack2 import mod2
from pack3 import mod3
from pack2.pack2a import mod2a
from pack2.pack2b import mod2b

def main():
    print("in proj.py -- main program")

    mod1.m1print()
    mod2.m2print()
    mod3.m3print()

    mod2a.m2aprint()
    mod2b.m2bprint()



if __name__ == "__main__":
    main()
