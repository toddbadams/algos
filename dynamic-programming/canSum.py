## given target sum and array such as 7, [5, 4, 3, 7]
## can the target sum be created from summation of a set of the numbers in the array

def canSum(target, arr, memo={}):
    if target in memo.keys(): return memo[target]
    if target == 0: return True
    for number in arr:
        newTarget = target - number
        if newTarget < 0: continue
        if canSum(newTarget, arr, memo): 
            memo[newTarget] = True            
            return True
    memo[newTarget] = False
    return False

## tests
def test(target, arr, expected):
    actual = canSum(target, arr)
    print(f'{target},{arr} should be {expected}, actual={canSum(7,[4,2])}, {("Passed","Failed")[expected!=actual]}')

test(7,[4,2],False)
test(7,[5,3,4,7],True)
test(7,[2,3],True)
test(7,[2,3,5],True)
test(300,[7,14],False)
