import math

class SpiralCell:
    def __init__(self, r, c,num):
        self.row = r
        self.col = c
        self.num = num
        self.s = 0
    @staticmethod
    def getCell(previousCell, direction, num, maxDirections):
            row = previousCell.row
            col = previousCell.col

            if direction == 1:
                col += 1
                if maxDirections.maxRightCol < col:
                    maxDirections.maxRightCol +=1
                    maxDirections.lastChange = "maxRightCol"
            if direction == 2:
                row += 1
                if maxDirections.maxUpRow < row:
                    maxDirections.maxUpRow +=1
                    maxDirections.lastChange = "maxUpRow"
            if direction == 3:
                col -= 1
                if maxDirections.maxLeftCol > col:
                    maxDirections.maxLeftCol -=1
                    maxDirections.lastChange = "maxLeftCol"
            if direction == 4:
                row -= 1
                if maxDirections.maxDownRow > row:
                    maxDirections.maxDownRow -=1
                    maxDirections.lastChange = "maxDownRow"
            cell = SpiralCell(row,col,num)
            return cell
    def getDistance(self):
        absRow = abs(self.row)
        absCol = abs(self.col)
        return absRow + absCol

class MaxDirections:
    maxLeftCol= 0
    maxRightCol= 0
    maxUpRow= 0
    maxDownRow = 0
    lastChange = ""

class Direction:
    RIGHT = 1
    UP = 2
    LEFT = 3
    DOWN = 4
    @staticmethod
    def nextDirection(previousCell,prevDir,maxDirections):

        if prevDir == Direction.RIGHT:
            if previousCell.col == maxDirections.maxRightCol:
                if maxDirections.lastChange == "maxRightCol":
                    direction = Direction.UP
                else:
                    #maxDirections.maxRightCol += 1
                    direction = Direction.RIGHT
            else:
                direction = Direction.RIGHT
        if prevDir == Direction.UP:
            if previousCell.row == maxDirections.maxUpRow:
                if maxDirections.lastChange == "maxUpRow":
                    direction = Direction.LEFT
                else:
                    #maxDirections.maxUpRow += 1
                    direction = Direction.UP
            else:
                direction = Direction.UP
        if prevDir == Direction.LEFT:
            if previousCell.col == maxDirections.maxLeftCol:
                if maxDirections.lastChange == "maxLeftCol":
                    direction = Direction.DOWN
                else:
                   # maxDirections.maxLeftCol -= 1
                    direction = Direction.LEFT
            else:
                direction = Direction.LEFT
        if prevDir == Direction.DOWN:
            if previousCell.col == maxDirections.maxDownRow:
                if maxDirections.lastChange == "maxDownRow":
                    direction = Direction.RIGHT
                else:
                    #maxDirections.maxDownRow -= 1
                    direction = Direction.DOWN
            else:
                direction = Direction.DOWN

        return direction

def GetCellSumByLocation(cells,row,col):
    surroundingCells = []
    for i in cells:
        if i.row == row-1 and i.col == col:
            surroundingCells.append(i)
        if i.row == row-1 and i.col+1 == col:
            surroundingCells.append(i)
        if i.row == row and i.col+1 == col:
            surroundingCells.append(i)
        if i.row == row+1 and i.col+1 == col:
            surroundingCells.append(i)
        if i.row == row+1 and i.col == col:
            surroundingCells.append(i)
        if i.row == row+1 and i.col-1 == col:
            surroundingCells.append(i)
        if i.row == row and i.col-1 == col:
            surroundingCells.append(i)
        if i.row == row-1 and i.col-1 == col:
            surroundingCells.append(i)

    s = 0
    for c in surroundingCells:
        s += c.num
    return s

input = 289326
sum = -99
currentNum = 0
previousCell = ""
previousOperation = 4 #this will start with going right
maxDir = MaxDirections()
maxDir.lastChange="maxDownRow"
cells = []

while sum <= input:
    if currentNum == 0:
        currentNum += 1
        continue
    if currentNum == 1:
        a = SpiralCell(0,0,num=currentNum)
        a.s = 1
        cells.append(a)
        currentNum += 1
        previousCell = a
        continue
    direction = Direction.nextDirection(previousCell=previousCell, prevDir=previousOperation, maxDirections=maxDir)
    previousOperation = direction
    cell = SpiralCell.getCell(previousCell=previousCell, direction=direction, num=currentNum,maxDirections=maxDir)
    previousCell = cell
    sum = GetCellSumByLocation(cells,cell.row,cell.col)
    cell.num = sum
    cells.append(cell)

d = previousCell.getDistance()
print(d)



