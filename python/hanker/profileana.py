#!/usr/bin/env python3

import sys
import pstats


def main():
    if len(sys.argv) < 2:
        print("Please input the filename")
        exit(0)

    file_name = sys.argv[1].strip()

    p = pstats.Stats(file_name)
    p.strip_dirs().sort_stats('tottime').print_stats()


if __name__ == '__main__':
    main()
