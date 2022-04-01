from graphes import *

graphe_sans_circuit = {"a":["b"],"b":["c","d"],"c":[],"d":[]}

def verification_chemin(G, c):
	isChemin = True;
	index = 0;
	while((index< len(c) - 1) and isChemin):
		if(not(c[index+1] in G[c[index]])):
			isChemin = False
		index += 1
	return isChemin

def testVerifChemin():
	l = ['a','b','c']
	return verification_chemin(graphe_sans_circuit, l)

def verification_origine(c, o):
	return ((len(c)>0) and (c[0] == o))

def verification_destination(c, d):
	return ((len(c)>0) and (c[-1] == d))

def testOrDest():
	
