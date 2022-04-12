from graphes import *

graphe_sans_circuit = {"a":["b"],"b":["c","d"],"c":[],"d":[]}

#1
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

#2
def verification_origine(c, o):
	return ((len(c)>0) and (c[0] == o))

#3
def verification_destination(c, d):
	return ((len(c)>0) and (c[-1] == d))

def testOrigDest():
	l = ['a','b','c']
	return(verification_origine(l,'a'),verification_destination(l,'c'))

#4
def calcul_longueur(l,c):
	result = 0
	for i in range (len(c)-1):
		result+= l(c[i],c[i+1])
	return result

def test_calcul_longueur():
	c = [1,2,3,7,8,9]
	return calcul_longueur(longueur,c)

#5
def verification_certificat_oui(G, l, c, s, t, k):
	return(verification_chemin(G,c) and verification_origine(c,s) and verification_destination(c,t) and (calcul_longueur(l,c) <= k))

def test_certificat_oui():
	G = {1:[2,4],2:[3,4],3:[4],4:[]}
	c = [1,2,3]
	return verification_certificat_oui(G,longueur,c,1,3,100)

#6
def verif_potentiel(G,l,phi):
	for sommet in list(G):
		for suivant in G[s]:
			if(phi(suivant)-phi(sommet) > l(sommet,suivant)):
				return False
	return True

def verification_certificat_non(G, l, phi, s, t, k):
	return((phi(t)-phi(s) > k) and (verif_potentiel(G,l,phi)))


#7
def sous_dijkstra(G,M):
	l = []
	for u in M:
		

def dijkstra(G,s,l):
	M = [s]
	o = []
	d = {s:0}
