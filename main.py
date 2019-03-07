import random

from ArrayStack import ArrayStack
from ListStack import ListStack
from ArrayQueue import ArrayQueue
from ListQueue import ListQueue
from NodeList import NodeList
from ArraySet import ArraySet
from ListSet import ListSet
from ArrayOrderedSet import ArrayOrderedSet
from ListOrderedSet import ListOrderedSet

random.seed(69)


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
    ind_pivot = ind_high
    val_pivot = arr[ind_pivot]
    ind_partition = ind_low
    for i in range(ind_low, ind_high): # from ind_low -> ind_high - 1 (don't want to reach ind_pivot = ind_high)
        if arr[i] < val_pivot:
            swap(arr, ind_partition, i)
            ind_partition += 1
    swap(arr, ind_partition, ind_pivot)
    return ind_partition


def partition_rand(arr, ind_low, ind_high):
    ind_pivot = random.randint(ind_low, ind_high+1)
    swap(arr, ind_high, ind_pivot)
    return partition(arr, ind_low, ind_high)


def quick_sort_helper(arr, ind_low, ind_high):
    if ind_low < ind_high:
        ind_partition = partition_rand(arr, ind_low, ind_high)
        quick_sort_helper(arr, ind_low, ind_partition-1)
        quick_sort_helper(arr, ind_partition+1, ind_high)


def quick_sort(arr):
    quick_sort_helper(arr, 0, len(arr)-1)


def binary_search(arr, val):
    ind_left = 0
    ind_right = len(arr) - 1
    while (ind_left <= ind_right):
        ind_mid = (ind_left + ind_right) // 2
        if val > arr[ind_mid]:
            ind_left = ind_mid + 1
        elif val < arr[ind_mid]:
            ind_right = ind_mid - 1
        else:
            return ind_mid
    return -1


def test_sort():
    test = [5, 27, 1, 7, -1, 2, 27, 9, 7, 3, 6]
    print_arr(test)
    quick_sort(test)
    print_arr(test)
    print(binary_search(test, 5))


def test_ArrayStack():
    s = ArrayStack()
    print(s.empty())
    for i in range(33):
        s.push(i)
        print('loop', i)
    print(s.top())
    s.print()


def test_ListStack():
    s = ListStack()
    print(s.empty())
    s.top()
    s.pop()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.top())
    s.pop()
    print(s.top())


def test_ArrayQueue():
    s = ArrayQueue()
    print(s.empty())
    for i in range(33):
        s.enqueue(i)
        print('loop', i)
    print(s.front())
    s.print()


def test_ListQueue():
    s = ListQueue()
    print(s.empty())
    s.enqueue(1)
    s.enqueue(2)
    s.enqueue(3)
    print(s.front())
    s.dequeue()
    print(s.front())
    s.dequeue()
    print(s.front())
    s.dequeue()
    print(s.front())


def test_NodeList():
    s = NodeList()
    print(s.empty())
    s.insert(0, 69)
    s.print()
    s.insert_front(3)
    s.insert_front(4)
    s.insert_front(5)
    s.insert_back(2)
    s.insert_back(1)
    s.print()
    s.remove(3)
    s.print()


def test_ArraySet():
    s = ArraySet()
    s.insert(1)
    s.insert(2)
    s.insert(3)
    s.insert(2)
    s.insert(1)
    s.insert(4)
    s.remove(1)
    s.remove(0)
    s.remove(3)
    s.print()


def test_ListSet():
    s = ListSet()
    s.insert(1)
    s.insert(5)
    s.insert(2)
    s.remove(3)
    s.remove(2)
    s.print()


def test_ArrayOrderedSet():
    s = ArrayOrderedSet()
    s.insert(5)
    s.insert(1)
    s.insert(3)
    s.insert(8)
    s.insert(2)
    s.remove(2)
    s.print()


def test_ListOrderedSet():
    s = ListOrderedSet()
    s.print()
    s.insert(2)
    s.insert(7)
    s.insert(1)
    s.insert(69)
    s.insert(42)
    s.insert(0)
    s.insert(6)
    s.insert(9)
    s.print()


if __name__ == '__main__':
    test_ListOrderedSet()
