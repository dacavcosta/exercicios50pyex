#!/usr/bin/env python3
# -*- coding: utf-8 -*-git 

import sys

def convert_f2c(S):
    fahrenheit = float(S)
    celsius = (fahrenheit -32) * 5 / 9
    return celsius

def main():
    if len(sys.argv) == 1:
        print('Utilize : {} temp1, temp2 ...'.format(sys.argv[0]))
        sys.exit(0)

    for arg in sys.argv[1:]:
        try:
            celsius = convert_f2c(arg)
        except ValueError:
            print("{!r} não é um valor numérico".format(arg), file=sys.stderr)
        else:
            print('{}\N{DEGREE SIGN}F = {:g}\N{DEGREE SIGN}C'.format(arg, round(celsius, 0)))

if __name__ == '__main__':
    main()
