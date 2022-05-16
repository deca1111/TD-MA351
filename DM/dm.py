from graphes import *

"""
1 - Encodage des graphes non-orientés

2 - Connexité des graphes non-orientés

	1)	Il a n composantes connexes.

	2)	On veut montrer que pour un sommet s de G->, l'ensemble des accessibles
		de de s forment une composante connexe de G.
		On commence par montrer que les accessibles depuis s forment une partie
		connexe de G puis on montrera que c'est la plus grande.

		Soit x un sommet accesible depuis s. Il existe un chemin de s à x dans G->.
		C'est à dire un	ensemble de sommet reliés par des arc, or comme G-> est
		un graphe symétrique, le chemin allant de x à s existe aussi.
		Il existe donc une chaine reliant s à x pour tout sommet x accessible
		depuis s.
		Donc les sommets accessible depuis s forme une partie connexe de G.

		On a aussi prouvé dans le cours qu'il n'existe aucun arc depuis un
		sommet x accessible de s, vers un sommet y qui ne serait pas dans
		l'ensemble des accessibles de s.
		La symétrie de G-> donne donc qu'il n'existe pas d'arrete entre x et y
		dans G.
		Il n'existe donc aucune chaine entre s et y.
		Donc l'ensemble des accessibles depuis s est bien la plus grande partie
		connexe de G contenant s.
		C'est donc une composante connexe de G.

	3)	On utilisera la fonction Accessibles3() du cours car nous avons prouvé
		qu'elle renvoie l'ensemble des sommets accessibles depuis s. Cela
		fonctionnera correctement car G est defini comme un graphe orienté spécial.
		Le résultat de cette fonction sera donc une composante connexe de G
		contenant s.
"""

#4)

def accessibles3(g, s, m, o):#fonction du cours
    for i in g[s]:
        if not (i in m):
            m.append(i)
            o.append((i,s))
            (m,o) = accessibles3(g, i, m, o)
    return (m,o)

def appel_accessibles3(g,s):
    return accessibles3(g,s,[s],[])[0]



def partition(G):
	sommets_libre = list(G)
	composantes_connexe = []
	while sommets_libre:
		composantes_connexe.append(appel_accessibles3(G,sommets_libre.pop(0)))
		for s in composantes_connexe[-1]:
			if s in sommets_libre:
				sommets_libre.remove(s)
	return composantes_connexe

def test_partition():
	graphe_ex = {'a':['b','c'], 'b':['a','c'], 'c':['a','b'], 'd':[], 'e':[]}
	return partition(graphe_ex)
#5)

def connexe(G):
	return len(partition(G)) == 1

def test_connexe():
	graphe_ex = {'a':['b','c'], 'b':['a','c'], 'c':['a','b','d'], 'd':['c'], 'e':[]}
	return degre(graphe_ex)

"""
3 - Cycles eulériens ; graphes eulériens

3.1 Routines utilitaires

#6)
"""

def degre(G, s):
	return len(G[s])

def test_degre():
	graphe_ex = {'a':['b','c'], 'b':['a','c'], 'c':['a','b','d'], 'd':['c'], 'e':[]}
	return degre(graphe_ex, 'a')

#7)

def degrePair(G,s):
	return (degre(G, s)%2) == 0

def test_degrePair():
	graphe_ex = {'a':['b','c'], 'b':['a','c'], 'c':['a','b','d'], 'd':['c'], 'e':[]}
	return degrePair(graphe_ex,'a')

#8)

def degrePairs(G):
	for s in list(G):
		if not degrePair(G,s):
			return False
	return True

def test_degrePairs():
	graphe_ex = {'a':['b','c'], 'b':['a','c'], 'c':['a','b','d'], 'd':['c'], 'e':[]}
	return degrePairs(graphe_ex)

#9)
"""
Version non destructive
def retireArete(G,x,y):#on considère que l'arete xy existe
	sG = sous_graphe(G, list(G)) #copie de G
	sG[x].remove(y)
	sG[y].remove(x)
	return sG #non destructif


Version destructive
"""
def retireArete(G,x,y):#on considère que l'arete xy existe
	G[x].remove(y)
	G[y].remove(x)
	return G


def test_retireArete():
	graphe_ex = {'a':['b','c'], 'b':['a','c'], 'c':['a','b','d'], 'd':['c'], 'e':[]}
	return retireArete(graphe_ex)


"""
3.2 Théorie

	10)	C'est, à peu de chose près le théorème d'Euler. Ici, il n'y a pas
		d'obligation que le graphe soit connexe.
		On pars d'un sommet dont le degré est non nul et on parcourt l'arrete
		qui mene a un de ses voisins.
		On retire cette arete, il y donc maintenant 2 sommets avec degrés
		impaires, les 2 sommets aux extremités de l'arete.
		On continue à parcourir le graphe en supprimant au fur et à mesure les
		aretes. Il y a toujours 2 sommets au degré impaire, le sommet de depart
		et le sommet à l'extremité de la dernière arete supprimée.
		On continue soit jusqu'à croiser le sommet de départ, soit jusqu'à ce
		qu'il ne reste qu'une seule arete. Cette dernière relie donc forcement
		le sommet de depart car il est à degré impair (ici forcement de degré 1).
		Dans tout les cas on recroise le sommet de départ, il y a donc un cycle.


	11)	On part du sommet commun au deux cycles et on parcourt le premier cycle
		jusqu'à retourner au sommet de départ, comme le sommet est commun aux 2
		cycles on peut maintenant parcourir le second cycle jusqu'à retourner au
		sommet de départ.
		On a bien parcouru un cycle contenant les aretes des 2 cycles C1 et C2.

	12)	On procède par l'absurde, soit G un graphe non-orienté connexe. C un
		cycle de G et G' le graphe obtenu en retirant de G le cycle C.
		On suppose que tous les degrés des sommets de C dans G' sont égaux à 0.
		Comme G est connexe, il existe un chemin reliant tous les sommets de G.
		Il existe donc une arete entre k un sommet de C et x un sommet pas dans
		C.
		Cette arete n'appartient pas à C donc existe dans G'.
		Donc deg(k) >=1. C'est absurde donc G n'est pas connexe.


3.3 Pratique

	13)
"""

def cycle(G,s):
	copie = sous_graphe(G, list(G)) #copie de G
	sommet_actu = s
	sommet_next = G[s][0]
	retireArete(sommet_actu,sommet_next)
	cycle = [sommet_actu,sommet_next]

	while sommet_next != s:
		sommet_actu = sommet_next
		sommet_next = G[sommet_actu][0]
		retireArete(sommet_actu,sommet_next)
		cycle.append(sommet_next)
	return cycle

def test_cycle():
	graphe_ex = {'a':['b','c'], 'b':['a','c'], 'c':['a','b','d'], 'd':['c'], 'e':[]}
	return cycle(graphe_ex)
