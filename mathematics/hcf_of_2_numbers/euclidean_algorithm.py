def gcd(a,b):
    while a!=b:
        if a>b:
            a=a-b
        else:
            b=b-a
    return a

a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
print(gcd(a,b))