from sys import maxint
with open('C:\Users\MICK\Desktop\Day2Test.txt') as text:
    checksum = 0
    for x in text:
        allNums = x.replace(" ","")
        allNums = allNums.replace("\n","")
        row = allNums.split("\t")
        smallest = maxint
        largest = -maxint
        for n in row:
            num = int(n)
            if num < smallest:
                smallest = num
            if num > largest:
                largest = num
        checksum += largest - smallest
print(checksum)