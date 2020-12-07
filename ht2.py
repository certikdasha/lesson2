print ('Введите 3 разных числа!')
a = int(input('Введите а: '))
b = int(input('Введите b: '))
c = int(input('Введите с: '))


# print ('a > b' if a > b else 'a =< b')


if a > b and a > c:
    print ('a наибольшее!')
elif b > a and b > c:
    print ('b наибольшее!')
else:
    print ('с наибольшее!')



