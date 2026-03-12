my_list = [1, 2, 3, 4, 5]
print("Изначальный список:", my_list)
print("Четные элементы в обратном порядке: ",end=' ')
for i in range (1, len(my_list)+1):
    if my_list[-i] % 2 == 0:
        print(my_list[i], end=' ')
