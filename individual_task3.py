#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    result = []
    for i in range(10, 100):
        num_sum = sum([int(n) for n in str(i)])
        if i % num_sum == 0:
            result.append(i)
    print(result)