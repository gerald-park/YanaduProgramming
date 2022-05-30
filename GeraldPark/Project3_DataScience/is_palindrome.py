import math
def is_palindrome(word):
    #word의 길이를 얻는다. 
    #첫글자와 길이의 마지막 글자가 같다. 
    #첫글자는 N 마지막은 M
    #N+1 과 M-1 의 글자가 같다. 하나라도 틀리면 FALSE 
    #N+1 M-1이 같아질때까지 반복 
    M = len(word) - 1
    N = 0
    res = True
    for i in range(0, math.trunc(M/2)):  # i=버림(M/2)
        if word[N+i] != word[M-i]:
            res = False
            break
    return res

# 테스트
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))

