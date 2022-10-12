## move from start to end in a grid
## start is upper left square
## end if lower right
## can only move down and right
## calculate the number of paths
import time

def gridTraveler(rows, cols, memo={}):
    if rows < 1 or cols < 1: return 0
    if rows == 1 or cols == 1: return 1
    if (rows,cols) in memo.keys(): return memo[(rows,cols)]
    memo[(rows,cols)] = gridTraveler(rows-1,cols,memo) + gridTraveler(rows,cols-1,memo)
    return memo[(rows,cols)]


def test():
    start = time.time()
    for r in range (2,10):
        for c in range(2,10):
            print(f'{r},{c}, {gridTraveler(r,c)}, {((time.time()-start)*1000):.2f}ms')

test()