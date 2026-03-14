violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]
music_time = 0
n = int(input("Сколько песен выбрать? "))
for i in range(1,n+1):
    music = str(input(f"Название {i}-й песни: "))
    for j in violator_songs:
        if j[0] == music:
            music_time += j[1]
print(f"\nОбщее время звучания песен: {music_time} минуты")