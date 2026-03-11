k = int(input("Сдвиг: "))
my_list = [1, 2, 3, 4, 5]
print("Изначальный список: ", my_list)
new_list = my_list[-k:] + my_list[:-k]
print("Сдвинутый список: ",new_list)