#! /usr/bin/python
# -*- coding: utf-8 -*-

import iterativo.multimat as iterativo
import recursivo.recursivo as recursivo
import strassen.strassen as strassen
import random as random
import sys
from time import time
import Gnuplot	


metodo = {
	1 : iterativo,
	2 : recursivo,
	3 : strassen
}

try:
	variables = int(sys.argv[1])
	algortimo = int(sys.argv[2])
	w, h = variables,variables
	Matrix = [[1 for x in range(w)] for y in range(h)]
	MatrixB = [[1 for x in range(w)] for y in range(h)] 
	print "a: ", Matrix
	print "b: ", MatrixB
	print "Metódo: ",str(metodo[algortimo])
	print metodo[algortimo].mul_matrices(Matrix,MatrixB,variables)
except Exception, e:
	#print "excepcion"
	tiempo =[]
	tiempo2 = []
	tiempo3 = []
	algortimo = int(sys.argv[1])
	for i in range(1,13):
		print i
		w,h = 2**i,2**i
		Matrix = [[1 for x in range(w)] for y in range(h)]
		MatrixB = [[1 for x in range(w)] for y in range(h)] 
		tiempo_inicial = time()
		meto = metodo[2].mul_matrices(Matrix,MatrixB,i)
		tiempo_final = time()
		tiempo2.append(tiempo_final -tiempo_inicial)
		tiempo_inicial = time()
		meto = metodo[3].mul_matrices(Matrix,MatrixB,i)
		tiempo_final = time()
		tiempo3.append(tiempo_final -tiempo_inicial)

	"""for i in range(1,9):
		w,h = 2**i,2**i
		Matrix = [[1 for x in range(w)] for y in range(h)]
		MatrixB = [[1 for x in range(w)] for y in range(h)] 
		tiempo_inicial = time()
		meto = metodo[2].mul_matrices(Matrix,MatrixB,i)
		print meto
		tiempo_final = time()
		tiempo2.append(tiempo_final -tiempo_inicial)
	for i in range(1,9):
		w,h = 2**i,2**i
		Matrix = [[1 for x in range(w)] for y in range(h)]
		MatrixB = [[1 for x in range(w)] for y in range(h)] 
		tiempo_inicial = time()
		meto = metodo[3].mul_matrices(Matrix,MatrixB,i)
		print meto
		tiempo_final = time()
		tiempo3.append(tiempo_final -tiempo_inicial)
	"""
	
	x = [1,2,4,8,16,32,64,128,256,512,1204,2048]
	#y = [1,2,3,4,5,6,7,8,9,9]
	#print len(x)
	#print len(y)
	gp = Gnuplot.Gnuplot(persist = 1)
	#plot2 = Gnuplot.PlotItems.Data(x,tiempo, with_="lines", title="Iterativo")
	plot3 = Gnuplot.PlotItems.Data(x,tiempo2, with_="lines", title="Recursion")
	plot4 = Gnuplot.PlotItems.Data(x,tiempo3, with_="lines", title="Strassen")
	gp.plot(plot3,plot4)
	

