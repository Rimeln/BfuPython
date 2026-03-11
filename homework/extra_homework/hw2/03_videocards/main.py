videocards = [3070, 2060, 3090, 3070, 3090]
max_vc = max(videocards)
new_vc = [x for x in videocards if x != max_vc]
print("Старый список видеокарт:",videocards)
print("Новый список видеокарт:",new_vc)