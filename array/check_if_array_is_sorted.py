def arraySortedOrNot(arr, n):
    if (n == 0 or n == 1):
        return True
    return (arr[n - 1] >= arr[n - 2] and
            arraySortedOrNot(arr, n - 1))

arr=list(map(int,input().split()))
n=len(arr)

if (arraySortedOrNot(arr, n)):
        print("Yes")
else:
        print("No")