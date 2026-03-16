text = str(input("Введите текск: "))
vowels = ["а", "е", "у", "о", "ё", "ы", "я", "и", "ю", "э"]
vowels_text = []
for i in text:
    if i in vowels:
        vowels_text.append(i)

print("\nСписок гласных букв:", vowels_text)
print("Длина списка:", len(vowels_text))
