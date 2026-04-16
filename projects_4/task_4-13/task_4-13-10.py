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
        
        if i % 2 != 0:
            S = S + element
        
        i = i + 1
    
    print(f"Массив: {A}")
    print(f"Сумма элементов с нечетными индексами (индексация с 1): {S}")