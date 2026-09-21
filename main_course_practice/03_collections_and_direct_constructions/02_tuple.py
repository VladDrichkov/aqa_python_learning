import copy


def main():
    # data = (["login"], "passed")
    #
    # # data[0] = ["payment"]
    #
    # a = (["login"], 200)
    # # b = a #tuple(a)
    # b = copy.deepcopy(a)
    #
    # print(b is a)
    #
    # a = (1, 2)
    # a = a + (3,)
    # print(a)
    #
    # matrix = [[]] * -1
    # print(matrix)
    #
    # data = ([1, 2],)
    #
    # try:
    #     data[0] += [3]
    # except TypeError:
    #     pass
    # # data = [1, 2] + [3]
    # print(data)
    #
    # data = {"login": 200, "payment": 500}
    #
    # a, b = data
    # print(a)
    # print(b)

    #
    # data = (1, 2, 3)
    #
    # del data

    # data = [1, 2, 3]
    #
    # print(data[:] is data)
    #
    # data = (1, 2, 3)
    #
    # data += [4, 5]

    data = tuple("login")
    data = tuple(200)
    print(data)

if __name__ == '__main__':
    main()
