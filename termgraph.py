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
yLabels = []
def y_check(valArray):
    countArray = []
    for dataArray in valArray:
        countArray.append(len(dataArray))
    sorted(countArray)
    print(countArray)
    if countArray[0] == countArray[-1]:
        return True
    else:
        return False
def count_gap_place():
    global gapPlace
    for i in range(len(yVals[0])):
        gapPlace.append(elementGap+elementGap*i*2)
        #comment out if using custom labels:
        xLabels.append(10*i)
def make_y_label(fraction):
    i = 1
    unitFrac = 1/fraction
    while i < fraction-1:
        yLabels.append((reverseNorm(unitFrac*i),round(YDIST*unitFrac*i)))
        i += 1
if __name__ == "__main__":
    count_gap_place()
    #print(gapPlace)
    #time.sleep(2)
def long_write(input, xLastPos, yPos=len(renderTable)-1):
    strInput = str(input)
    firstX = xLastPos-len(strInput)+1
    if firstX >= 0:
        for i in range(len(strInput)):
            if renderTable[firstX+i][yPos] == " ":
                renderTable[firstX+i][yPos] = strInput[i]
            else:
                print(f"x {firstX+i} letter {strInput[i]} would replace {renderTable[firstX+i][yPos]}")
                time.sleep(1)
    else:
        print(f"{input} ending at {xLastPos} too long")
        time.sleep(2)
        renderTable[xLastPos][yPos] = strInput[-1]
def init_render_table(xdist, ydist,nullchar=" ", yLabelOffset=0):
    global renderTable
    yLabelOffset += 1 #space for separator lines
    yLabeli = 0
    while yLabeli < yLabelOffset:
        renderTable.append([])
        for yLabelj in range(ydist):
            if yLabeli+1 == yLabelOffset:
                renderTable[yLabeli].append("|")
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
def reverseNorm(value,mode=0,base=10):
    if mode == 1:
        return math.sqrt(value*yMax**2)
    else:
        return value*yMax
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
    init_render_table(XDIST,YDIST,yLabelOffset=1)
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