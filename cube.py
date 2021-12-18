inp = input()
data = []
no_match = True
while inp != 'end':
    data.append(inp.split()[-1])
    inp = input()
for i in range(len(data)):
    for j in range(len(data[i])):
        for k in data[i:]:
            if k != data[i] and data[i][:j] + data[i][j+1:] == k[:j] + k[j+1:]:
                print('Найден куб:', k[:j] + 'X' + k[j+1:], f'связывающий элементы{i + 1}-{data.index(k) + 1}',
                      f'элемент {i + 1}:{data[i]}, элемент {data.index(k) + 1}:{k}')
                no_match = False
if no_match:
    print("Кубов не найдено. Если они обязаны были быть, перепроверьте ввод")