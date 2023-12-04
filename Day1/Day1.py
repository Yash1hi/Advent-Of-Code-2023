# Advent of Code Day 1 - Yash Thapliyal

def challenge1():
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
    return total

########################################################################
########################################################################
########################################################################

#
def challenge2():
    input = open("input.txt", "r", encoding="utf-8").readlines()
    total = 0
    for line in input:
        firstNum, lastNum = getFirstLast(line)        
        total += int(str(firstNum) + str(lastNum))
    return total

def getFirstLast(line):
    for j in range(len(line)):
        isNum, value = isANum(line, j)
        if isNum:
            firstNum = value
            break
    for j in range(len(line)-1, -1, -1):
        isNum, value = isANum(line, j)
        if isNum:
            lastNum = value
            break
    return firstNum, lastNum
def isANum(line, index):
    '''
    str line - Line of input file
    int index - Index of the line that we would like to check for digit
    '''

    # List of digits as strings and their mapping to ints
    digitsAsWords = ["one","two","three","four","five","six","seven","eight","nine"]
    digMap = {"one" : 1,
              "two" : 2,
              "three" : 3,
              "four" : 4,
              "five" : 5,
              "six" : 6, 
              "seven" : 7,
              "eight" : 8,
              "nine" : 9}
    
    # Instant return if digit
    if line[index].isdigit():
        return True, int(line[index])
    
    for word in digitsAsWords:
        if recurWord(word, line[index:]):
            return True, digMap[word]
    return False, -1
          
def recurWord(word, line):
    '''
    str word - string of number to check against
    str line - line beginning with the index to check
    '''
    if word == "":
        return True
    elif line == "" or word[0] != line[0]:
        return False
    elif line[0] == word[0]:
        return recurWord(word[1:], line[1:])

print("Challenge 1 Answer:", challenge1())
print("Challenge 2 Answer:", challenge2())