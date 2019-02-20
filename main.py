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


test = [5, 1, 7, 2, 9, 3, 6]
print_arr(test)
selection_sort(test)
print_arr(test)
