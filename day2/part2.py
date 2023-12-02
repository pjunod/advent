#!/usr/bin/env python3

from functools import reduce


resdict = {}

with open("data", 'r', encoding='utf8') as f:
    data = f.readlines()
# dict is {"gamenum": {color: colornum, color1: colornum1}}
for line in data:
    line = line.strip()
    game, plays = line.split(':')
    gamenum = game.split()[1]
    resdict[gamenum] = {}
    for play in plays.split(';'):
        for turn in play.split(','):
            colornum, color = turn.split()
            colornum = int(colornum)
            resdict[gamenum][color] = max(resdict[gamenum].get(color, 0), colornum)

ans = 0

for gamenum, gameres in resdict.items():
    reslist = list(gameres.values())
    print(reslist)
    ans += reduce((lambda x, y: x * y), reslist)

print(ans)