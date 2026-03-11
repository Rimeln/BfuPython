containers_count = int(input("Количество контейнеров: "))
containers = []
for i in range(containers_count):
    container = int(input("Введите вес контейнера:"))
    if container > 200:
        print("Вес контейнера не может быть больше 200")
        exit()
    containers.append(container)

new_container = int(input("\nВведите вес нового контейнера: "))

count = 0
for i in containers:
    if i < new_container:
        print("\nНомер, который получит новый контейнер: ", count+1)
        break
    else:
        count += 1