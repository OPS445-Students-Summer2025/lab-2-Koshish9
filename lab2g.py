#!/usr/bin/env python3
# Author: Koshish Adhikari
# Author ID: kadhikari9
# Date Created: 2025/05/26

import sys

if len(sys.argv) == 2:
    timer = int(sys.argv[1])
else:
    timer = 3

while timer != 0:
    print(timer)
    timer -= 1
print("blast off!")
