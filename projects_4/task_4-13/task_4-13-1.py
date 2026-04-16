A = float(input("Введите первое число (A): "))
B = float(input("Введите второе число (B): "))
C = float(input("Введите третье число (C): "))
D = float(input("Введите четвёртое число (D): "))

min_value = A

if min_value > B:
    min_value = B

if min_value > C:
    min_value = C

if min_value > D:
    min_value = D

print(f"Минимальное из чисел {A}, {B}, {C}, {D} равно {min_value}")