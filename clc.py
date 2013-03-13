#!/usr/bin/env python

import sys

def main():
    cl = " ".join(sys.argv[1:])
    print ">", eval(cl)

if __name__ == '__main__':
    main()
