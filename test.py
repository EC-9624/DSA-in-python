"""
Searching
"""


def linear_search(arr, target):
    for i in range(len(arr)):
        if target == arr[i]:
            return i
    return -1


def binary_Search(arr, target):

    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # not found


list = [1, 3, 5, 7, 9, 10, 12, 13, 15, 20]
target_e = 20

res = binary_Search(list, target_e)
print("target ai index", res)
res2 = linear_search(list, target_e)
print("target ai index", res2)

"""
Sorting
"""


def bubble_Sort(arr):
    for i in range(len(arr)):
        swapped = False
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                swapped = True
        if not swapped:
            break


my_list = [64, 34, 25, 12, 22, 11, 90]
bubble_Sort(my_list)
print("Sorted array:", my_list)
