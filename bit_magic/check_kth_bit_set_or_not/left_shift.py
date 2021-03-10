def isKthBitSet(n,k):
    if(n &(1 << (k - 1))!=0):
        return "SET"
    else:
        return "NOT SET" 

n=int(input("Enter the number:"))
k=int(input("Enter the number:"))
print(isKthBitSet(n,k))