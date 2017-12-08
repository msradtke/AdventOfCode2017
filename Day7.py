class program:
    def __init__(self):
        self.name = ""
        self.weight = 0
        self.children = []
        self.totalWeight = 0

def get_total_weight(parent):
    weight = parent.weight
    for child in parent.children:
        weight += get_total_weight(programs[child])
    parent.totalWeight = weight
    if parent.name == "smaygo":
        print()
    return weight



programs = {}
with open('C:\Users\MICK\Desktop\Day7.txt') as text:
    for row in text:
        row = row.replace("\n","")
        row = row.replace(",","")
        spl = row.split(" ")
        prog = program()
        first = True
        for s in spl:
            if first == True:
                if s == "fbnbt":
                    print "here"
                prog.name = s
                programs[s] = prog
                first = False
                continue
            if "(" in s:
                s = s.replace("(", "")
                s = s.replace(")", "")
                prog.weight = int(s)
                continue
            if "-" in s:
                continue
            prog.children.append(s)


base = ''
for p in programs.values():
    base = p
    isChild = False
    for p2 in programs.values():
        if p == p2:
            continue
        for child in p2.children:
            if child == p.name:
                isChild = True
                break
        if isChild:
            break
    if not isChild:
        break
print("parent: " + base.name)

for p in programs.values():
    if p.totalWeight == 0:
        get_total_weight(p)

for p in programs.values():
    childWeight = 0
    for child in p.children:
        c = programs[child]
        if childWeight == 0:
            childWeight = c.totalWeight
            continue
        if c.totalWeight != childWeight:
            print("------------------------------------------------------------------------")
            print c.name + ": " + str(c.weight)
            print ("parent: "+ p.name)

            for c2 in p.children:
                c3 = programs[c2]
                print("\t" + c3.name + ": " + str(c3.totalWeight) + " weight: " + str(c3.weight))
            print("not equal!")
            print c.name
            print c.weight
            print ("parent: "+ p.name)
            break



