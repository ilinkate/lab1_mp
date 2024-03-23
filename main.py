# вариант№ 7: в, д, е:
# Задание: Массив данных о сборной олимпийской команде: ФИО,  возраст, рост, вес, вид спорта
# (сравнение по полям – вид  спорта, ФИО, возраст)
# в)Сортировка простыми вставками
# д)Пирамидальная сортировка
# е)Быстрая сортировка
# ссылка, откуда был взят набор данных: https://www.kaggle.com/datasets/bhanupratapbiswas/olympic-data

import pandas as pd
import time
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv('/Users/ekaterina/Documents/учёба/методы программирования/lab1_mp/dataset_olympics.csv')  # main dataset
df = df.drop(["ID", "Sex", "Team", "NOC", "Year", "Season", "City", "Event", "Medal", "Games"], axis=1)

df_1 = df[:1000]
df_1.to_csv("d_1.csv")

df_2 = df[1000:3100]
df_2.to_csv("d_2.csv")

df_3 = df[3100:6300]
df_3.to_csv("d_3.csv")

df_4 = df[6300:10600]
df_4.to_csv("d_4.csv")

df_5 = df[10600:16000]
df_5.to_csv("d_5.csv")

df_6 = df[16000:22500]
df_6.to_csv("d_6.csv")

df_7 = df[22500:30100]
df_7.to_csv("d_7.csv")


class OBJ:
    def __init__(self, name: str, sport: str, age: float, height: float, weight: float):
        self.name = name
        self.sport = sport
        self.age = age
        self.height = height
        self.weight = weight
# >
    def __gt__(self, other):
        if self.name > other.name:
            return True
        elif self.name < other.name:
            return False
        else:
            if self.sport > other.sport:
                return True
            elif self.sport < other.sport:
                return False
            else:
                if self.age > other.age:
                    return True
                else:
                    return False
# <
    def __lt__(self, other):
        if self.name < other.name:
            return True
        elif self.name > other.name:
            return False
        else:
            if self.sport < other.sport:
                return True
            elif self.sport > other.sport:
                return False
            else:
                if self.age < other.age:
                    return True
                else:
                    return False
# >=
    def __ge__(self, other):
        if self.name > other.name:
            return True
        elif self.name < other.name:
            return False
        else:
            if self.sport > other.sport:
                return True
            elif self.sport < other.sport:
                return False
            else:
                if self.age > other.age:
                    return True
                elif self.age < other.age:
                    return False
                else:
                    return True
# <=
    def __le__(self, other):
        if self.name < other.name:
            return True
        elif self.name > other.name:
            return False
        else:
            if self.sport < other.sport:
                return True
            elif self.sport > other.sport:
                return False
            else:
                if self.age < other.age:
                    return True
                elif self.age > other.age:
                    return False
                else:
                    return True


df_1 = pd.read_csv('d_1.csv')
fin_1 = []
l = len(df_1)
for i in range(l):
    fin_1.append(OBJ(df_1['Name'][i], df_1['Sport'][i], df_1['Age'][i], df_1['Height'][i], df_1['Weight'][i]))

df_2 = pd.read_csv('d_2.csv')
fin_2 = []
l = len(df_2)
for i in range(l):
    fin_2.append(OBJ(df_2['Name'][i], df_2['Sport'][i], df_2['Age'][i], df_2['Height'][i], df_2['Weight'][i]))

df_3 = pd.read_csv('d_3.csv')
fin_3 = []
l = len(df_3)
for i in range(l):
    fin_3.append(OBJ(df_3['Name'][i], df_3['Sport'][i], df_3['Age'][i], df_3['Height'][i], df_3['Weight'][i]))

df_4 = pd.read_csv('d_4.csv')
fin_4 = []
l = len(df_4)
for i in range(l):
    fin_4.append(OBJ(df_4['Name'][i], df_4['Sport'][i], df_4['Age'][i], df_4['Height'][i], df_4['Weight'][i]))

df_5 = pd.read_csv('d_5.csv')
fin_5 = []
l = len(df_5)
for i in range(l):
    fin_5.append(OBJ(df_5['Name'][i], df_5['Sport'][i], df_5['Age'][i], df_5['Height'][i], df_5['Weight'][i]))

df_6 = pd.read_csv('d_6.csv')
fin_6 = []
l = len(df_6)
for i in range(l):
    fin_6.append(OBJ(df_6['Name'][i], df_6['Sport'][i], df_6['Age'][i], df_6['Height'][i], df_6['Weight'][i]))

df_7 = pd.read_csv('d_7.csv')
fin_7 = []
l = len(df_7)
for i in range(l):
    fin_7.append(OBJ(df_7['Name'][i], df_7['Sport'][i], df_7['Age'][i], df_7['Height'][i], df_7['Weight'][i]))

final = [fin_1, fin_2, fin_3, fin_4, fin_5, fin_6, fin_7]
final_1 = final
final_2 = final
final_3 = final

x = []
for i in final:
    x.append(len(i))
print(x)


# СОРТИРОВКА ПРОСТЫМИ ВСТАВКАМИ
def insertion_sort(nums):
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = item_to_insert


insert_times = []
for (i, fin) in enumerate(final_1):
    tmp = fin[:]
    start = time.time()
    insertion_sort(tmp)
    insert_times.append(time.time() - start)
    with open(f'insertion_{i+1}.txt', 'w') as f:
        for elem in tmp:
            f.write(f'{elem.name} {elem.sport} {elem.age} {elem.height} {elem.weight}\n')
print("Время сортировки простыми вставками:",insert_times)


# ПИРАМИДАЛЬНАЯ СОРТИРОВКА
def heapify(nums, heap_size, root_index):
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2
    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child


    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child

    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        heapify(nums, heap_size, largest)

def heap_sort(nums):
    n = len(nums)
    for i in range(n, -1, -1):
        heapify(nums, n, i)
    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)


heap_times = []
for (i, fin) in enumerate(final_2):
    tmp = fin[:]
    start = time.time()
    heap_sort(tmp)
    heap_times.append(time.time() - start)
    with open(f'heap_{i+1}.txt', 'w') as f:
        for elem in tmp:
            f.write(f'{elem.name} {elem.sport} {elem.age} {elem.height} {elem.weight}\n')
print("Время для пирамидальной сортировки:", heap_times)


# БЫСТРАЯ СОРТИРОВКА
def partition(nums, low, high):
    point = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < point:
            i += 1

        j -= 1
        while nums[j] > point:
            j -= 1

        if i >= j:
            return j

        nums[i], nums[j] = nums[j], nums[i]


def quick_sort(nums):
    def _quick_sort(items, low, high):
        if low < high:
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)


quick_times = []
for (i, fin) in enumerate(final_3):
    tmp = fin[:]
    start = time.time()
    quick_sort(tmp)
    quick_times.append(time.time() - start)
    with open(f'quick_{i+1}.txt', 'w') as f:
        for elem in tmp:
            f.write(f'{elem.name} {elem.sport} {elem.age} {elem.height} {elem.weight}\n')
print("Время для быстрой сортировки:", quick_times)

# Прологарифмирование результатов
log_heap_times = np.log(heap_times)
log_insertion_times = np.log(insert_times)
log_quick_times = np.log(quick_times)

# Построение графиков
plt.plot(x, log_heap_times, label='пирамидальная')
plt.plot(x, log_insertion_times, label='простые вставки')
plt.plot(x, log_quick_times, label='быстрая')

plt.legend()
plt.show()

