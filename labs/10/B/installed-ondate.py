#!/usr/bin/env python3

import re
import sys

def main():
    if len(sys.argv) < 2:
        sys.exit(0)

    inp = sys.argv[1]

    pattern = re.compile(r"(\d\d\d\d-\d\d-\d\d)( .+) installed (.+):(.*)")

    for line in sys.stdin:
        line = line.rstrip()

        m = pattern.search(line)
        if m:
            a = str(m.group(1))
            b = str(m.group(3))
            if a == inp:
                print("%s: %s" % (a,b))

if __name__ == "__main__":
    main()
