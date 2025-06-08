import math
import os
import time
yVals = [[20,10,50,40,100]]
yMax = max(yVals[0])
XDIST = 50 #available space for graph
YCHAR = 5/3 #height:width for characters
YDIST = 39
FULLCHAR = "#"
horizontalSeparator = "="
renderTable = []
elementGap = round((XDIST/2)/(len(yVals[0])))
gapPlace = []
xLabels = []
yLabels = [0, yMax]
yLabelPos = [YDIST, 0]
yLabelLength = 0
def y_check(valArray):
    countArray = []
    for dataArray in valArray:
        countArray.append(len(dataArray))
    sortedCountArray = sorted(countArray)
    print(countArray)
    if sortedCountArray[0] == sortedCountArray[-1]:
        return True
    else:
        return False
def reverseNorm(value,mode=0,base=10):
    if mode == 1:
        return math.sqrt(value*yMax**2)
    else:
        return value*yMax
def count_gap_place():
    global gapPlace
    for i in range(len(yVals[0])):
        gapPlace.append(elementGap+elementGap*i*2)
        #comment out if using custom labels:
        xLabels.append(10*i)
def make_y_label(fraction=4):
    global yLabels, yLabelLength, yLabelPos
    i = 1
    unitFrac = 1/fraction
    while i < fraction-1:
        yLabels.append(round(reverseNorm(unitFrac*i)))
        yLabelPos.append(round(YDIST*unitFrac*i))
        i += 1
    lengthDecider = []
    for i in yLabelPos:
        lengthDecider.append(len(str(i)))
    yLabelLength = sorted(lengthDecider)[-1]+1
    print(f"length {yLabelLength} labels {yLabels} label pos {yLabelPos}")
if __name__ == "__main__":
    count_gap_place()
    make_y_label()
    #print(gapPlace)
    #time.sleep(2)
def long_write(input, xLastPos, yPos=len(renderTable)-1):
    strInput = str(input)
    print(f"input {strInput} y {yPos}")
    firstX = xLastPos-len(strInput)+1
    if firstX >= 0:
        for i in range(len(strInput)):
            print(renderTable[firstX+i])
            print(f"y {yPos} firstX {firstX} i {i} last len {len(renderTable[firstX+i-1])} len {len(renderTable[firstX+i])}")
            if renderTable[firstX+i][yPos] == " ":
                
                
                renderTable[firstX+i][yPos] = strInput[i]
            else:
                print(f"x {firstX+i} letter {strInput[i]} would replace {renderTable[firstX+i][yPos]}")
                time.sleep(1)
    else:
        print(f"{input} ending at {xLastPos} with y {yPos} too long")
        time.sleep(2)
        renderTable[xLastPos][yPos] = strInput[-1]
def init_render_table(xdist, ydist,nullchar=" ", yLabelOffset=0):
    global renderTable
    yLabelOffset += 1 #space for separator lines and label
    yLabeli = 0
    while yLabeli < yLabelOffset:
        renderTable.append([])
        for yLabelj in range(ydist):
            if yLabeli+1 == yLabelOffset:
                renderTable[yLabeli].append("|")
            elif yLabeli+2 == yLabelOffset:
                if yLabelj in yLabelPos:
                    labelPlace = yLabelPos.index(yLabelj)
                    renderTable[yLabeli].append(nullchar)
                    long_write(yLabels[labelPlace],yLabeli,yLabelj)
                else:
                    renderTable[yLabeli].append(nullchar)
            else:
                renderTable[yLabeli].append(nullchar)
        yLabeli += 1
    for unoffset in range(xdist-yLabelOffset): #TBD: allocated space for y-descriptors on first few columns
        i = unoffset+yLabelOffset
        renderTable.append([])
        for j in range(ydist):
            if j == ydist-2:
                renderTable[i].append(horizontalSeparator)
            elif j == ydist-1:
                if (i in gapPlace):
                    renderTable[i].append(" ") #long_write can not append
                    long_write(xLabels[gapPlace.index(i)],xLastPos=i,yPos=j)
                else:
                    renderTable[i].append(nullchar)
            else:
                renderTable[i].append(nullchar)
    print((len(renderTable),len(renderTable[0])))

def write_render_table():
    global renderTable
    os.system("clear")
    tempRow = ""
    for i in range(len(renderTable[0])): #number of rows in first (all) columns
        for j in range(len(renderTable)):
            tempRow += str(renderTable[j][i])
        print(tempRow)
        tempRow = ""
def n_y(value, mode=0, base=10):
    if mode == 1:
        return (value**2)/(yMax**2) #square norming
    elif mode == 2:
        return (math.sqrt(value))/(math.sqrt(yMax))
    elif mode == 3:
        return (base**value)/(base**yMax)
    elif mode == 4:
        return(math.log(value,base=base))/(math.log(yMax,base=base))
    else:
        return value/yMax

def d_slope(height):
    targetTan = height/(XDIST/len(yVals[0]))
    print(targetTan)
    return 180*math.atan(targetTan)/math.pi #return value in degrees
def bar_graph(vals=yVals[0],offset=0,xdist=XDIST,ydist=YDIST, gap=elementGap):
    global yMax
    yMax = max(vals)
    gapPos = gap+offset
    for iVal in range(len(vals)):
        iterVal = vals[iVal]
        normY = round(ydist*(1-n_y(iterVal))) #lowest y has highest index
        i = len(renderTable[0])-2 #space for separator+numbers
        while i > normY:
            i -= 1
            renderTable[gapPos][i] = FULLCHAR
        gapPos += 2*gap #"gap" is half the intended gap
if __name__ == "__main__":
    init_render_table(XDIST,YDIST,yLabelOffset=yLabelLength)
    if y_check(yVals):
        iOffset = 0
        for dataArray in yVals:
            bar_graph(dataArray, offset=iOffset)
            iOffset += 1
    else:
        print("y check failed")
        time.sleep(1)
        bar_graph(yVals[0], offset=0)
    write_render_table()