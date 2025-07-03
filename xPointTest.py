def c(s):
    pass
yVals = []
xVals = []
def newSubroutine(inputLine,lineNum):
    global yVals
    if len(yVals) == 0:
        yVals.append([])
    iItem = 0
    for item in inputLine:
        if len(yVals) > iItem:
            yVals[iItem].append(float(item))
            c("iItem is the set of values-position, item is the current item")
        else:
            yVals.append([])
            for retrieve in yVals[0]:
                yVals[-1].append(float(retrieve))
            yVals[-1][-1] = float(item)

            c("all X columns have to be at least depth 0, so they are in yVals[0]")
        iItem += 1 
def newLoad(path,doCustomX=False):
    global yVals, xVals
    yVals = []
    with open(path) as file:
        iLine =0
        for line in file:
            splitLine=line.strip().split(",")
            if doCustomX:
                xVals.append(splitLine[0])
                newSubroutine(splitLine[1:],iLine)
            else:
                newSubroutine(splitLine,iLine)