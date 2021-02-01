def gcd(a,b):
    r=min(a,b)
    while(r>0):
        if (a%r==0 and b%r==0):
            break
        r-=1
    return r

a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
print(gcd(a,b))