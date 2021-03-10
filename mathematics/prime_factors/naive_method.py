def isPrime(n) : 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
    if (n % 2 == 0 or n % 3 == 0): 
        return False
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
    return True

def primeFactor(n):
    for i in range(2,n):
        if(isPrime(i)):
            x=i
            while(n%x==0):
                print(i)
                x=x*i

n=int(input("Enter a number:"))
print(primeFactor(n))