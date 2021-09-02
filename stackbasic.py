stack=[]
n=int(input("number of element you want to add in stack:"))
for i in range(n):
    i=input()
    stack.append(i)

print(stack)
d=int(input("number of element you want to add in stack:"))
for i in range(d):
    stack.pop()

print(stack)
