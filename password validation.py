def val(n):
    if (len(n)>=10 and len(n)<32):
        return True
    if(n.isupper()):
        d=True
    if(n.isdigit()):
        f=True
        
p=input("enter password:")   
c=val(p)
if(c==True):
    print("Valid")
else:
    print("Invalid")
