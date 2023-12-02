#!/usr/bin/env python3

import pprint

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
    
#pprint.pprint(resdict)


checkdict = {}
ans = []

for gamenum, gameres in resdict.items():
    if gameres["red"] <= 12 and gameres["green"] <= 13 and gameres["blue"] <= 14:
        ans.append(int(gamenum))

print(ans)
print(sum(ans))
