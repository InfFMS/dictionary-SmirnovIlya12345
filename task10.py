# Нужно считать файл parameters.txt. 
# Это файл с настройками расчетной модели.
# Формат в файле следующий первое слово в строке - это ключ, 
# потом после пробела - значение (может быть строкой, числом, или набором чисел),
# все, что после символа "//" это комментарий  должно игнорироваться.
# Реализуйте считывание значений из файла и запись этих значений в словарь.
f=open('parameters.txt', 'r', encoding='utf-8')
lines=[line for line in f]
a=0
b=''
my_dict={}
for j in range(len(lines)):
    a+=len(lines[j])
    for k in range(len(lines[j]) - 1):
        if lines[j][k:k+2:] == '//':
            break
        else:
            b+=(lines[j][k])
    b+=' '
b=b.split(' ')
c=[]
print(type(b))
for i in range(len(b)):
    if b[i]!='' and b[i]!=' ':
        c.append(b[i])
for i in range(len(c)//2):
    my_dict[c[i*2]] = c[i*2+1]
print(my_dict)
