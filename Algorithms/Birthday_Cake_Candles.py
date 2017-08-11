



#!/bin/python3

import sys

input()     # Value not needed
candles = list(map(int, input().strip().split(' ')))

tallest = max(candles)
return candles.count(tallest);
        
