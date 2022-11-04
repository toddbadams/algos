import re
import string

def sepNums(s: string) -> int:
    if len(s)<1 or s[0:1]=='0': return 0
    return compare(0, '', s)

def compare(index: int, left: string, right: string) -> int:
    if right <= left: return 0
    if index==0: return(compare(1,right[0:1], right[1:len(right)]))
    count = 1
    # decompose right
    i = len(left)
    if i==0: i=1
    while i <= len(right):
        newLeft = right[0:index]
        newRight = right[i:len(right)-1]
        count += compare(newLeft, newRight)
        i+=1
    return count

assert sepNums('0') == 0
assert sepNums('') == 0
assert sepNums('094') == 0
assert sepNums('327') == 2
assert sepNums('1543267309') == 12