def isKthBitSet(n,k):
    if((n >> (k - 1)) & 1):
        return "SET"
    else:
        return "NOT SET" 

n=int(input("Enter the number:"))
k=int(input("Enter the number:"))
print(isKthBitSet(n,k))