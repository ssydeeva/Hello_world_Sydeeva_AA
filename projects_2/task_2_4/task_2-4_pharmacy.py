quantity = int(input("Введите общее количество произведенных капсул: "))
capacity = int(input('Введите количество капсул в одной упаковке: '))
count = quantity // capacity
overtime = quantity % capacity
print(f'--- Отчет фасовочного цеха ---\nПолных упаковок:\t{count}\nОстаток капсул:\t{overtime}')