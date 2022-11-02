#!/usr/bin/env python3

import re
import sys

def main():
    if len(sys.argv) < 2:
        sys.exit(0)

    date_from = sys.argv[1]
    date_to   = sys.argv[2] 

    # TODO: Complete your code here as described at the end of video # 2 for Lab 10.

    
    pattern = re.compile(r"(\d\d\d\d-\d\d-\d\d)( .+) installed (.+):(.*)")

    for line in sys.stdin:
        line = line.rstrip()

        m = pattern.search(line)
        if m:
            a = str(m.group(1))
            b = str(m.group(3))
            if date_from <= a <= date_to:
                print("%s: %s" % (a,b))


if __name__ == "__main__":
    main()
