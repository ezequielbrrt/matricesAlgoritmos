#! /usr/bin/python
# -*- coding: utf-8 -*-

def new_m(p, q): # crea matriz
    matrix = [[0 for row in range(p)] for col in range(q)]
    return matrix

def mul_matrices(a, b, q): # multiplica las dos matrices
    if len(a[0]) != len(b): 
        return "La matriz no es correcta"
    else:
        p_matrix = new_m(len(a), len(b[0]))
        for i in range(len(a)):
            for j in range(len(b[0])):
                for k in range(len(b)):
                    p_matrix[i][j] += a[i][k]*b[k][j]
    return p_matrix

