"""
Є декілька мережевих кабелів різної довжини,
їх потрібно об'єднати по два за раз в один кабель, використовуючи з'єднувачі,
 у порядку, який призведе до найменших витрат. 
 Витрати на з'єднання двох кабелів дорівнюють їхній сумі довжин, 
 а загальні витрати дорівнюють сумі з'єднання всіх кабелів.
Завдання полягає в тому, щоб знайти порядок об'єднання, який мінімізує загальні витрати.
"""

import heapq

cables = [3, 10, 4, 8, 1, 2, 5, 8]


def conn_by_heap(cables):
    heapq.heapify(cables)
    total_cost = 0

    while len(cables) > 1:
        # get two minimum length cable
        print("Cabels:", cables, "\n connection....")
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        # calculate total cost
        cost = first + second
        total_cost += cost
        connection = "=" * first + "*" + "=" * second
        num_line = int(first/2) * " " + str(first) + int(first/2) * " " +\
             int(second/2) * " " + str(second) + int(second/2) * " "
        print(num_line)
        print(connection , total_cost)
        heapq.heappush(cables, cost)
    return total_cost


print(f"Total connection cost: {conn_by_heap(cables)}")
