def isPower(n):
    if(n == 0):
        return True
    return ((n & (n - 1)) == 0)

n=int(input("Enter the number:"))
print(isPower(n))