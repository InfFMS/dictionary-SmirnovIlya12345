# Представьте, что вы шпионы)
# Придумайте шифр, в котором буквы заменяются на какие-то символы
# и реализуйте шифроватор и дешифровато
print("Enter a phrase")
s=input()
def to_numbers(s):
    a=[]
    for i in range(len(s)):
        if s[i]==' ':
            a.append(0)
        if s[i]=='a':
            a.append(1)
        if s[i]=='b':
            a.append(2)
        if s[i]=='c':
            a.append(3)
        if s[i]=='d':
            a.append(4)
        if s[i]=='e':
            a.append(5)
        if s[i]=='f':
            a.append(6)
        if s[i]=='g':
            a.append(7)
        if s[i]=='h':
            a.append(8)
        if s[i]=='i':
            a.append(9)
        if s[i]=='j':
            a.append(10)
        if s[i]=='k':
            a.append(11)
        if s[i]=='l':
            a.append(12)
        if s[i]=='m':
            a.append(13)
        if s[i]=='n':
            a.append(14)
        if s[i]=='o':
            a.append(15)
        if s[i]=='p':
            a.append(16)
        if s[i]=='q':
            a.append(17)
        if s[i]=='r':
            a.append(18)
        if s[i]=='s':
            a.append(19)
        if s[i]=='t':
            a.append(20)
        if s[i]=='u':
            a.append(21)
        if s[i]=='v':
            a.append(22)
        if s[i]=='w':
            a.append(23)
        if s[i]=='x':
            a.append(24)
        if s[i]=='y':
            a.append(25)
        if s[i]=='z':
            a.append(26)
    return a
def from_numbers(a):
    t=''
    for i in range(len(a)):
        if a[i]==0:
            t+=' '
        if a[i]==1:
            t+='a'
        if a[i]==2:
            t+='b'
        if a[i]==3:
            t+='c'
        if a[i]==4:
            t+='d'
        if a[i]==5:
            t+='e'
        if a[i]==6:
            t+='f'
        if a[i]==7:
            t+='g'
        if a[i]==8:
            t+='h'
        if a[i]==9:
            t+='i'
        if a[i]==10:
            t+='j'
        if a[i]==11:
            t+='k'
        if a[i]==12:
            t+='l'
        if a[i]==13:
            t+='m'
        if a[i]==14:
            t+='n'
        if a[i]==15:
            t+='o'
        if a[i]==16:
            t+='p'
        if a[i]==17:
            t+='q'
        if a[i]==18:
            t+='r'
        if a[i]==19:
            t+='s'
        if a[i]==20:
            t+='t'
        if a[i]==21:
            t+='u'
        if a[i]==22:
            t+='v'
        if a[i]==23:
            t+='w'
        if a[i]==24:
            t+='x'
        if a[i]==25:
            t+='y'
        if a[i]==26:
            t+='z'
    return t
def side_one(s):
    a2=to_numbers(s)
    for i in range(len(a2)):
        if i%4==0:
            a2[i]+=12
        if i%4==1:
            a2[i]+=5
        if i%4==2:
            a2[i]+=21
        if i%4==3:
            a2[i]+=9
    for i in range(len(a2)):
        if a2[i]>26:
            a2[i]=a2[i]-27
    print(from_numbers(a2))
    return from_numbers(a2)
def side_minus_one(s):
    a3=to_numbers(s)
    for i in range(len(a3)):
        if i%4==0:
            a3[i]+=15
        if i%4==1:
            a3[i]+=22
        if i%4==2:
            a3[i]+=6
        if i%4==3:
            a3[i]+=18
    for i in range(len(a3)):
        if a3[i]>26:
            a3[i]=a3[i]-27
    print(from_numbers(a3))
    return from_numbers(a3)
side_one(s)
side_minus_one(s)
side_minus_one(side_one(s))