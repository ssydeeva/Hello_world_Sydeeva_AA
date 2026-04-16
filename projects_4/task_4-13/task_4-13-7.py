N = int(input("Введите размер массива N: "))

if N <= 0:
    print("Ошибка: N должно быть > 0!")
else:
    A = []
    
    S = 0
    i = 1
    while i <= N:
        element = float(input(f"Введите элемент A[{i}]: "))
        A.append(element)
        S = S + element
        i = i + 1
    
    Avg = S / N
    
    print(f"Массив: {A}")
    print(f"Сумма элементов: {S}")
    print(f"Среднее арифметическое: {Avg}")