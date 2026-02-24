operator_name = input('Введите имя оператора: ')
pressure = input('Введите текущее значение давления (Па): ')
with open("sensor_log.txt", "w", encoding="utf-8") as sensor_log: sensor_log.write(f'Оператор:\tТекущее значение давления (Па): \n{operator_name}\t{pressure}')
print('Данные успешно сохранены в sensor_log.txt')
