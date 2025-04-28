# Имеется следующий словарь:
numbers = {'dict1': [11, 20, 30, 17, 6, 24, 90, 15, 17],
          	'dict2': [21, 33, 40, 10, 29, 31, 90, 12],
          	'dict3': [52, 34, 20, 21, 44, 22, 10, 87],
          	'dict4': [22, 54, 29, 21, 70, 88, 99, 34],
          	'dict5': [21, 40, 29, 21, 19, 32, 68, 77],
          	'dict6': [14, 60, 70, 10, 55, 61, 84, 99],
          	'dict7': [45, 80, 12, 23, 42, 22, 37, 90],
          	'dict8': [13, 14, 15, 26, 48, 92, 36, 11],
          	'dict9': [12, 70, 18, 28, 18, 28, 53, 91],
          	'dict10': [29, 79, 18, 28, 18, 28, 32, 55]}
# Напишите программу, которая удалит из значений словаря все четные числа.
list1=[]
list2=[]
list3=[]
list4=[]
list5=[]
list6=[]
list7=[]
list8=[]
list9=[]
list10=[]
for i in range(len(numbers['dict1'])):
	if numbers['dict1'][i]%2==1:
		list1.append(numbers['dict1'][i])
for i in range(len(numbers['dict2'])):
	if numbers['dict2'][i]%2==1:
		list2.append(numbers['dict2'][i])
for i in range(len(numbers['dict3'])):
	if numbers['dict3'][i]%2==1:
		list3.append(numbers['dict3'][i])
for i in range(len(numbers['dict4'])):
	if numbers['dict4'][i]%2==1:
		list4.append(numbers['dict4'][i])
for i in range(len(numbers['dict5'])):
	if numbers['dict5'][i]%2==1:
		list5.append(numbers['dict5'][i])
for i in range(len(numbers['dict6'])):
	if numbers['dict6'][i]%2==1:
		list6.append(numbers['dict6'][i])
for i in range(len(numbers['dict7'])):
	if numbers['dict7'][i]%2==1:
		list7.append(numbers['dict7'][i])
for i in range(len(numbers['dict8'])):
	if numbers['dict8'][i]%2==1:
		list8.append(numbers['dict8'][i])
for i in range(len(numbers['dict9'])):
	if numbers['dict9'][i]%2==1:
		list9.append(numbers['dict9'][i])
for i in range(len(numbers['dict10'])):
	if numbers['dict10'][i]%2==1:
		list10.append(numbers['dict10'][i])
print(list1,list2,list3,list4,list5,list6,list7,list8,list9,list10,sep='\n')