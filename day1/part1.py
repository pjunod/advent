#!/usr/bin/env python3

with open("data", 'r', encoding='utf8') as f:
    mydata = f.readlines()
runtotal = 0
for line in mydata:
    start = 0
    end = len(line) - 1

    while start < end:
        if not line[start].isdigit():
            start += 1
        elif not line[end].isdigit():
            end -= 1
        else:
            break
    newnum = int(line[start]+line[end])
    runtotal += newnum

print(f"Total is {runtotal}")
