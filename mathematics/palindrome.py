def isPal(n):
    rev=0
    temp=n
    while temp!=0:
        ld=temp%10
        rev=rev*10+ld
        temp=temp//10
    return(rev==n)
a=int(input("Enter the number:"))
print(isPal(a))