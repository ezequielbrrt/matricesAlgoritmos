#! /usr/bin/python
# -*- coding: utf-8 -*-

def new_m(p, q):
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
        a11, a12, a21, a22 = split(a)
        b11, b12, b21, b22 = split(b)
        # p1 = (a11+a22) * (b11+b22)
        p1 = mul_matrices(add_m(a11,a22), add_m(b11,b22), q/2)
        # p2 = (a21+a22) * b11
        p2 = mul_matrices(add_m(a21,a22), b11, q/2)
        # p3 = a11 * (b12-b22)
        p3 = mul_matrices(a11, sub_m(b12,b22), q/2)
        # p4 = a22 * (b12-b11)
        p4 = mul_matrices(a22, sub_m(b21,b11), q/2)
        # p5 = (a11+a12) * b22
        p5 = mul_matrices(add_m(a11,a12), b22, q/2)
        # p6 = (a21-a11) * (b11+b12)
        p6 = mul_matrices(sub_m(a21,a11), add_m(b11,b12), q/2)
        # p7 = (a12-a22) * (b21+b22)
        p7 = mul_matrices(sub_m(a12,a22), add_m(b21,b22), q/2)
        # c11 = p1 + p4 - p5 + p7
        c11 = add_m(sub_m(add_m(p1, p4), p5), p7)
        # c12 = p3 + p5
        c12 = add_m(p3, p5)
        # c21 = p2 + p4
        c21 = add_m(p2, p4)
        # c22 = p1 + p3 - p2 + p6
        c22 = add_m(sub_m(add_m(p1, p3), p2), p6)
        c = new_m(len(c11)*2,len(c11)*2)
        for i in range(len(c11)):
            for j in range(len(c11)):
                c[i][j]                   = c11[i][j]
                c[i][j+len(c11)]          = c12[i][j]
                c[i+len(c11)][j]          = c21[i][j]
                c[i+len(c11)][j+len(c11)] = c22[i][j]

        return c