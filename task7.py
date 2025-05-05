# Даны два словаря. Напишите программу, которая объединит эти словари. 
# Если ключи встречаются в обоих исходных словарях, значения, 
# которые хранятся по этим ключам складываются.
# Пример:
# Первый словарь: {'a': 100, 'b': 200, 'c':300}
# Второй словарь: {'a': 300, 'b': 200, 'd':400}
# Результат: {'a': 400, 'b': 400, 'd': 400, 'c': 300}
dict1={'a': 100, 'b': 200, 'c':300}
dict2={'a': 300, 'b': 200, 'd':400, 'e':300}
dict3={}
for i in range(len(dict1)):
    c=0
    for j in range(0, len(dict2)):
        if list(dict1)[i]==list(dict2)[j]:
            dict3[list(dict1)[i]]=list(dict1.values())[i]+list(dict2.values())[j]
            c=1
            break
    if c==0:
        dict3[list(dict1)[i]]=list(dict1.values())[i]
for i in range(len(dict2)):
    c=0
    for j in range(0, len(dict1)):
        if list(dict2)[i]==list(dict1)[j]:
            c=1
            break
    if c==0:
        dict3[list(dict2)[i]]=list(dict2.values())[i]
print(dict3)
