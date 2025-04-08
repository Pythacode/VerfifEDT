# $\textsf {Verfif} \textsf{\color{#ba1ce6}{EDT}}$

## Sommaire

- Installation
- Utilisation
- Explication du code

> [!WARNING]
> Ce projet n'est en aucun cas certifié infaillible, il peut donc contenir des bugs... Merci de votre compréhension.
> Si vous en trouvez un, vous pouvez me le faire parvenir en [créant une issue](https://github.com/Pythacode/PySolver/issues), **avec la sortie console**


## Installation

Pour installer le projet, téléchargez-le avec 
```bash
git clone https://github.com/Pythacode/VerfifEDT.git
```
ou avec le fichier zip.

Ensuite, rentrez dans le dossier du projet, puis installez les dépendances avec

```bash
pip install -r requirements.txt
```

> [!TIP]
> Python doit être installé, sinon, [installez-le](https://www.python.org/downloads/).
> Pip doit également être installé, sinon, [installez-le](https://pip.pypa.io/en/stable/installation/) ou ajoutez `python -m` au début de la commande.

Enfin, il faut installer GeckoDriver :

En le téléchargant depuis le [GitHub de Mozzilla](https://github.com/mozilla/geckodriver/releases), puis en le plaçant dans un fichier PATH.

Où en utilisant un script d'instalation automatique avec
```bash
python3 install-geckodriver.py
```
Quand la page GitHub du projet s'ouvre, GeckoDriver seras installé.

## Utilisation 

Pour utiliser le programme, il faut le configurer ces information de connection en ouvran `login_info.txt`
lancer dans un terminal avec
```bash
python main.py
```
ou
```bash
python3 main.py
```

Le programme afficeras des logs, puis le cours actuel et le prochain cour.
Attention, si la connexion est mauvaise, le programme peut ne pas fonctionner.

### Exemple de sortie

```bash
[2025-04-08 09:44:12] Open driver
[2025-04-08 09:44:44] Driver opened
[2025-04-08 09:44:45] Connection
[2025-04-08 09:44:46] Éduconnect
[2025-04-08 09:44:51] Bot log !
[2025-04-08 09:44:53] Pronote
[2025-04-08 09:45:02] Pronote load
Cours : SC.NUMERIQ.TECHNOL. de 12h55 à 14h45. Fin dans 11 minutes
Prochain cours : ALLEMAND LV2 de 1
```

## Explication du code

Pour tous ceux & celles qui veulent améliorer le code, le modifier, ajouter une UI, cette section est faite pour toi :

### Fichier `main.py`

> [!TIP]
> Souvent, le code est commenté ligne par ligne dans le fichier. Si tu ne comprends pas cette explication, lis le code, tu comprendras peut-être mieux

#### Fonction `contient_nombre(nbr)`

Cette fonction vérifie si `nbr` contient un nombre. On l'appellera dans `get_param(exp, is_invert=False)`

##### Input :
| Variable | Description | Type | Exemple |
|----------|----|--|---------|
| nbr  | Variable à vérifier si elle contient un nombre | str  | "4x" ou "x"  |

##### Output :
bool :
`True` si `nbr` contient un nombre

### Fonction `split_with_sign(text, sign:str)`

Permet de séparer `text` avec `sign` en gardant le signe, si l'expression n'en a pas déjà (`+` ou `-`)

##### Input :
| Variable | Description | Type | Exemple |
|----------|----|--|---------|
| text  | Variable à séparer | str  | "4x+9y" |
| sign  | Signe pour séparer | str  | "+" |

##### Output :
Une liste.

### Fonction `get_param(exp, is_invert=False)`

Cette fonction permet de trouver les paramètres a, b, c, d, e, f pour résoudre le système.

##### Input :
| Variable | Description | Type | Exemple |
|----------|----|--|---------|
| exp  | une liste d'éléments récupérés avec `split_with_sign`  | list  | ["+4x", "+9y"] |
| is_invert  | Faut-il inverser les résultats. Cette variable, par défaut `False`, permet de spécifier si c'est le membre droit ou gauche de l'équation dont on cherche à récupérer les valeurs | bool  | True |

##### Output :

| Ordre | Variable | Description | Type | Exemple |
|----|------|----|--|---------|
| 1 | x | Nombre de `x`  | float  | 1.5 |
| 2 | x | Nombre de `y`  | float  | 7.0 |
| 3 | x | Quotient  | float  | 4.0 |

### Fonction `resoudre_systeme(a, b, c, d, e, f)`

Cette fonction permet de résoudre le système pour les paramètres a, b, c, d, e, f pour le système suivant :

$$
\begin{aligned}
ax + by = e \\
cx + dy = f
\end{aligned}
$$


##### Input :

Variable `a`, `b`, `c`, `d`, `e`, `f`. Variables correspondantes au système ci-dessus

##### Output :

| Ordre | Variable | Description | Type | Exemple |
|----|------|----|--|---------|
| 1 | y | Valeur de `x`  | float  | 1.7 |
| 2 | x | Valeur de `y`  | float  | 7.4 |
