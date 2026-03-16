n = int(input("Кол-во человек: "))
k = int(input("Какое число в считалке? "))
print(f"Значит выбывает каждый {k}-й человек")

circle = [x for x in range(1, n+1)]
i=0

while len(circle) > 1:
    i = i % len(circle)
    print("\nТекущий круг людей:", circle)
    print("Начало счёта с номера", circle[i])
    i = (i+k-1) % len(circle)
    print("Выбывает человек под номером", circle[i])
    circle.pop(i)


print("\nОстался человек под номером", circle[0])