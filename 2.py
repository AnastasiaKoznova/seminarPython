#Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
#Пример: Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

n=int(input('Введите натуральное число'))
result={}
for key in range (1, n+1):
    result[key]= key*3+1

print(result)
