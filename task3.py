string = input('Введіть текст:')
count = 0
for i in range(len(string)):
    if string[i] == "H":
        count += 1
    else:
        pass
print('Символ зустрічається таку кількість разів:', count)
