n = int(input("Кол-во чисел: "))
digits = []
for i in range(n):
    a=int(input("Число: "))
    digits.append(a)
print("\nПоследовательность:", digits)

if digits == digits[::-1]:
    print("Последовательность симметрична")

else:
    for i in range(n):
        if digits[i:] == digits[i:][::-1]:
            print("Нужно приписать чисел:", len(digits[:i][::-1]))
            print("Сами числа:", digits[:i][::-1])