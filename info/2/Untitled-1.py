f = open("result.txt", "w", encoding="utf-8")
print('Имя:\tАлександра\nФамилия:\tСыдеева\nВозраст:\t21\nГород:\tСанкт-Петербург\nИнтересы:\tВолейбол', file=f)
f.close()