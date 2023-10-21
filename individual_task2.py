#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from math import sqrt


if __name__ == '__main__':
    a, b, c = [float(num) for num in input('Enter a, b, c: ').split()]
    if a == 0:
        print('Error: a can\'t be null!', file=sys.stderr)
    else:
        discriminant = b**2 - 4*a*c
        if discriminant >= 0:
            x1, x2 = (-b + sqrt(discriminant)) / (2 * a), (-b - sqrt(discriminant)) / (2 * a)
            x3, x4 = sqrt(x1), -1*sqrt(x2)
            print(f'Real roots:\nx1: {x1}\nx2: {x2}\nx3: {x3}\nx4: {x4}')
        else:
            print('No real roots!')