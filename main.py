import time

print('Добро пожаловать, это секундомер!')
sec = int(input('Введите время, которое необходимо засечь(в секундах)'))
print(f'Вы ввели {sec} сек.')
time.sleep(sec)
print(f'Прошло {sec} сек.')

with open('logs.txt', 'a') as f:
    f.write(f'Запущен таймер на {sec} сек.\n')