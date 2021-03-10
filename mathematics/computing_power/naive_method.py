def computingPower(base,power):
    res=1
    for index in range(0,power):
        res=res*base
    return res

power=int(input("Enter the number:"))
base=int(input("Enter the number:"))
print(computingPower(power,base))
