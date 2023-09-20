x = input("Введите число: ")
list1 = list()
list2 = list()
for i in range(len(x)):
    if int(x[i]) % 2 == 0:
        list1.append(x[i])
    else:
        list2.append(x[i])
print("Чётные: ", list1,"Нечетные: ", list2)

x = int(input("Введите число: "))
y = int(input("Введите число: "))
if x > y:
    print("Наибольшее:", x)
else:
    print("Наибольшее:", y)

a = int(input("Введите число: "))
b = int(input("Введите число: "))
c = int(input("Введите число: "))
if 1<a<3 or 1<b<3 or 1<c<3:
    if 1<a<=3:
        print(a, "Подходит")
    elif 1<b<=3:
        print(b, "Подходит")
    elif 1<c<=3:
        print(c, "Подходит")
    else:
        print("No")

a = int(input("Введите сторону: "))
b = int(input("Введите сторону: "))
c = int(input("Введите сторону: "))
p = (a+b+c)/2
s = (p*((p-a)*(p-b)*(p-c)))**(1/2)
print(s)