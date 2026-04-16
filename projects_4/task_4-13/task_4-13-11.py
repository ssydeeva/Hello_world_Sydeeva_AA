N = int(input("Введите размер массива N: "))

if N <= 0:
    print("Ошибка: N должно быть > 0!")
else:
    A = []
    
    S = 0
    count = 0
    i = 1  
    
    while i <= N:
        element = float(input(f"Введите элемент A[{i}]: "))
        A.append(element)
        
        if i % 2 == 0:
            S = S + element
            count = count + 1
        
        i = i + 1
    
    if count > 0:
        Avg = S / count
        print(f"Массив: {A}")
        print(f"Сумма элементов с четными индексами: {S}")
        print(f"Количество элементов с четными индексами: {count}")
        print(f"Среднее арифметическое: {Avg}")
    else:
        print(f"Массив: {A}")
        print("Нет элементов с четными индексами!")