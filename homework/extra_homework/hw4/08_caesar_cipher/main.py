text = str(input("Введите сообщение: "))
k = int(input("Введите сдвиг: "))
alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
cipher_text = ""
for c in text:
    if c in alphabet:
        i = alphabet.index(c)
        cipher_text += alphabet[(i+3)%len(alphabet)]
    else:
        cipher_text += c
print(cipher_text)

