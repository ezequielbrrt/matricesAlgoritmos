#! /usr/bin/python
# -*- coding: utf-8 -*-

def new_m(p, q): # crea una matriz con ceros
    matrix = [[0 for row in range(p)] for col in range(q)]
    return matrix
def split(matrix): 
    a = matrix
    b = matrix
    c = matrix
    d = matrix
    while(len(a) > len(matrix)/2):
        a = a[:len(a)/2]
        b = b[:len(b)/2]
        c = c[len(c)/2:]
        d = d[len(d)/2:]
    while(len(a[0]) > len(matrix[0])/2):
        for i in range(len(a[0])/2):
            a[i] = a[i][:len(a[i])/2]
            b[i] = b[i][len(b[i])/2:]
            c[i] = c[i][:len(c[i])/2]
            d[i] = d[i][len(d[i])/2:]
    return a,b,c,d
def add_m(a, b):
    if type(a) == int:
        d = a + b
    else:
        d = []
        for i in range(len(a)):
            c = []
            for j in range(len(a[0])):
                c.append(a[i][j] + b[i][j])
            d.append(c)
    return d
def sub_m(a, b):
    if type(a) == int:
        d = a - b
    else:
        d = []
        for i in range(len(a)):
            c = []
            for j in range(len(a[0])):
                c.append(a[i][j] - b[i][j])
            d.append(c)
    return d
def mul_matrices(a, b, q):
    # caso base
    if q == 1:
        d = [[0]]
        d[0][0] = a[0][0] * b[0][0]
        return d
    else:
        #a    b   c    d 
        a11, a12, a21, a22 = split(a)
        #e    f    g    h
        b11, b12, b21, b22 = split(b)
        ae = mul_matrices(a11, b11, q/2)
        bg = mul_matrices(a12, b21, q/2)
        af = mul_matrices(a11, b12, q/2)
        bh = mul_matrices(a12, b22, q/2)
        ce = mul_matrices(a21, b11, q/2)
        dg = mul_matrices(a22, b21, q/2)
        cf = mul_matrices(a21, b12, q/2)
        dh = mul_matrices(a22, b22, q/2)
        c11 = add_m(ae,bg)
        c12 = add_m(af, bh)
        c21 = add_m(ce, dg)
        c22 = add_m(cf, dh)
        c = new_m(len(c11)*2,len(c11)*2)
        for i in range(len(c11)):
            for j in range(len(c11)):
                c[i][j]                   = c11[i][j]
                c[i][j+len(c11)]          = c12[i][j]
                c[i+len(c11)][j]          = c21[i][j]
                c[i+len(c11)][j+len(c11)] = c22[i][j]

        return c
