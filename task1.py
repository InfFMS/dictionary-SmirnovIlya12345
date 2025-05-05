# Напишите программу, которая получает на вход две строки, и формирует из них словарь. 
# Ключами служат слова из первой строки, значениями – целые числа из второй.
# Пример ввода
# яблоки сливы груши персики манго киви апельсины
# 34 56 23 89 55 32 11
print('Enter string 1; enter qwerty to finish')
all=[]
dict1=dict()
c=0
while True:
    g=input()
    if g=='qwerty':
        break
    all.append(g)
    c+=1
    print(c)
print('Enter string 2')
for i in range(c):
    dict1[all[i]]=int(input())
print(dict1)
