import sys;
input = raw_input("Input: " )
print("input is " + input)
length = len(input)
endIterator = length - 1
isFirst = True
firstNum = input[0]
previousNum = -1
sum = 0
print("test first num =" +firstNum)


for i, c in enumerate(input):
    if i == endIterator:
        if c == firstNum:
            print("firstNum and last are equal")
            sum += int(c)
    if i != 0:
        if int(c) == int(previousNum):
            sum += int(c)
    previousNum = int(c)

print(sum)