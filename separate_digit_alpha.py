n=input()
l=[]
l1=[]
l2=[]
for i in n:
    if(i.isalpha()):
        l.append(i)
    elif(i.isdigit()):
        l1.append(i)
    else:
        l2.append(i)
print(l ,l1 ,l2)
