#5.1[26]: Напишите рекурсивную функцию для возведения числа a в степень b. Разрешается использовать только операцию умножения. Циклы использовать нельзя
#Примеры/Тесты:
#<function_name>(2,0) -> 1
#<function_name>(2,1) -> 2
#<function_name>(2,3) -> 8
#<function_name>(2,4) -> 16
def degree (num, deg):
    if deg == 0:
        return 1
    else:
        return num*degree(num,deg-1)

number = int(input('Введите число: '))
degr = int(input('Введите степень: '))
print (f'Число {number} в степени {degr} равняется {degree (number, degr)}')