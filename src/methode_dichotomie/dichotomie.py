import numpy as np
def dichotomie(f,a,b,tol=1e-7): # cette fonction retourne l'abscisse x à epsilon près tel que f(x)=0
    while np.abs(b-a)> tol: 
        milieu =(a+b)/2
        if f(milieu)*f(a)>0: #on peut avoir une fonction croissante ou decroissant
            a=milieu # recherche dans l'intervalle [milieu,b]
        else:
            b=milieu # recherche dans l'intervalle [a,milieu]

    return (a+b)/2 # on retourne a ou b
"""
def dichotomie_visualisation(f,a,b,tol=1e-7):
    if f(a)*f(b) > 0:
        print("Erreur : la fonction ne change pas de signe")
        return None
    
    historique_milieu = []
    # On itere jusqu'a l'approximation
    milieu = (a+b)/2
    while milieu > tol :
            historique_milieu.append(milieu)

            if f(milieu) == 0:
                 break
            elif f(a)*f(milieu) < 0:
                 b = milieu
            else:
                 a = milieu
    return historique_milieu
"""