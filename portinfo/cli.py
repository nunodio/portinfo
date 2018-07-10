#!/usr/bin/env python3
import sys
from portinfo import search


def usage():
    print("Usage: {0} [ port | service name ]".format(sys.argv[0]))


def main():
    if len(sys.argv) < 2:
        usage()
    else:
        search(sys.argv[1])


if __name__ == "__main__":
    main()
