import math
import os
import time
import argparse
yVals = [[20,10,50,40,100]]
yMax = max(yVals[0])
XDIST = 50 #available space for graph
YCHAR = 5/3 #height:width for characters
YDIST = 39
FULLCHAR = "#"
horizontalSeparator = "="
renderTable = []
elementGap = 5
gapPlace = []
xLabels = []
yLabels = []
yLabelPos = []
yLabelLength = 0
fileSeparator = ","
debugLevel = 3 #set to 7 when long_write errors
customXLabels = False
xLabelShift = 0
def load_csv(filename):
    global yVals
    with open(filename) as file:
        loadCheck = 0
        for line in file:
            iLoad = 0
            yVals.append([])
            for item in line.split(fileSeparator):
                yVals[-1].append(float(item.strip())) #append to last dataset array
                iLoad += 1
            if debugLevel > 3: #debug
                if loadCheck < 1:
                    loadCheck = iLoad
                elif loadCheck == iLoad:
                    iLoad = 0 #reset loading counter
                else:
                    print(f"expected {loadCheck} got {iLoad} at line {line}")
                    raise ValueError(f"err when loading csv lines, last {yVals[-2]} now {yVals[-1]}")

def y_check(valArray):
    countArray = []
    for dataArray in valArray:
        countArray.append(len(dataArray))
    sortedCountArray = sorted(countArray)
    if sortedCountArray[0] == sortedCountArray[-1]:
        return True
    else:
        return False
def operation_2D(array2D,op=max):
    opArray = []
    for array1D in array2D:
        opArray.append(op(array1D))
    return (op(opArray),max(opArray),len(opArray))
def reverseNorm(value,mode=0,base=10):
    if mode == 1:
        return math.sqrt(value*yMax**2)
    else:
        return value*yMax
def count_gap_place():
    global gapPlace, elementGap
    elementGap = math.floor((XDIST/2)/(len(yVals[0])))
    for i in range(len(yVals[0])):
        gapPlace.append(elementGap+elementGap*i*2)
        #comment out if using custom labels:
        if False == customXLabels:
            xLabels.append(i)
    if gapPlace[-1] > XDIST-2:
        gapPlace[-1] = XDIST-2
    if debugLevel > 2:
        print(gapPlace)
        print(elementGap)
        time.sleep(1)
def make_y_label(fraction=4):
    global yLabels, yLabelLength, yLabelPos
    yLabels.append(round(yMax))
    yLabelPos.append(0)
    i = 1
    unitFrac = 1/fraction
    while i < fraction:
        yLabels.append(round(reverseNorm(unitFrac*i)))
        yLabelPos.append(round(YDIST*(1-unitFrac*i)))
        i += 1
    lengthDecider = []
    for i in yLabels:
        lengthDecider.append(len(str(i)))
    yLabelLength = sorted(lengthDecider)[-1]
    if debugLevel > 5:
        print(f"length {yLabelLength} labels {yLabels} label pos {yLabelPos}")
def halving(array,mult=0.5):
    i = 0
    while i < len(array):
        array[i] = float(array[i])*mult
        i += 1
def termgraph_prepare():
    global yVals,xLabelShift,yMax,XDIST,YDIST
    parser = argparse.ArgumentParser(description="CLI graph rendering")
    parser.add_argument("file", type=str, help="comma-separated values to plot, one set per each line")
    parser.add_argument("--y-label-fraction",type=int,default=4,help="Number of labels on the y axis")
    parser.add_argument("--y-space",default=39,help="Character count for graph height")
    parser.add_argument("--x-space",default=50,help="Character count for graph width")
    args = parser.parse_args()
    if args.file != "" and args.file != None :
        yVals = []
        load_csv(args.file)
        if debugLevel > 5:
            print(yVals)
    #if debugLevel > 2:
    #    for dataset in yVals:
    #        halving(dataset,1)
    xLabelShift = math.floor(len(yVals)/2)
    yMax = operation_2D(yVals,max)[0]
    XDIST = round(int(args.x_space))
    YDIST = round(int(args.y_space))
    count_gap_place()
    make_y_label(args.y_label_fraction)
if __name__ == "__main__":
    termgraph_prepare()
def long_write(input, xLastPos, yPos=len(renderTable)-1):
    strInput = str(input)
    if debugLevel > 6:
        print(f"input {strInput} y {yPos}")
    firstX = xLastPos-len(strInput)+1
    if firstX >= 0:
        for i in range(len(strInput)):
            if debugLevel > 6:
                print(renderTable[firstX+i])
                print(f"y {yPos} firstX {firstX} i {i} last len {len(renderTable[firstX+i-1])} len {len(renderTable[firstX+i])}")
            if renderTable[firstX+i][yPos] == " ":
                
                
                renderTable[firstX+i][yPos] = strInput[i]
            else:
                print(f"x {firstX+i} letter {strInput[i]} would replace {renderTable[firstX+i][yPos]}")
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
                    renderTable[i].append(nullchar) #long_write can not append
                    long_write(xLabels[gapPlace.index(i)],xLastPos=i+xLabelShift,yPos=j)
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
    gapPos = gap+offset
    for iVal in range(len(vals)):
        iterVal = vals[iVal]
        normY = round(ydist*(1-n_y(iterVal))) #lowest y has highest index
        i = len(renderTable[0])-2 #space for separator+numbers
        while i > normY:
            i -= 1
            renderTable[gapPos][i] = FULLCHAR
        gapPos += 2*gap #"gap" is half the intended gap
def termgraph_render():
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
if __name__ == "__main__":
    termgraph_render()