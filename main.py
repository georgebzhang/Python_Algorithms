def print_arr(arr):
    for i in range(len(arr)):
        print(arr[i], " ", end="")
    print()


def swap(arr, ind1, ind2):
    temp = arr[ind1]
    arr[ind1] = arr[ind2]
    arr[ind2] = temp


def find_ind_min(arr):
    ind_min = 0
    val_min = arr[0]
    for i in range(1,len(arr)):
        if arr[i] < val_min:
            val_min = arr[i]
            ind_min = i
    return ind_min


def selection_sort(arr):
    for i in range(len(arr)):
        ind_min = find_ind_min(arr[i:len(arr)]) + i
        swap(arr, i, ind_min)


def insertion_sort(arr):
    ind_last_sorted = 0
    for i in range(1, len(arr)):
        count = 0
        for j in range(ind_last_sorted, -1, -1): # goes from ind_last_sorted -> 0
            ind_new = i - (ind_last_sorted - j)
            if arr[ind_new] < arr[j]:
                swap(arr, j, ind_new)
                count += 1
            else:
                continue
        ind_last_sorted += 1


def bubble_sort(arr):
    ind_last_sorted = len(arr)
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(ind_last_sorted - 1):
            if arr[i] > arr[i+1]:
                swap(arr, i, i+1)
                is_sorted = False
        ind_last_sorted -= 1


def merge(arr, left, right):
    ind_left = 0
    ind_right = 0
    ind_arr = 0
    while ind_left < len(left) and ind_right < len(right):
        if left[ind_left] < right[ind_right]:
            arr[ind_arr] = left[ind_left]
            ind_left += 1
        else:
            arr[ind_arr] = right[ind_right]
            ind_right += 1
        ind_arr += 1
    while ind_left < len(left):
        arr[ind_arr] = left[ind_left]
        ind_left += 1
        ind_arr += 1
    while ind_right < len(right):
        arr[ind_arr] = right[ind_right]
        ind_right += 1
        ind_arr += 1


def merge_sort(arr):
    size = len(arr)
    if size < 2:
        return
    mid = size//2
    left = arr[0:mid]
    right = arr[mid:size]
    merge_sort(left)
    merge_sort(right)
    merge(arr, left, right)


def partition(arr, ind_low, ind_high):
    ind_pivot = ind_low
    val_pivot = arr[ind_pivot]
    ind_partition = ind_low
    for i in range(ind_low, ind_high + 1):
        if arr[i] < val_pivot:
            swap(arr, ind_partition, i)
            ind_partition += 1
    return ind_partition


def quick_sort_helper(arr, ind_low, ind_high):
    if ind_low < ind_high:
        ind_partition = partition(arr, ind_low, ind_high)
        quick_sort_helper(arr, ind_low, ind_partition-1)
        quick_sort_helper(arr, ind_partition+1, ind_high)


def quick_sort(arr):
    quick_sort_helper(arr, 0, len(arr)-1)


test = [5, 1, 7, 2, 9, 3, 6]
print_arr(test)
quick_sort(test)
print_arr(test)
