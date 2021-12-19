# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 01:14:12 2021

@author: German
"""

"""Найти сумму элементов матрицы, лежащих выше главной диагонали"""


matrix=[[1, 4, 6],
        [6, 3, 8],
        [2, 9, 4]]
sum=0
for i in range(0, len(matrix)):
    for j in range(i+1, len(matrix[i])):
        sum+=matrix[i][j]

print(sum)