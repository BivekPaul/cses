"""
https://cses.fi/problemset/task/1069
"""

lst=list(input())
max=0
sum=0
previous='0'

for i in lst:
    if i==previous:
        sum+=1
        previous = i
        if max<sum:
            max=sum
    else:
        sum = 1
        previous=i
        if max<sum:
            max=sum

print(max)