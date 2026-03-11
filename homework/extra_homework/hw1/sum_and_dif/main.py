def sum_of_digits(n):
    str_n =str(n)
    result = 0
    for i in str_n:
        result +=int(i)
    return result

def count_digits(n):
    count = 0
    while n > 0:
        n = n // 10
        count += 1
    return count

n = int(input("Введите число: "))

print(f"\nСумма чисел: {sum_of_digits(n)}")
print(f"Количество цифр в числе: {count_digits(n)}")
print(f"Разность суммы и количества цифр: {sum_of_digits(n)-count_digits(n)}")