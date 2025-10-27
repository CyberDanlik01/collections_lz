import matplotlib.pyplot as plt

#Моя функция: y = (x**4) + 6(x**2) + 15
x = []
y = []

# все x
for i in range(25):
    x.append(i)

#Найдем к ним y
for i in range(len(x)):
    y.append((x[i] ** 4) + 6 * (x[i] ** 2) + 15)

plt.plot(x, y) #График
plt.xlabel('Ось х') #Подпись для оси x
plt.ylabel('Ось y') #Подпись для оси y
plt.title('График') #Название
plt.show() #Вывод графика на экран
