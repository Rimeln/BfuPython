def merge_sorted_lists(arr1, arr2):
    for i in arr1:
        while i in arr2:
            arr2.remove(i)
    arr1.extend(arr2)
    arr1.sort()
    return arr1


list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 5, 6, 8, 10]
merged = merge_sorted_lists(list1, list2)
print(merged)