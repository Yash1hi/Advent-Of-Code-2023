#!/usr/bin/env python3
def main():
    input = open("input.txt", "r", encoding="utf-8").readlines()
    total = 0
    for i in input:
        firstNum = -1
        lastNum = -1
        for j in range(len(i)):
            if i[j].isdigit():
                firstNum = i[j]
                break
        for j in range(len(i)-1, -1, -1):
            if i[j].isdigit():
                lastNum = i[j]
                break
        total += int(str(firstNum) + str(lastNum))
    print(total)

main()