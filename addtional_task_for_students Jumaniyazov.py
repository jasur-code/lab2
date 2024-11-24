# TODO Написать свою реализацию функции для подсчёта числа вхождения элементов в список
def my_count(l: list, item):

    total = 0
    for el in l:
        if el == item:
            total += 1

    return total
# Пример использования:
sample_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
print(my_count(sample_list, 'banana'))
