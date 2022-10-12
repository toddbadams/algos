# Dynamic Programming
Dynamic programming is essentially just an optimization technique. In dynamic programming, many different sets of algorithms are stored to solve each simple sub-problem. This works under the concept that smaller problems end in a complex one, so, once the sub-problems are corrected, the final scene is solved. Thus, the use of these techniques reduces errors, ensures efficacy in the linework, and improves the quality of the final result.

# Dynamic Programming Steps
In the rest of this post, I will go over a recipe that you can follow to figure out if a problem is a “DP problem”, as well as to figure out a solution to such a problem. Specifically, I will go through the following steps:

1. **Recognize a DP problem**  - can the problem solution be expressed as a function of solutions to similar smaller problems? This establishes a recursive structure between subproblems.
1. **Identify problem variables** - list examples of several subproblems and compare the parameters.
1. **Determine recurrence relation** - Once you figure out that the recurrence relation exists and you specify the problems in terms of parameters, this should come as a natural step. How do problems relate to each other? In other words, let’s assume that you have computed the subproblems. How would you compute the main problem?
1. **Identify the base cases** - A base case is a subproblem that doesn’t depend on any other subproblem, found by tring a few examples.
1. **Decide approach: iterative or recursive** - Analyse the trade-offs: time complexity, memory, readability, ease of implementation
1. **Add memoization** - used for storing the results of expensive function calls and returning the cached result when the same inputs occur again, thus lowering time complexity.

# Can Sum

Given target sum and array such as 7, [5, 4, 3, 7],  can the target sum be created from summation of any set of the numbers in the array.

Test cases
| target  |  array | expected  |  
|---|---|---|
| 7    | [4,2]      | False  |
| 7    | [5,3,4,7]  | True  | 
| 7    | [2,3]      | True  |
| 7    | [2,3,5]    | True  |
| 300  | [7,14]     | False |

``` python
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
```

#  How Sum

Given target sum and array such as 7, [5, 4, 3, 7],  return an array containing any combination of elements that add up to exactly the targetSum.

If there is no combination that adds up to the targetSum, then return null.

If there are multiple combinations possible, return any single one.

Test cases
| target  |  array | expected  |  
|---|---|---|
| 7    | [4,2]      | NULL  |
| 7    | [5,3,4,7]  | [3,4]  | 
| 7    | [2,3]      | [2,2,3]  |
| 7    | [2,3,5]    | [2,5]  |
| 300  | [7,14]     | NULL |

``` python
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
```


# Fibonacci Sequence
The Fibonacci Sequence is the series of numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

The next number is found by adding up the two numbers before it.

``` python
def recursiveFibonacci(n, memo={}):
    if n in memo.keys(): return memo[n]
    if n <= 2: return 1
    memo[n] = recursiveFibonacci(n-1, memo) + recursiveFibonacci(n-2, memo)
    return memo[n]

def iterativeFibonnaci(n):
    if (n<=2): return 1
    n1=1
    n2=1
    for i in range(3,n):
        temp = n1+n2
        n2 = n1
        n1 = temp
    return n1 + n2
```


# Climbing Stairs
You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Test Cases
| n | expected |
|---|---|
| 1 | 1 |
| 2 | 2 | 
| 3 | 3 | 
| 4 | 5 | 
| 5 | 8 | 
| 6 | 13 | 
| 45 | 1836311903 | 


Constraints
1 <= n <=45

``` python
# iterative approach, slower time, less memory
def climbStairsIterative(n: int) -> int:
    if (n<=3): return n
    n1 = 1
    n2 = 2
    i = 4
    while i <= n:
        temp = n1+n2
        n1 = n2
        n2 = temp
        i += 1
    return n1 + n2

# recursive approach, faster time, more memory
def climbStairsRecursion(n: int) -> int:
    if (n<=3): return n
    return climbStairsRecursion(n-1) + climbStairsRecursion(n-2)
```