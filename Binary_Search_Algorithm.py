def binarySearch(array, target):
    '''Takes one array & target number,
    returns the index position of the target'''

    left = 0
    right = len(array)
    middle = (left + right) //2

    while left<=right:
        middle = (left+right) // 2
        if target == array[middle]:
            return middle
        elif target > array[middle]:
            left = middle + 1
        else:
            right = middle - 1

array = [1,5,8,9,10,59,76]
target = 1
index = binarySearch(array,target)
print(f'The number {target} is present at {index}th index')
