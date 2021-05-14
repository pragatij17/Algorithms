def largest_num(array:list)->int:
    largest_no=-99999
    largest_index=0
    for index in range(0,len(array)):
        if(largest_no<array[index]):
            largest_no=array[index]
            largest_index=index
    del array[largest_index]
    largest_no=-99999
    largest_index=0
    for index in range(0,len(array)):
        if(largest_no<array[index]):
            largest_no=array[index]
            largest_index=index
    return largest_no

array=list(map(int,input().split()))
print(largest_num(array))