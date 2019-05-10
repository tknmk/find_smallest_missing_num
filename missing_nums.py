# -*- coding: utf-8 -*-

# Find the smallest missing number in a list
def findMissingNo(arr, n):

    for i in range(n) :

        if (arr[i] <= 0 or arr[i] > n):
            continue

        val = arr[i]

    while (arr[val-1] != val):
        nextval = arr[val-1]
        arr[val-1] = val
        val = nextval
        if (val <= 0 or val > n):
            break

    for i in range(n):
        if (arr[i] != i + 1) :
            return i + 1

    return n + 1


if __name__ == '__main__':
    # sample list
    arr = [ 2, 3, 7, 6, 8, -1, -10, 15 ]
    
    arr_size = len(arr)
    missing = findMissingNo(arr, arr_size)
    print( 'The smallest positive', 'missing number is ', missing)

