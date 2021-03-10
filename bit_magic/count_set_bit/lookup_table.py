def initialize(): 
      table[0] = 0
      for i in range(0,256):
          table[i] =(i & 1) + table[i / 2]	
def countSetBits(n):
    return table[n & 0xff] +
    table[(n >> 8) & 0xff]+
    table[(n >> 16) & 0xff]+
    table[n >> 24]

n=int(input("Enter the number:"))
print(countSetBits(n))