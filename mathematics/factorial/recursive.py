def fact(n):
    if n==0:
        return 1
    elif(n>=0):
        return n*fact(n-1)
    else:
        return "invalid"

n=int(input("Enter the Number:"))
print(fact(n))
