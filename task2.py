# Напишите программу, которая получает на вход строку чисел, разделенных пробелами, и формирует словарь,
#  в котором ключами служат числа, а значениями – слово "четное" или "нечетное".
print("Enter some numbers separated by ' '")
arr=input().split(' ')
dic=dict()
for i in range(len(arr)):
    if int(arr[i])%2==0:
        dic[arr[i]]='even'
    else:
        dic[arr[i]]='odd'
print(dic)
