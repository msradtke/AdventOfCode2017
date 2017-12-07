def distribute_evenly():
    True

def check_for_dupes(subject, listToCheck):
    for i in listToCheck:
        is_dupe = True
        index = 0
        for i2 in i:
            if subject[index] != i2:
                is_dupe = False
                break
            index += 1
        if is_dupe:
            return True
    return is_dupe


count = 0
patterns = []
dupeCount = []
with open('C:\Users\MICK\Desktop\Day6.txt') as text:
    t = text.read()
    mems = map(int,t.split("\t"))
    firstToAdd = list(mems)
    patterns.append(firstToAdd)
    totalCount = len(mems)
    while True:
        mems = list(mems)
        maxMem = max(mems)
        maxMemIndex = mems.index(max(mems))

        remainder = maxMem
        mems[maxMemIndex] = 0
        if maxMem >= totalCount:
            toAdd = maxMem / totalCount
            remainder = maxMem % totalCount

            for i, m in enumerate(mems):
                mems[i] += toAdd
        if remainder > 0:
            index = maxMemIndex + 1
            while remainder > 0:
                if index > (totalCount - 1):
                    index = 0
                mems[index] += 1
                index += 1
                remainder -= 1
        is_dupe = check_for_dupes(mems,patterns)
        count += 1
        if is_dupe:
            dupeCount.append(count)
            print "dupe at: " + str(count)
            patterns = []
            count = 0

        patterns.append(mems)
    print count