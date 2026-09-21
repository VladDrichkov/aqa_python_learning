def main():
    input_result_1 = input("Введите имя друга 1: ")
    input_result_2 = input("Введите имя друга 2: ")
    input_result_3 = input("Введите имя друга 3: ")
    # print("Мои друзья: " + input_result_1 + ", " + input_result_2 + " и " + input_result_3 + ".")
    print("Мои друзья: ", end="")
    print(input_result_1, ", ", input_result_2, " и ", input_result_3, ".", sep="")


if __name__ == '__main__':
    main()
