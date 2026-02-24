pH = float(input("Введите значение pH: "))
if pH < 7:
   print("Среда кислая")
elif pH == 7:
    print("Среда нейтральная")
else: #pH > 7:
    print("Среда щелочная")