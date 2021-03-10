def isPower(n):
    if(n == 0):
        return True    
    while(n != 1):
        if(n % 2 != 0):
            return False        
        n = n / 2    
    return True

n=int(input("Enter the number:"))
print(isPower(n))