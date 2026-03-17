h_str = str(input("Введите строку: "))
h = []
index = 0
for c in h_str:
    if c=="h":
        h.append(index)
    index += 1

reversal_str = h_str[h[0]+1:h[-1]][::-1]
print("Развёрнутая последовательность между первым и последним h:", reversal_str)