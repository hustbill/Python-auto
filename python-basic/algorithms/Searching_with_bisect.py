'''
P44 Fluent Python
DEMO: bisect_right
haystack -> 1 4 5 8 12 15 20 21 23 23 26 29 30
31 @ 13        |  |  |  |  |  |  |  |  |  |  |  |  |31
30 @ 13        |  |  |  |  |  |  |  |  |  |  |  |  |30
29 @ 12        |  |  |  |  |  |  |  |  |  |  |  |29
23 @ 10        |  |  |  |  |  |  |  |  |  |23
22 @  8        |  |  |  |  |  |  |  |22
10 @  4        |  |  |  |10
 8 @  4        |  |  |  |8
 5 @  3        |  |  |5
 2 @  1        |2
 1 @  1        |1
 0 @  0      0
'''

import bisect
import sys

HAYSTACK = [1, 4, 5, 8, 12, 15, 20, 21, 23, 23, 26, 29 ,30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

ROW_FMT = '{0:2d} @ {1:2d}      {2}{0:<2d}'

def demo(bisect_fn):
    for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK, needle)
        offset = position * '  |'
        print(ROW_FMT.format(needle, position, offset))

if __name__ == '__main__':
    if sys.argv[-1] == 'left':
        bisect_fn = bisect.bisect_left
    else:
        bisect_fn = bisect.bisect

    print('DEMO:', bisect_fn.__name__)
    print('haystack ->', ' '.join('%d'  %n for n in HAYSTACK))
    demo(bisect_fn)
