# Зад 1
number = int(input('Введите число:'))
isNature = True
while isNature:
    if number > 0:
        break
    else:
        number = int(input('Введите натуральное число:'))
sum=0
remainder=0
while number>=1:
    remainder=number%10
    if remainder % 2 == 0:
        sum+=remainder
    number //=10
if sum > 0:
    print(f'Сумма чётных цифр равна {sum}')
else:
    print('0')

# зад 3
# my_list = [12, 511, 'Python', 311, 122, 'love']
# for i in range(len(my_list)):
#     if isinstance(my_list[i], int):
#         if my_list[i] % 2 == 0:
#             number = my_list[i]
#             sum = 0
#             while number > 0:
#                 digit = number % 10
#                 sum += digit
#                 number //= 10
#             my_list[i] = sum
#
#         else:
#             my_list[i] = 1
#
# print(my_list)

# зад 2
# s = input("Введите строку:")
# count = 0
# count2 = 0
# space = ' '
# vowels = set("aeiou")
# for letter in s:
#     if letter in vowels:
#         count += 1
#     elif letter == ' ':
#         continue
#     else:
#         count2 +=1
# print("Количество гласных равно:")
# print(count)
# print("Количество согласных равно:")
# print(count2)


# зад 4
# my_dict = {'a': 12, 'b': 13, 'c': 56, 'd': 400, 'e': 58, 'f': 20}
# min_value = min(my_dict.values())
# smallest_values = []
# for key, value in my_dict.items():
#     if value == min_value:
#         smallest_values.append(key)
# print("Три ключа с самыми маленькими значениями:")
# print(smallest_values)


# зад 6
# my_tuple = (10, 5, 20, 15, 30)
# max_element = max(my_tuple)
# index_of_max = my_tuple.index(max_element)
# print(f"Максимальный элемент {max_element} находится по индексу {index_of_max}")


# Зад 5
# toys = {
#     'Мяч': ['Детский мяч для игры', 10.99, 50],
#     'Кукла': ['Кукла с аксессуарами', 15.99, 30],
#     'Конструктор': ['Строительный конструктор', 19.99, 40],
#     'Пазл': ['Пазл с изображением животных', 12.49, 20],
#     'Велосипед': ['Детский велосипед', 89.99, 10]
# }
#
# while True:
#     print("\nМеню:")
#     print("1. Просмотр описания")
#     print("2. Просмотр цены")
#     print("3. Просмотр количества")
#     print("4. Вся информация")
#     print("5. Покупка")
#     print("6. До свидания")
#
#     choice = input("Введите номер пункта меню: ")
#
#     if choice == '1':
#         toy_name = input("Введите название игрушки: ")
#         if toy_name in toys:
#             print(f"Описание: {toys[toy_name][0]}")
#         else:
#             print("Такой игрушки нет в магазине.")
#
#     elif choice == '2':
#         toy_name = input("Введите название игрушки: ")
#         if toy_name in toys:
#             print(f"Цена: {toys[toy_name][1]}")
#         else:
#             print("Такой игрушки нет в магазине.")
#
#     elif choice == '3':
#         toy_name = input("Введите название игрушки: ")
#         if toy_name in toys:
#             print(f"Количество: {toys[toy_name][2]}")
#         else:
#             print("Такой игрушки нет в магазине.")
#
#     elif choice == '4':
#         print("Вся информация о товарах:")
#         for toy_name, info in toys.items():
#             print(f"{toy_name}: {info[0]}, Цена: {info[1]}, Количество: {info[2]}")
#
#     elif choice == '5':
#         print("Покупка игрушек:")
#         total_price = 0
#         while True:
#             toy_name = input("Введите название игрушки (n - завершить покупки): ")
#             if toy_name == 'n':
#                 break
#             if toy_name in toys:
#                 quantity = int(input("Введите количество: "))
#                 if quantity <= toys[toy_name][2]:
#                     price = toys[toy_name][1] * quantity
#                     total_price += price
#                     toys[toy_name][2] -= quantity
#                 else:
#                     print("Недостаточно товара в магазине.")
#             else:
#                 print("Такой игрушки нет в магазине.")
#
#         print(f"Общая стоимость покупки: {total_price}")
#
#     elif choice == '6':
#         print("До свидания!")
#         break
#
#     else:
#         print("Некорректный выбор. Пожалуйста, выберите пункт из меню.")