from random import randint # Вводим рандом
fiku = 0
def selection_sort(n):  # создаем фунцию
    for i in range(len(n)): # Значение i соответствует кол-ву отсортированных значений
        l = i  # Исходно считаем наименьшим первый элемент
        for j in range(i + 1, len(n)): # Этот цикл перебирает несортированные элементы
            if n[j] < n[l]:
                l = j # Самый маленький элемент меняем с первым в списке
        n[i], n[l] = n[l], n[i]
        print(n) #выводим промежуточный результат
        fiku += 1
random = [] #создаем наш список
for i in range(100): #закидываем 100 случайных эл-ов
    random.append(randint(0, 1000000))
selection_sort(random)  #запускаем функцию с созданым списком
random.reverse() #переворачиваем список
print(random) #выводим список
print('кол-во сравнений выборкой:', fiku)

#теперь пузырьком

l = []
for i in range(100): #закидываем 100 случайных эл-ов
    l.append(randint(0, 1000000))
stop_flag = True
fikus = 0
while stop_flag is True:
    stop_flag = False
    for i in range (0, len(l)-1):
        if l[i] > l[i+1]:
            a = l[i+1]
            l[i+1] = l[i]
            l[i] = a
            stop_flag = True
            print(l)
            fikus += 1
l.reverse()
print(l)
print('кол-во сравнений пузырьком:', fikus)