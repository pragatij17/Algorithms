def min_number(array:list)->int:
    smallest_no = 99999999
    smallest_index=0
    for index in range(0,len(array)):
        if(smallest_no > array[index]):
            smallest_no=array[index]
            smallest_index=index
    return(smallest_index)
array=[int(element) for element in input().split()]
print(min_number(array))