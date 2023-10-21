#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
    months = {
        1: 'January', 2: 'February', 3: 'March',
        4: 'April', 5: 'May', 6: 'June',
        7: 'July', 8: 'August', 9: 'September',
        10: 'October', 11: 'November', 12: 'December'
    }
    m = int(input('Enter number from 1 to 12: '))
    if m < 0 or m > 12:
        print('Invalid Input!', file=sys.stderr)
    else:
        print(f'{m} is {months[m]}')