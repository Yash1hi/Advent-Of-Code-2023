def challenge1():
    f = open("input.txt", "r", encoding="utf-8").readlines()
    total = 0
    for line in f:
        isPos, id = lineRead(line)
        if isPos:
            total += id
    return total

def lineRead(line):
    colonIndex = line.find(":")
    roundArr = line[colonIndex+1:].split(";")
    roundArr[-1] = roundArr[-1][:-1]
    for round in roundArr:
        if not isRoundPos(round):
            return False, -1
    
    return True, int(line[5:colonIndex])

def isRoundPos(round):
    colorArr = round.split(",")
    for color in colorArr:
        color = color.strip().split(" ")
        if color[1] == "red" and int(color[0]) > 12:
            return False
        elif color[1] == "green" and int(color[0]) > 13:
            return False
        elif color[1] == "blue" and int(color[0]) > 14:
            return False
    return True

########################################################################
########################################################################
########################################################################

def challenge2():
    f = open("input.txt", "r", encoding="utf-8").readlines()
    total = 0
    for line in f:
        total += linePower(line)
    return total

def linePower(line):
    colonIndex = line.find(":")
    roundArr = line[colonIndex+1:].split(";")
    roundArr[-1] = roundArr[-1][:-1]
    colors = [-1, -1, -1]
    for round in roundArr:
        currColorCount = getCount(round)
        if currColorCount[0] > colors[0]:
            colors[0] = currColorCount[0]
        if currColorCount[1] > colors[1]:
            colors[1] = currColorCount[1]
        if currColorCount[2] > colors[2]:
            colors[2] = currColorCount[2]
    return colors[0]*colors[1]*colors[2]

def getCount(round):
    colorArr = round.split(",")
    colors = [-1, -1, -1]
    for color in colorArr:
        color = color.strip().split(" ")
        if color[1] == "red":
            colors[0] = int(color[0])
        elif color[1] == "green":
            colors[1] = int(color[0])
        elif color[1] == "blue":
            colors[2] = int(color[0])
    return colors

print("Challenge 1 Answer:", challenge1())
print("Challenge 2 Answer:", challenge2())