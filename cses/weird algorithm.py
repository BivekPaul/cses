#this is a python program to execute the werid algorithm
#the question
#https://cses.fi/problemset/task/1068

n=int(input())
print(n, end=" ")

while True:
    if n==1:
        exit()
    if n%2==0:
        n/=2
    else:
        n=n*3+1
    print(int(n), end=" ")