# Представить случайный список в обратном порядке. С использованием трех способов
# решения

# Список функций reverse()
# product = input("Введите название продуктов для покупки: ").split()
# print("Ваш список: \n", product)
#
# num_product = input("\nКакие продукты уже куплены?\n ").split()
# for num in num_product:
#     product.remove(num)
#
# print("\nОсталось купить: \n", product)
#
# active = input("\nВывести список в обратном порядке? (да\нет)")
# if(active == "да"):
#     product.reverse()
#     print(product)
# else:
#     print("Удачных покупок!!)")

# # Использование нарезки
# product = input("Введите название продуктов для покупки: ").split()
# print("Ваш список: \n", product)
#
# num_product = input("\nКакие продукты уже куплены?\n ").split()
# for num in num_product:
#     product.remove(num)
#
# print("\nОсталось купить: \n", product)
#
# active = input("\nВывести оставшиеся покупки в обратном порядке? (да\нет)")
# if(active == "да"):
#     product = product[::-1]
#     print(product)
# else:
#     print("Удачных покупок!!)")

# reversed()
# product = input("Введите название продуктов для покупки: ").split()
# print("Ваш список: \n", product)
#
# num_product = input("\nКакие продукты уже куплены?\n ").split()
# for num in num_product:
#     product.remove(num)
#
# print("\nОсталось купить: \n", product)
#
# active = input("\nВывести оставшиеся покупки в обратном порядке? (да\нет)")
# if(active == "да"):
#     product = list(reversed(product))
#     print(product)
# else:
#     print("Удачных покупок!!)")