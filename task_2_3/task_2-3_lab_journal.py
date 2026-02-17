name = input('Введите ФИО исследователя: ')
date = input('Введите дату: ')
experiment = input('Введите название эксперимента: ')
conclusion = input('Введите вывод: ')
lines = [
        'Лабораторный журнал',
        '',
        f"ФИО исследователя: {name}",
        f"Дата: {date}",
        f"Название эксперимента: {experiment}",
        f"Вывод: {conclusion}",
        ""
        ]
max_len = max(len(line) for line in lines)
width = max_len + 4
with open('journal.txt', 'w', encoding='utf-8') as f:
    f.write('+' + '-' * (width - 2) + '+\n')
    for line in lines:
        f.write('| ' + line.ljust(width - 4) + '|\n')
        f.write('+' + "-" * (width - 2) + '+\n')
print('Данные успешно записаны в файл journal.txt')