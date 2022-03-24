#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 10:14:04 2022

@author: valettel
"""

from graphes import *

g = graphe_oriente(100, 10)


# 2.2
# 1) Ce graphe est de type dict, il a 100 sommets.
# Les succeseurs du sommet 0 sont : 2,8,22,28,42,48,62,68,82,88
# Les succeseurs du sommet 67 sont : 3,20,33,50,71,88

# 2)
def degre_sommet(g, s):
    return len(g[s])


# 3)
def sommets_graphe(g):
    return list(g)


# 4)
def arc_graphe(g):
    temp = []
    for i in sommets_graphe(g):
        for j in g[i]:
            temp.append((i, j))
    return temp


# 5)
def parametre_graphe(g):
    return len(sommets_graphe(g)), len(arc_graphe(g))


# 6)
def graphe_mirroir(g):
    d = {}
    for i in range(0, parametre_graphe(g)[0]):
        d[i] = []

    for i in sommets_graphe(g):
        for j in g[i]:
            d[j].append(i)
    return d


# 7)
def degre_entrant(g, s):
    return degre_sommet(graphe_mirroir(g), s)


# 8)
def sous_graphe(g, ls):
    d = {}
    for i in ls:
        d[i] = []
        for j in g[i]:
            if j in ls:
                d[i].append(j)
    return d


# 2.3

# 1)
def accessibles1(g, s):
    res = [s]
    for i in g[s]:
        temp = accessibles1(g, i)
        res += temp
    return res


# 2)
g_simple = {1:[2], 2:[3,4], 3:[], 4:[]} #Avec ce graphe accesibles1 fonctionne correctement...
g_boucle = {1:[2], 2:[3], 3:[4], 4:[2]} #...pas avec celui la.


# 3)
def accessibles2(g, s, res):
    for i in g[s]:
        if not (i in res):
            res.append(i)
            res = accessibles2(g, i, res)
    return res

def appel_accessibles2(g,s):
    return  accessibles2(g, s, [s])

# 4)
def accessibles3(g, s, m, o):
    for i in g[s]:
        if not (i in m):
            m.append(i)
            o.append((i,s))
            (m,o) = accessibles3(g, i, m, o)
    return (m,o)

def appel_accessibles3(g,s):
    return accessibles3(g,s,[s],[])[0]

# 5)
o = accessibles3(g_simple,1,[1],[])

def reconstruire_chemin(s,z,o):
    if z != s :
        for x in o:
            if x[0] == z:
                o_z = x[1]
        return reconstruire_chemin(s,o_z,o)+[z]
    else:
        return [s]


# 6)
