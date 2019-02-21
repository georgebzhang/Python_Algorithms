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
        for j in range(ind_last_sorted, -1, -1):
            ind_new = i - (ind_last_sorted - j)
            if arr[ind_new] < arr[j]:
                swap(arr, ind_new, j)
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


test = [5, 1, 7, 2, 9, 3, 6]
print_arr(test)
insertion_sort(test)
print_arr(test)
