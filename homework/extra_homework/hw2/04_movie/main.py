films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия', 'Город грехов', 'Мементо', 'Отступники', 'Деревня']

n = int(input("Сколько фильмов хотите добавить? "))
user_films = []
for i in range(n):
    film = str(input("Введите название фильма: "))
    if film in films:
        user_films.append(film)
    else:
        print(f"Ошибка: фильма {film} у нас нет :(")
print("Ваш список любимых фильмов:", end=" ")
for i in range(len(user_films)):
    print(user_films[i], end=" ")