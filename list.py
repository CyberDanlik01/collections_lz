#Введём элементы последовательности
a = 0
b = 1
i = 0

#Список, в котором будет наша последовательность
l = list()
l.append(a)
l.append(b)

#Пользователь задаст последний элемент ряда
n = int(input("Введите количество членов ряда Фибоначи: "))

#Зададим цикл
for i in range (0, n-2):
    f = a + b 
    a = b
    b = f
    l.append(f)
print(l)

#Поменяем список:
for u in range (0, len(l)):
    if u % 2 == 0:
        l[u] = l[u]*2 
    else:
        l[u] = l[u]**2
print("Ваш новый список: ",l)

#Найдем медиану списка
medi = sum(l) / len(l)
county = 0

#Сравним элементы с ней
for k in range(0, len(l)):
    if l[k] > medi:
        county = county + 1

#Выведем
print('Минимальный элемент:', min(l))
print('Максимальный элемент:', max(l))
print('Длина списка:', len(l))
print('Медиана списка:', medi)
print('Количество элементов, больших медианы:', county)