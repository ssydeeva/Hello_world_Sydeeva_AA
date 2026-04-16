N = int(input("Введите количество чисел N: "))

if N <= 0:
    print("Ошибка: N должно быть > 0!")
else:
    X = float(input("Введите число 1: "))
    max_value = X
    
    i = 2
    while i <= N:
        X = float(input(f"Введите число {i}: "))
        if max_value < X:
            max_value = X
        i = i + 1
    
    print(f"Максимальное из введённых {N} чисел = {max_value}")