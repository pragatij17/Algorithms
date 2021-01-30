def max_number(array:list)->int:
    largest_no=-99999
    largest_index=0
    for index in range(0,len(array)):
        if(largest_no<array[index]):
            largest_no=array[index]
            largest_index=index
    return largest_index
array=[int(element) for element in input().split()]
print(max_number(array))