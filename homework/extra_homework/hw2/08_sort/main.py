def my_sort(arr):
    for i in range (len(arr)):
        for j in range (0, len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

my_list = [5, 9, -3, 4, 2]
print("Изначальный список:", my_list)
print("\nОтсортированный список:", my_sort(my_list))