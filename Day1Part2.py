import sys;
puzzleInput = raw_input("Input: ")
print("input is " + puzzleInput)
length = len(puzzleInput)
endIterator = length - 1
isFirst = True
firstNum = puzzleInput[0]
previousNum = -1
sum = 0
print("test first num =" +firstNum)

def getHalfwayAround(i):
    input_length = len(puzzleInput)
    half = input_length/2
    next = i + half
    if next > input_length-1:
        next -= input_length
    return next

for i, c in enumerate(puzzleInput):
    next = getHalfwayAround(i)
    first = int(c)
    second = int(puzzleInput[next])
    if first == second:
        sum += first

print(sum)