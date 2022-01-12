##
## EPITECH PROJECT, 2022
## B-MAT-500-RUN-5-1-307multigrains-tom.hermann
## File description:
## siplexe
##

from sys import int_info
from typing import List
from math import inf


def init_matrice(ressources, prices):
    simplexe = [
        [1, 0, 1, 0, 2],
        [1, 2, 0, 1, 0],
        [2, 1, 0, 1, 0],
        [0, 0, 3, 1, 2],
        [-x for x in prices] + ([0] * 5)
    ]
    for i in range(0, 4):
        for j in range(0, 4):
            simplexe[i].append(1 if j == i else 0)
        simplexe[i].append(ressources[i])
    return simplexe

def find_pivot(matrice: List[List[int]]):
    values = matrice[-1][:5]
    min_value = min(values)
    if min_value >= 0:
        return True, 0, 0
    else:
        pivot_x, pivot_y = values.index(min_value), 0
    min_value = inf
    for i in range(len(matrice) - 1):
        if matrice[i][-1]:
            if matrice[i][pivot_x] > 0 and min_value > (matrice[i][-1] / matrice[i][pivot_x]) > 0:
                pivot_y = i
                min_value = matrice[i][-1] / matrice[i][pivot_x]
        elif min_value > matrice[i][pivot_x] > 0:
            pivot_y = i
            min_value = matrice[i][-1] / matrice[i][pivot_x]
    return False, pivot_y, pivot_x

def pivot_matrice(matrice: List[List[int]], pivot_y, pivot_x):
    pivot_value = matrice[pivot_y][pivot_x]

    matrice[pivot_y] = [x / pivot_value for x in matrice[pivot_y]]
    for i in range(len(matrice)):
        if i == pivot_y:
            continue
        pivot_coef = matrice[i][pivot_x]
        for j in range(len(matrice[0])):
            matrice[i][j] -= pivot_coef * matrice[pivot_y][j]
    return matrice

def display_res(matrice, simplexe, prices):
    total = 0
    res = [0] * 5

    for i in range(len(simplexe)):
        if simplexe[i] == -1:
            continue
        res[simplexe[i]] = matrice[i][-1]
        total += matrice[i][-1] * prices[simplexe[i]]

    for resource, value, price in zip(["Oat", "Wheat", "Corn", "Barley", "Soy"], res, prices):
        print("{}: {} units at ${:.0f}/units".format(resource, "{:.2f}".format(value) if value != 0 else 0, price))
    print()
    print("Total production value: ${:.2f}".format(total))

def simplexe_methode(resources, prices):
    matrice = init_matrice(resources, prices)
    res = [-1] * 4
    while True:
        finish, pivot_y, pivot_x = find_pivot(matrice)
        if finish:
            break
        matrice = pivot_matrice(matrice, pivot_y, pivot_x)
        res[pivot_y] = pivot_x
    display_res(matrice, res, prices)