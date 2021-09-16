def fact(n):
    if (n==0):
        return 1 
    return n*fact(n-1)

n=int(input())
r=int(input())
print(int(fact(n)/(fact(n-r)*fact(r))))
