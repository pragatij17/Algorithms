import math 
def printDivisors(n): 
    i = 1
    while i <= math.sqrt(n):
        if (n % i == 0) :
            if (n / i == i) : 
                print (i), 
            else : 
                print (i) , n/i, 
        i = i + 1

n=int(input("Enter the number:"))