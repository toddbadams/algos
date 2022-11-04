

class node:
    def __init__(self, num: int) -> None:
        self.num = num

    def __eq__(self, obj):
        return self.num == obj.num

    def __gt__(self, obj):
        return self.num > obj.num

    def __str__(self) -> str:
        return str(self.num)

    def __repr__(self) -> str:
        return str(self.num)
        

def longestConsecutive(nums: list[int]) -> int:
    result = 0
    i = 1
    current = 0
    while i < len(nums):
        if nums[i] > nums [i-1]:
            current += 1
        i += 1   
    return result


def test(nums: list[int], expected: int):
    actual = longestConsecutive(nums)
    print(f'nums = {nums}, result={actual}')
    assert actual == expected

test([100,4,200,1,3,2], 4)
test([0,3,7,2,5,8,4,6,0,1], 9)