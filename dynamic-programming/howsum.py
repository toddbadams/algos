# Write a function howSum(targetSum, numbers) that takes in a 
# targetSum and an array of numbers as arguments.
# The function should return an array containing any combination 
# of elements that add up to exactly the targetSum. If there is no
# combination that adds up to the targetSum, then return null
# If there are multiple combinations possible, you may return any single one.

from asyncio.windows_events import NULL


def howSum(target, arr, memo={}):
    if target in memo.keys(): return memo[target][0]
    if target == 0: return memo[target][1]
    for number in arr:
        newTarget = target - number
        if newTarget < 0: continue
        r = howSum(newTarget, arr, memo) 
        if (r != []):
            memo[newTarget][0] = True   
            memo[newTarget][1].append(r)         
            return memo[newTarget][1]
    memo[newTarget][0] = False
    return NULL

## tests
def test(target, arr, expected):
    actual = howSum(target, arr)
    print(f'{target},{arr} should be {expected}, actual={howSum(7,[4,2])}, {("Passed","Failed")[expected!=actual]}')

test(7,[4,2],NULL)
test(7,[5,3,4,7],[3,4])
test(7,[2,3],[2,2,3])
test(7,[2,3,5],[2,5])
test(300,[7,14],NULL)