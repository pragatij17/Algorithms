def countDigits(x):
    count=0
    while x>0:
        x=x//10
        count+=1
    return count
x=int(input("Enter the Number:"))
print(countDigits(x))
