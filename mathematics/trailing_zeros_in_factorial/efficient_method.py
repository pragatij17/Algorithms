def optimized_trailing_zeros(num: int) -> int:
    index = 5
    count_of_zeros = 0
    while index <= num:
        count_of_zeros += num // index
        index *= 5
    return count_of_zeros

num=int(input("Enter the Number:"))
print(optimized_trailing_zeros(num))