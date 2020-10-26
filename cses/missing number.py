#https://cses.fi/problemset/task/1083
"""
what i am planning to do is
kindof the best method to do this particular question
here we simply substract the sum of n numbers by n*(n+1) / 2
and then substract the sum of the numbers from the input
here: sum(lst)
"""


n=int(input())
lst=[int(x) for x in input().strip().split()]

print(int(((n*(n+1))/2)-sum(lst)))