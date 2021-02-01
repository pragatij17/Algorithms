def countZeroes(n):
    fact=1
    for index in range(2,n+1):
        fact=fact*index
    res=0
    while ((fact%10)==0):
        res+=1
        fact=fact//10
    return res

n=int(input("Enter the number:"))
print(countZeroes(n))