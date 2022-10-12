import time

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

def test():
    start = time.time()
    for n in range (1,51):
        print(f'{n}, {recursiveFibonacci(n)}, {((time.time()-start)*1000):.2f}ms')
    start = time.time()
    for n in range (1,51):
        print(f'{n}, {iterativeFibonnaci(n)}, {((time.time()-start)*1000):.2f}ms')

test()