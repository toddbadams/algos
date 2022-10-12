from asyncio.windows_events import NULL

def textsum(word, arr, memo={}):
    if len(word)==0: return []
    for letters in arr:
        if word.startswith(letters)==False: continue
        newWord = word[len(letters):]
        if newWord in memo.keys(): continue
        result = textsum(newWord, arr)
        if result is NULL: 
            memo[newWord] = False
            continue
        result.insert(0,letters)
        return result
    return NULL

# test scenarios
def test(word, arr, expected):
    actual = textsum(word, arr)
    print(f'word={word}, arr={arr}, result={actual}, {("Passed","Failed")[expected!=actual]}')

test('', ['ab', 'abc', 'cd', 'def', 'abcd'], [])
test('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd'], ['abc', 'def'])
test('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee'], ['abc', 'def'])
