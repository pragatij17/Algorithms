def lcm(a,b):
    res=max(a,b)
    while(a>0):
        if(res%a==0 and res%b==0):
            return res
        res+=1
    return res

a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
print(lcm(a,b))  