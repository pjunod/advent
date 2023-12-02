#!/usr/bin/env python3

import time
import re

# Forgive me, for I am about to sin

s = re.compile('one|two|three|four|five|six|seven|eight|nine|zero', re.IGNORECASE)

numdict = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "zero": "0"
}

with open("data", 'r', encoding='utf8') as f:
    mydata = f.readlines()
runtotal = 0
for line in mydata:
    line = line.strip()
    print(f"whole ass line is [{line}]")
    first = 0
    second = 0
    start = 0
    end = len(line) - 1

    while start < end:
        if not line[start].isdigit():
            wordend = start + 1
            while wordend <= end:
                if line[wordend].isdigit():
                    first = line[wordend]
                    start = end + 1
                    wordend = end + 1
                    break
                if line[start:wordend+1] in numdict:
                    first = numdict[line[start:wordend+1]]
                    start = end + 1
                    wordend = end + 1
                elif s.search(line[start:wordend+1]):
                    first = numdict[s.search(line[start:wordend+1]).group()]
                    start = end + 1
                    wordend = end + 1
                else:
                    wordend += 1

        elif line[start].isdigit():
            first = line[start]
            break 
    print(f"first is {first}")
    start = len(line) - 1
    end = 0 
    while start >= end:
        if not line[start].isdigit():
            wordend = start - 1
            while wordend >= end:
                if line[wordend].isdigit():
                    second = line[wordend]
                    start = end - 1
                    wordend = end - 1
                    break
                if line[wordend:start+1] in numdict:
                    second = numdict[line[wordend:start+1]]
                    start = end - 1
                    wordend = end - 1
                elif s.match(line[wordend:start+1]):
                    second = numdict[s.search(line[wordend:start+1]).group()]
                    start = end - 1
                    wordend = end - 1
                else:
                    wordend -= 1
        elif line[start].isdigit():
            second = line[start]
            break
    print(f"second is {second}")




    fullnum = int(first + second)
    print(f"fullnum is {fullnum}")
    runtotal += fullnum
print(f"runtotal is {runtotal}")
