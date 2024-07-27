# Бинарный поиск - на входе получает отсортированный список элементов.
# Если элемент присутствует в списке, бинарный поиск возвращает его позицию.
# Если не присутствует, возвращает NULL
# Сложность - О(log n) - для обработки списка из 128 элементов требуется 7 операций

def binary_search(spisok: list[int], elem: int) -> int | None:
    low = 0
    high = len(spisok) - 1

    while low <= high:
        mid = int((low + high) / 2)
        guess = spisok[mid]
        if guess == elem:
            return mid
        elif guess > elem:
            high = mid - 1
        else:
            low = mid + 1
    return None


# print(binary_search(spisok=[1, 2, 3, 5, 7, 10], elem=9))

# --------------------------------------------------------------------------------------------------------------------
# Сортировка выбором
# Сложность - О(n*n) - поиск наименьшего объекта в списке (О(n)) n раз

# Функция поиска индекса наименьшего элемента в списке
def find_smallest(spisok: list[int]) -> int:
    smallest = spisok[0]
    smallest_index = 0
    for i in range(1, len(spisok)):
        if spisok[i] < smallest:
            smallest = spisok[i]
            smallest_index = i
    return smallest_index


# Функция сортировки выбором
def selection_sort(spisok: list[int]) -> list[int]:
    sorted_spisok = []
    while spisok:
        smallest_index = find_smallest(spisok)
        sorted_spisok.append(spisok.pop(smallest_index))

    return sorted_spisok


# print(selection_sort([1, 4, 8, 3, 4, 0]))

# --------------------------------------------------------------------------------------------------------------------
# Рекурсия - вызов функции самой себя. Реалзиована за счет стека.
# Каждый вызов функции интерпретатор сохраняет вызов в памяти, и, после вызова всех фунций,
# приступает к выполнению сверху вниз
# Временная сложность зависит от количества вызовов функций за раз.
#   Факториал вызывает одну функцию, временная сложность - О(n),
#   Число фибоначчи вызывает две функции, временная сложность О(2^n)

def countdown(start: int) -> str | int:
    next_int = start - 1
    print(next_int)
    if next_int == 0:
        return 'end'
    else:
        return countdown(next_int)


# print(countdown(45))

def fact(x: int):
    if x == 1:
        return x
    else:
        return fact(x - 1) * x


# print(fact(998))


# --------------------------------------------------------------------------------------------------------------------
# Разделяй и властвуй - рекурсивный метод решения задач. Два шага:
#   1. Определяется базовый случай - для ф-ии ниже это пустой список
#   2. Задача сокращается до тех пор, пока не будет сведена к базовому случаю - для ф-ии ниже это отбрасывание эл-та
#   из списка
def rekurs_sum(spisok: list[int]) -> int:
    if spisok:
        return spisok[0] + rekurs_sum(spisok[1:])
    else:
        return 0


# print(rekurs_sum([4, 2, 5, 1, 2, 4]))


def rekurs_len(spisok: list[int]) -> int:
    if spisok:
        return 1 + rekurs_len(spisok[1:])
    else:
        return 0


# print(rekurs_len([4, 2, 5, 1, 2, 4]))


def find_biggest(spisok: list[int]) -> int:
    if len(spisok) == 2:
        return spisok[0] if spisok[0] > spisok[1] else spisok[1]
    else:
        sub_max = find_biggest(spisok[1:])
        return spisok[0] if spisok[0] > sub_max else sub_max


# print(find_biggest([4, 2, 5, 1, 2, 4, 332]))


# --------------------------------------------------------------------------------------------------------------------
# Быстрая сортировка - алгоритм сортировки на основе метода "разделяй и властвуй".
# Алгоритмическая сложноcть - O(n*log(n)). В худшем случае, когда опорный эл-т максимальный или минимальный,
# сложность n^2

def quick_sort(spisok: list[int]) -> list[int]:
    if len(spisok) < 2:
        return spisok
    else:
        base_elem = spisok[len(spisok) // 2]
        left_part = []
        middle_part = []
        right_part = []
        for elem in spisok:
            if elem < base_elem:
                left_part.append(elem)
            elif elem == base_elem:
                middle_part.append(elem)
            elif elem > base_elem:
                right_part.append(elem)
        return quick_sort(left_part) + middle_part + quick_sort(right_part)


# print(quick_sort([2, 5, 3, 1, 8, 4, 1]))

# --------------------------------------------------------------------------------------------------------------------
# Хэш-таблица - объединение хэш-функции и массива
# Алгоритмическая сложность - О(1). В худшем случае, когда данные распределены неравномерно (неправильно подобрана хэш-
# -функция), сложность О(n).
# Важно не допускать наполненность хэш-таблицы (все эл-ты таблицы / количество ячеек) больше 1.

# --------------------------------------------------------------------------------------------------------------------
# Граф - моделирует набор связей

graph = {}

graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []

# print(graph)

# --------------------------------------------------------------------------------------------------------------------
# Поиск в ширину - алгоритм поиска по графу (позволяет определить существует ли путь из A в B).
# Находит путь с минимальным кол-вом сегментов.
# Сложность - O(V+E), где V - количество вершин,
# E - количество ребер (связей в графе).


from collections import deque


def is_seller(name: str) -> bool:
    if name[-1] == 'pp':
        return True


def bfs(name: str) -> str:
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            print(person)
            searched.append(person)
            if is_seller(person):
                return f'{person} is a mango-seller'
            else:
                search_queue += graph[person]
    return 'There"s no mango sellers'


# print(bfs('you'))


# --------------------------------------------------------------------------------------------------------------------
# Алгоритм Дейкстры - алгоритм поиска кратчайшего пути во взвешенном графе (граф, в котором ребрам присваивается вес).
# 1. Найти узел с наименьшей стоимостью
# 2. Проверить, существует ли более дешевый путь к соседям этого узла и, если существует, обновить их стоимость
# 3. Повторять, пока это не будет сделано для всех усзлов графа\
# 4. Вычислить итоговый путь


graph = {}
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2
graph['a'] = {}
graph['a']['fin'] = 1
graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] = 5
graph['fin'] = {}

infinity = float('inf')
costs = {}
costs['a'] = 6
costs['b'] = 2
costs['fin'] = infinity

parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None

processed = []


def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


def deykstra_alg():
    node = find_lowest_cost_node(costs)
    while node is not None:
        cost = costs[node]
        neighbours = graph[node]
        for n in neighbours.keys():
            new_cost = cost + neighbours[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs)
        print(costs)
        print(parents)


# deykstra_alg()


# --------------------------------------------------------------------------------------------------------------------
# Жадные алгоритмы - на каждом шаге выбирают локально-оптимальное решение.

states_needed = {'mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'}

stations = {}
stations['kone'] = {'id', 'nv', 'ut'}
stations['ktwo'] = {'id', 'wa', 'mt'}
stations['kthree'] = {'or', 'nv', 'ca'}
stations['kfour'] = {'nv', 'ut'}
stations['kfive'] = {'ca', 'az'}

final_stations = set()

while states_needed:
    best_station = None
    states_covered = set()
    for station, states_for_station in stations.items():
        covered = states_needed & states_for_station
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered

    states_needed -= states_covered
    final_stations.add(best_station)

# print(final_stations)



# --------------------------------------------------------------------------------------------------------------------
# Сортировка слиянием - сложность O(n^2).