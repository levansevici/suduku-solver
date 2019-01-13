#  python 3.6
def getposi(a):
    posi = {}
    for i in range(9):
        for j in range(9):
            if a[i][j] == 0 :
                pos = [1,2,3,4,5,6,7,8,9]
                pos = rowcheak(pos,a,i)
                pos = colcheak(pos,a,j)
                pos = boxcheak(pos,a,i,j)
                posi.update({str(i)+str(j):pos})
            else:
                posi.update({str(i)+str(j):[a[i][j]]})
    return posi
def rowcheak(pos,a,i):
    for k in range(9):
        if (a[i][k] != 0) and (a[i][k] in pos):
            pos.remove(a[i][k])
    return pos
def colcheak(pos,a,j):
    for k in range(9):
        if (a[k][j]!=0) and (a[k][j] in pos):
            pos.remove(a[k][j])
    return pos
def boxcheak(pos,a,i,j):
    i = math.floor(i/3)
    j = math.floor(j/3)
    for k in range(3):
        for l in range(3):
            if (a[i*3+k][j*3+l] != 0) and (a[i*3+k][j*3+l] in pos):
                pos.remove(a[i*3+k][j*3+l] )
    return pos
def cheakempty(posi):
    empty = {}
    isfulled = True
    for i in range(9):
        for j in range(9):
            if len(posi.get(str(i)+str(j)))==1 :
                empty.update({str(i)+str(j):1})
            else:
                empty.update({str(i)+str(j):0})
                isfulled = False
    return empty,isfulled
def refreash(empty,a,posi):
    isrefreashed = False
    for i in range(9):
        for j in range(9):
            if empty.get(str(i)+str(j))==1 and a[i][j]==0:
                a[i][j]=posi.get(str(i)+str(j))[0]
                isrefreashed = True
    return a,isrefreashed
def cheakwrong(posi,a,isfulled):
    iswrong = False
    for i in range(9):
        for j in range(9):
            if posi.get(str(i)+str(j))==[]:
                iswrong = True
    if isfulled:
        for i in range(9):
            row = []
            col = []
            box = []
            for j in range(9):
                row.append(a[i][j])
                col.append(a[j][i])
            for j in range(3):
                for k in range(3):
                    box.append(a[math.floor(i/3)*3+j][divmod(i,3)[1]*3+k])
            for j in range(1,10):
                if not (j in row) or not (j in col) or not (j in box):
                    iswrong = True
    return iswrong
def findtry(posi):
    for k in range(2,10):
        for l in range(9):
            for m in range(9):
                if len(posi.get(str(l)+str(m)))==k:
                    return l,m
def solver(a,n):
    isfulled = False
    isrefreashed = True
    iswrong = False
    issolved = False
    olda = a.copy()
    while 1-isfulled and isrefreashed and 1-iswrong:
        posi = getposi(a)
        empty,isfulled = cheakempty(posi)
        a,isrefreashed = refreash(empty,a,posi)
        posi = getposi(a)
        empty, isfulled = cheakempty(posi)
        iswrong = cheakwrong(posi,a,isfulled)
    a, isrefreashed = refreash(empty, a, posi)
    iswrong = cheakwrong(posi, a, isfulled)
    if isfulled and 1-iswrong:
        issolved = True
        return a,issolved
    elif iswrong:
        return olda,issolved
    else:
        i,j = findtry(posi)
        trys = posi.get(str(i)+str(j))
        for k in range(len(trys)):
            newa = a.copy()
            newa[i][j]=trys[k]
            # print("try",trys,trys[k],"of",(i,j),"in depth",n+1)
            # print(newa)
            newa,issolved = solver(newa,n+1)
            newa = newa.copy()
            if issolved:
                return newa,issolved
        return olda,issolved
if __name__ == "__main__":
    import numpy, math, time
    a = numpy.array([[0, 0, 0, 1, 0, 0, 0, 0, 0],
                     [0, 0, 1, 0, 6, 0, 2, 0, 0],
                     [4, 0, 0, 0, 9, 3, 0, 6, 0],
                     [3, 0, 0, 0, 0, 2, 0, 0, 5],
                     [0, 0, 5, 4, 0, 0, 1, 0, 2],
                     [0, 0, 0, 0, 0, 0, 0, 8, 0],
                     [9, 0, 0, 8, 2, 0, 0, 0, 0],
                     [0, 0, 7, 0, 0, 0, 0, 1, 8],
                     [0, 4, 0, 9, 0, 0, 0, 2, 0]])
    a,issolved = solver(a,0)
    print(a)
