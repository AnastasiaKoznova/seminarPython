#Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
Number=int(input('Введите число:'))
result=[]
for degree in range(Number):
    result.append(str((-3)**degree))
print (",". join(result), end=".")


