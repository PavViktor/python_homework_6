# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

list_ = [2, 4, 7, 2, 5, 4, 5, 1, 10, 0]
minNum = int(input("Введите минимальное значение искомого диапазона: "))
maxNum = int(input("Введите максимальное значение искомого диапазона: "))
listIndex = []
for i in range(len(list_)):
    if minNum <= list_[i] <= maxNum:
        listIndex.append(i)
print(list_)
print(f"Индексы элементов списка, лежащих в диапазоне от {minNum} до {maxNum}: \n{listIndex}")