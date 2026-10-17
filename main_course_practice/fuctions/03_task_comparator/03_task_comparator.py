
# Дан список пар «тест — сколько раз упал».
# Вывести по убыванию числа падений, а при равном числе — по алфавиту.

from functools import cmp_to_key

def compare_tests(a,b):
    if a[1] != b[1]:
        if a[1] < b[1]:
            return 1
        else:
            return -1
    else:
        if a[0] < b[0]:
            return -1
        elif a[0] > b[0]:
            return 1
        else:
            return 0

report = [("оплата", 5), ("вход", 12), ("корзина", 5)]


sorted_report = sorted(report, key=cmp_to_key(compare_tests))
print(sorted_report)

