def fetch_largest_number(array:list)->[int,int]:
    largest_number=-99999
    largest_index=0
    second_largest=-99999
    second_largest_index=0
    third_largest=-99999
    third_largest_index=0

    for index in range(0,len(array)):

        if largest_number < array[index]:
            third_largest_index=second_largest_index
            third_largest=second_largest
            second_largest_index=largest_index
            second_largest = largest_number
            largest_number=array[index]
            largest_index=index

    return(third_largest_index,third_largest)

array=list(map(int,input().split()))
print(fetch_largest_number(array))


