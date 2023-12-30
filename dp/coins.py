from typing import List


def min_ignore_none(a,b):
    if a is None:
        return b
    if b is None:
        return a
    return  min(a,b)

memo = {}
def minimum_coins(m,coins):
    if m in memo :
        return memo[m]
    if m == 0 :
        answer = 0
    else :
        answer = None
        for coin in coins : 
            # print(coin)
            subproblem = m - coin
            if subproblem < 0 : 
                continue
            answer = min_ignore_none(answer,minimum_coins(subproblem,coins)+1)
    memo[m] =  answer
    return answer

print(minimum_coins(m=13,coins=[1,4,5]))