volume = float(input('Введите общий объем: '))
salt_mass = volume * 0.009
with open("recipe.txt", "w", encoding="utf-8") as recipe: recipe.write(f'ОТЧЕТ ПО ПРИГОТОВЛЕНИЮ:\n{"-" * 23}\nОбщий объем:\t{volume} мл.\nМасса соли:\t{salt_mass:.2f} Г.\nОбъем воды:\t{salt_mass:.2f} мл.')