def bitwise_operator(x,y):
    a = x & y
    b = x | y
    c = x ^ y
    return a,b,c

x=int(input("Enter the number:"))
y=int(input("Enter the number:"))
print(bitwise_operator(x,y))