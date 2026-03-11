videocards_count = int(input("Количество видеокарт: "))
videocards = []
for i in range(videocards_count):
    videocard = int(input(f"{i+1} Видеокарта: "))
    videocards.append(videocard)
max_vc = max(videocards)
new_vc = [x for x in videocards if x != max_vc]
print("Старый список видеокарт:",videocards)
print("Новый список видеокарт:",new_vc)