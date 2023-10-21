#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


if __name__ == '__main__':
    x, n = float(input('Enter x: ')), int(input('Enter n: '))
    eps = 1e-10
    k, j = 0, 0
    while True:
        jp = j
        j += (((-x**2 / 4) ** k) / (math.factorial(k) * math.factorial(k + n)))
        k += 1
        if math.fabs(j - jp) < eps:
            break

    print(f'J(x) = {((x / 2)**n) * j}')