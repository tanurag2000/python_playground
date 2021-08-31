lst=[]
n=int(input("number of element:"))
for i in range(n):
    i=int(input())
    lst.append(i)
    
print(lst)    

j=int(input("search:"))
for i  in lst:
    if(i==j):
        print("element at",i)