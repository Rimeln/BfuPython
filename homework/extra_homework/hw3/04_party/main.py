guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
answer = ""
while answer != "Пора спать":
    print(f"\nСейчас на вечеринке {len(guests)} человек: {guests}")
    answer = str(input("Гость пришёл или ушёл? "))
    if answer == "пришёл":
        guest = str(input("Имя гостя: "))
        if len(guests) >= 6:
            print(f"Прости, {guest}, но мест нет.")
        else:
            print(f"Привет, {guest}!")
            guests.append(guest)

    if answer == "ушёл":
        guest = str(input("Имя гостя: "))
        if not(guest in guests):
            print("Такого гостя нет на вечеринке.")
        else:
            print(f"Пока, {guest}!")
            guests.remove(guest)

print("\nВечеринка закончилась все легли спать.")
