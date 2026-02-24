weight = float(input('Введите ваш вес (кг): '))
height = float(input('Введите ваш рост (м): '))
bmi = weight / (height ** 2)
print(f'---Отчет о состоянии здоровья---\nРост:\t{height}\nВес:\t{weight}\nИндекс массы тела:\t{bmi:.2f}')