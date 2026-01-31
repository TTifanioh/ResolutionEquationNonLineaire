# 🎯️ Résolution d'équation non linéaire
## 📝️ Description et objectif
Pour résoudre des équation non lineaire de type $f(x) = 0$, c'est à dire trouver une solution de cette équation. 

Pour ce faire, il y a plusieurs méthode pour la résoudre un eqation non linéaire. On écrit des algo afin de la résoudre.
Voici quelques methode que je vais vous citez :
- Méthode de point fixe
- Méthode de newton
- Méthode de dichotomie

L'objectif de ces méthodes est d'approximée un solution d'une équation c'est à dire une valeur près

---

## 🛠️ Outils:

Pour utiliser ces algorithmes dans vous besoin, il faut avoir les outils nécessaire.
Il y en a différent outils disponible, mais je vais vous citez ces que je connaissent :
- Jupyter Notebook
- VS Code (Visual Studio Code)
- Terminal

Il y en a d'autre, je vous invite à les cherches si ces outils ne vous conviennent pas ou juste pour la curiosité. Mais ces sont ces outils que j'utilise en générale.

---

## 📁️ Structure de projet

```text

|_______
|	docs/
|	|_______
|	|	ResolutionEquationNonLineaire.pdf	# Support pdf 
|	|_______
|		ResolutionEquationNonLineaire.tex	# Code source latex 	
|
|_______
	src
	|_______
	|	methode_dichotomie
	|	|_______
	|	|	dichotomie.ipynb			
	|	|_______
	|_______	dichotomie.py
		methode_newton
		|_______
		|	newton.ipynb
		|_______
			newton.py
		methode_point_fixe
		|_______
		|	point_fixe.ipynb
		|_______
			point_fixe.py
```

---

## 🧑‍💻️ Installation et utilisation :
Assurer vous d'avoir installer python et jupyter, si ce n'est pas le cas veuillez suivre les commandes suivant :

1. Installer python et jupyter:
 
Pour installer python :
```bash
sudo apt update & upgrade
sudo install python
```
Vous pouvez vérifier si l'installation à été un succès avec la commande :
```bash
python3 --version
```

Pour installer jupyter:
```bash
sudo apt install jupyter
```

2. Cloner la dépôt:
```bash
git clone https://github.com/TTifanioh/ResolutionEquationNonLineaire.git
```

3. Utiliser les algorithmes:
```bash
python3 fichier.py  # ici fichier represente dichotomie.py ou newton.py ou point_fixe.py
```

4. Voir la solution approximer sur un graphique:


Il suffit de cliquer sur le fichier .ipynb si vous avez installer jupyter et le graphique apparaitra.

---

> Auteur :  RANDRIANOELINA Tifanioh Mahefa Fandresentsoa
