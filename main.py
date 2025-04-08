from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.webdriver import Options
from colorama import init, Fore
from datetime import datetime
import re
from datetime import datetime
from selenium.common.exceptions import NoSuchElementException


init(autoreset=True)

def log(message) :

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"{Fore.YELLOW}[{now}] {message}")

log_info = open('login_info.txt', 'r').read().splitlines()

username = log_info[0]
password  = log_info[1]
url = log_info[2]

log("Open driver")

options = Options()
options.add_argument("--headless")

driver = webdriver.Firefox(options=options)

log('Driver opened')

driver.get(url)
assert "Authentification" in driver.title

log("Conection")

#Élève ou parent
elem = driver.find_element(By.XPATH, "/html/body/main/div/div/div[1]/div/div/form/fieldset[1]/legend/button")
elem.click()

# De l'académie de montpellier 
elem = driver.find_element(By.XPATH, "/html/body/main/div/div/div[1]/div/div/form/fieldset[1]/ul/li[1]/div/label")
elem.click()

#Valider
elem = driver.find_element(By.ID, "button-submit")
elem.click()

log('Éduconnect')

## Éduconnect
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "bouton_eleve")))


assert "ÉduConnect" in driver.title

#Éleve
elem = driver.find_element(By.ID, "bouton_eleve")
elem.click()

#Username
username_entry = driver.find_element(By.ID, "username")
username_entry.clear()
username_entry.send_keys(username)

#Password
password_entry = driver.find_element(By.ID, "password")
password_entry.clear()
password_entry.send_keys(password)

# Valider
elem = driver.find_element(By.ID, "bouton_valider")
elem.click()

log('Bot log !')

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/nav/ul[2]/li[7]/a")))

# Pronote link
elem = driver.find_element(By.XPATH, "/html/body/div[3]/nav/ul[2]/li[7]/a")
elem.click()

log('Pronote')

onglets = driver.window_handles
driver.switch_to.window(onglets[-1])
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "id_74id_38")))

log('Pronote load')

format_hour = "%Hh%M"  # Le format des heures est "HH:MM"

cour_element = driver.find_element(By.ID, "id_74id_38")
elements = cour_element.find_elements(By.XPATH, ".//li")

now = datetime.now()

def locate_cours(elements) :

    result = False

    display_day_elem = driver.find_element(By.ID, "IE.Identite.collection.g5.cellule_Edit")

    if display_day_elem.text != "Aujourd'hui" : return False

    for element in elements :
        match = re.match("de ([0-9]{2})h([0-9]{2}) à ([0-9]{2})h([0-9]{2}) (.*)", element.text)
        if match :
            start_hour = datetime.strptime(f"{match.group(1)}h{match.group(2)}", format_hour).replace(year=now.year, month=now.month, day=now.day)
            end_hour = datetime.strptime(f"{match.group(3)}h{match.group(4)}", format_hour).replace(year=now.year, month=now.month, day=now.day)


            if now > start_hour :
                if now < end_hour :
                    print(f"{Fore.GREEN}Cours : {match.group(5)} de {start_hour.strftime('%Hh%M')} à {end_hour.strftime('%Hh%M')}. Fin dans {((end_hour - now).total_seconds() / 60):.0f} minutes")
                    result =  True
            elif now < start_hour :
                print(f"{Fore.GREEN}Prochain cours : {match.group(5)} de {start_hour.strftime('%Hh%M')} à {end_hour.strftime('%Hh%M')}. Début dans {((start_hour - now).total_seconds() / 60):.0f} minutes")
                result =  True
                break
                
                    
            
    return result
    
if not locate_cours(elements) :
    print(Fore.GREEN + "Tu a fini ta journée")

driver.quit()
