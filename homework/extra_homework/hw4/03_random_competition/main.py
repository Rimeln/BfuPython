import random

list1 = [round(random.uniform(5,10), 2) for i in range(20)]
list2 = [round(random.uniform(5,10), 2) for i in range(20)]
winners_list = []
for i in range(20):
    winners_list.append(max(list1[i], list2[i]))
print("Первая команда:", list1)
print("Вторая команда:",list2)
print("Победители тура:", winners_list)