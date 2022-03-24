from graphes import *

graphe_sans_circuit = {"a":["b"],"b":["c","d"],"c":[],"d":[]}

#2.1
	#1)
def Trouve_Puits(g,s):
    while(len(g[s])!=0):
        s = g[s][0]
    return s
"""
	#2)

		#1)Executabilité :
		#(1ere iteration) Comme s est un sommet de g g[s] existe toujours
		#Comme len(g[s]) > 0 alors g[s][0] existe
		#s sera encore un sommet de g car il est dans les succeseurs du noeud précedent

		#2)Terminaison :
		#Comme g ne comporte pas de circuit, alors aucun chemin ne peut passer 2 fois
		#par le même sommet, donc dans le pire des cas un chemin passera par tous les
		#sommets du graphe, la boucle s'arretera donc à un moment.

		#3)Correction :
		#Par l'absurde: le somment s retourné n'est pas un puit, donc il a au moins un
		#succeseur, donc il ne peut pas être l'element retourné car il ne serait pas
		#sorti de la boucle while.

	#3)
		#Par l'absurde:
		#Si un circuit c passant par un sommet s qui est un puit alors s n'a aucun succeseur
		#Donc le chemin c s'arrête et s est son dernier élément. Or s ne peut pas être
		#le premier élément de c car s n'as pas de succeseur.

#2.2
	#4)
		{"a":["b"],"b":["c","d"],"c":[],"d":[]}

		Tri(a) = 1
		Tri(b) = 2
		Tri(c) = 3
		Tri(d) = 4

	5)
		Soit G un graphe contenant un circuit et un tri topologique Tri().
		C'est à dire qu'il existe un chemin simple, clos et de longueur non nulle.
		Soit A le premier sommet du chemin, on a donc Tri(A) < Tri(B) pour tout B,
		tq B est un autre sommet du chemin.
		Soit C l'avant dernier sommet du chemin, alors on aura Tri(C) > Tri(A),
		Or l'arc CA existe car A est un succeseur de C. IL Y A UNE ERREUR.
		Soit le chemin n'est pas un circuit soit Tri n'est pas un tri topologique.

	6)
		On suppose l'énoncé.
		On pose x la valeur max du tri topologique de G[V\{p}]
		On pose Tri(p) = x+1,
		Comme p est un puit alors il n'a aucun succeseur.
		Donc les seuls arc contenant p seront du type yp, avec y n'importe quel
		sommet de V\{p}.
		On a donc bien, pour tout arc yp, Tri(y) < Tri(p)
		Donc Tri est un tri topologique.

2.3

7)
"""
def sous_graphe(g, ls):
    d = {}
    for i in ls:
        d[i] = []
        for j in g[i]:
            if j in ls:
                d[i].append(j)
    return d


def appelTriTopo(G):
	Tri = {}
	return (TriTopo(G,Tri))


def TriTopo(G,Tri):
	if(len(list(G)) == 1):
		Tri[(list(G)[0])] = 0
	else :
		puit = Trouve_Puits(G,(list(G)[0]))
		ls = list(G)
		ls.remove(puit)
		sg = sous_graphe(G,ls)
		Tri = TriTopo(sg,Tri)
		max_ = max(Tri.values())
		Tri[puit] = max_ + 1
	return Tri


def TestTriTopo():
	g = {"a":["c"],"b":["a","c"],"c":["d"],"d":[]}
	g_ = {"a":["c"],"b":["a"],"c":["b","d"],"d":[]}
	t = {"a":[],"b":["a"],"c":["b"],"d":["b"]}
	v = {"a":44,"b":14}

	return appelTriTopo(g)

"""
8)
	Le fait qu'il n'y ai pas de circuit permet de dire qu'on pourra toujours
	trouver un puit. Cela valide donc le principe de recurrence de l'algo de
	la question 7.

9)
	Le tri topologique est un certificat du NON pour le problème de la recherche
	de circuit.

3.

10)
"""

def Circuit_ou_Puit(G, s):
	result = []

	while((len(G[s])!=0) and not(s in result)):
		result.append(s)
		s = G[s][0]
	if(len(G[s]) ==0):
		return ([s])
	else:
		return(result[(result.index(s)):]+[s])

def TestCircuit_ou_Puit():
	g = {"a":["c"],"b":["a","c"],"c":["d"],"d":[]}
	g_ = {"a":["c"],"b":["a"],"c":["b","d"],"d":[]}
	g__ = graphe_oriente(100, 3)
	return Circuit_ou_Puit(g__,0)


#11)
def Pas_De_Circuit(G):
	sommets = list(G)
	sg = sous_graphe(G,sommets)
	while(len(sommets) > 1):
		list_s = Circuit_ou_Puit(sg,sommets[0])
		if len(list_s) > 1 :
			return False
		else:
			sommets.remove(list_s[0])
			sg = sous_graphe(sg,sommets)
	return True

"""
def Circuit_ou_Tri_Topologique(G,s):
	result = []
	while(len(G[s] != 0):
		if()
"""
