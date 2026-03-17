n = int(input("Введите длину списка: "))
gen = [1 if x%2==0 else x%5 for x in range(n)]
print("Результат:", gen)