# Задача 1. Пропуск в кинотеатр

age = 13
has_adult = True

if age >= 18 or (age >= 14 and has_adult):
    print("Доступ разрешен")
else:
    print("Вход запрещен")


# Задача 2. Проверка логина
print("=========== # Задача 2. Проверка логина =================")

username = "admin"
password = "12345"

username_input = input("введите логин: ")
password_input = input("введите пароль: ")

if username_input == username and password_input == password:
    print("Вход выполнен")
elif username_input == username:
     print("Неверный пароль")
else:
    print("Пользователь не найден")

# if username_input == username:
#     if password_input == "12345":
#         print("Вход выполнен")
#     else:
#         print("Неверный пароль")
# else:
#     print("Пользователь не найден")

# Задача 3. Угадай число

print("=========== # Задача 3. Угадай число =================")

hidden = 7

user_number = int(input("введите число: "))

if user_number > hidden:
    print("Слишком много")
if user_number < hidden:
    print("Слишком мало")
else:
    print("Угадал")
