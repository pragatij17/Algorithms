def countTrailingZeros(n):
    res=0
    for index in range(5,n+1,5):
        res=res+(n//index)
    return res

n=int(input("Enter the Number:"))
print(countTrailingZeros(n))