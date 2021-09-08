s="a4gt4i33.567ytythfj34h"
a=list(s)
print(a)
stack=[]
for i in range(len(s)):
    if(s[i].isalpha()):
        stack.append(s[i])
print(stack)       
for i in range(len(stack)):
    print(stack.pop(),end="")

