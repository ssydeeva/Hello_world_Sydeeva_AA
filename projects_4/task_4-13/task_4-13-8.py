N = int(input("Введите размер массива N: "))

if N <= 0:
    print("Ошибка: N должно быть > 0!")
else:
    A = []
    
    count = 0
    i = 1
    while i <= N:
        element = float(input(f"Введите элемент A[{i}]: "))
        A.append(element)
        
        if element > 0:
            count = count + 1
        
        i = i + 1
    
    print(f"Массив: {A}")
    print(f"Количество положительных чисел в массиве: {count}")