n = int(input("Кол-во коньков: "))
rol = []
for i in range(1,n+1):
    a = int(input(f"Размер {i}-й пары: "))
    rol.append(a)

k = int(input("\nКол-во людей: "))
p = []
for i in range(1,k+1):
    b = int(input(f"Размер ноги {i}-го человека: "))
    p.append(b)

count = 0
for i in p:
    if i in rol:
        rol.remove(i)
        count += 1

print("\nНаибольшее кол-во людей, которые смогут взять ролики:", count)
