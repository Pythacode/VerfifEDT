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

Pour utiliser le programme, il faut le configurer ces information de connection en ouvrant `login_info.txt`, puis en mettant sur la première ligne le nom d'utilisateur, sur la deuxième ligne le mot de passe, et sur la troisième l'url de connection qui correspond à l'url de la page ci-dessous.

![image](https://github.com/user-attachments/assets/d35883c1-637e-4dd1-b1cd-1683dd4cb0a1)


Enfin, lancer le programe dans un terminal avec
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
Prochain cours : ALLEMAND LV2 de 15h00 à 15h55. Début dans 26 minutes
```

## Explication du code

Pour tous ceux & celles qui veulent améliorer le code, le modifier, l'utiliser à des fin utiles (ou non), cette section est faite pour toi :

### Fichier `main.py`


#### Fonction `log(message)`

Affiche `message` avec l'heure et la date en jaune sous le format suivant : `[AAA-MM-JJ HH:MM:SS] message`
Se serais facilement adaptable au pour l'enregister dans un fichier de log.

#### Définition des information de connection

```python
log_info = open('login_info.txt', 'r').read().splitlines() # ouvre le fichier login_info.txt et le transforme en liste en séparant cheque retour à la ligne

username = log_info[0] # Première ligne du fichier
password  = log_info[1] # Deuxième ligne du fichier
url = log_info[2] # Troisième ligne du fichier
```

#### Ouverture du driver 

```python
options = Options() # Crée un objet option
options.add_argument("--headless") # Ajoute une option pour cacher l'UI (facultatif)

driver = webdriver.Firefox(options=options) # Ouvre le driver avec les options
```

##### Navigation

```python
assert "X" in driver.title # Verifie si il y à "X" dans le titre de la page
```

```python
elem = driver.find_element(By.XPATH, "XPATH") # Localise l'élement avec l'XPATH "XPATH"
elem.click() # Clique dessus
```


```python
elem = driver.find_element(By.ID, "ID") # Localise l'élement avec l'ID "ID"
elem.click() # Clique dessus
```

Idem avec `CLASS_NAME`

```python
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "bouton_eleve"))) # Attent que l'élément exsiste
```

```python
onglets = driver.window_handles # Récupère une liste des onglets
driver.switch_to.window(onglets[-1]) # Switch sur le dernier onglet ouvert
```
#### Fonction `locate_cours(elements)`

Cette fonction prend en entrée une liste d'élément.
Pour tous les élèment, elle vérifie si ils corresponde au REGEX suivant :

```regex
de ([0-9]{2})h([0-9]{2}) à ([0-9]{2})h([0-9]{2}) (.*)
```

puis, le cas échèant, récupère les horraires du cours 

```python
start_hour = datetime.strptime(f"{match.group(1)}h{match.group(2)}", format_hour).replace(year=now.year, month=now.month, day=now.day)
end_hour = datetime.strptime(f"{match.group(3)}h{match.group(4)}", format_hour).replace(year=now.year, month=now.month, day=now.day)
```

Pour verifier si le cours à commencé ou non

```python
if now > start_hour :
    ...
elif now < start_hour :
    ...
```
Dans le premier cas, verifie si le cours et fini

```python3
if now < end_hour :
```

Si oui, on affiche le cours en vert et on met `result` à `True`

```pyton
print(f"{Fore.GREEN}Cours : {match.group(5)} de {start_hour.strftime('%Hh%M')} à {end_hour.strftime('%Hh%M')}. Fin dans {((end_hour - now).total_seconds() / 60):.0f} minutes")
result =  True
```

Sinon, on ne fait rien.

Dans le second cas, on affiche le cours suivant en vert, on met `result` à `True`, et on sort de la boucle pour éviter d'afficher plus de cours.

```python
print(f"{Fore.GREEN}Prochain cours : {match.group(5)} de {start_hour.strftime('%Hh%M')} à {end_hour.strftime('%Hh%M')}. Début dans {((start_hour - now).total_seconds() / 60):.0f} minutes")
result =  True
break
```