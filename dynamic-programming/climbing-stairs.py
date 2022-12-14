from ast import Num
from tkinter import N

# iterative approach, slower time, less memory
def climbStairsIterative(n: int) -> int:
    if (n<=3): return n
    n1 = 3
    n2 = 5
    i = 4
    while i < n:
        temp = n1
        n1 = n2
        n2 = temp+n2
        i += 1
    return n2

# recursive approach with memotization, faster time, less memory
def climbStairsRecursion(n: int, memo={}) -> int:
    if n in memo.keys(): return memo[n]
    if (n<=3): return n
    result = climbStairsRecursion(n-1, memo) + climbStairsRecursion(n-2, memo)
    memo[n] = result
    return result

assert climbStairsIterative(1) == 1
assert climbStairsIterative(2) == 2
assert climbStairsIterative(3) == 3
assert climbStairsIterative(4) == 5
assert climbStairsIterative(5) == 8
assert climbStairsIterative(6) == 13
assert climbStairsIterative(45) == 1836311903

assert climbStairsRecursion(1) == 1
assert climbStairsRecursion(2) == 2
assert climbStairsRecursion(3) == 3
assert climbStairsRecursion(4) == 5
assert climbStairsRecursion(5) == 8
assert climbStairsRecursion(6) == 13
assert climbStairsRecursion(45) == 1836311903

