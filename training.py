import csv
import random

personnes = ["yo", "tú", "él", "nosotros", "vosotros", "ellos"]

def verbChoice():
    
    with open('spanishVerbsList.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        rows = [row for row in reader]
        random_verbe = random.choice(rows)[0]
        
        return random_verbe
  

def userInput(verbe, temps, personne):
    
    rep = input(f"[{temps}] [{personne}] {verbe} :")

    return rep



def verif(rep, verbe, temps, personne):
    
    terminaison = str(verbe[-2:])
    
    if terminaison == "ar" :
        indice2 = 0
    
    elif terminaison == "er":
        indice2 = 1
        
    else:
        indice2 = 2
     
        
    if temps == "Imparfait":
        indice1 = 0
        
    else:
        indice1 = 1
        
    
    if rep == verbe[:-2] + conjugaisons[indice1][indice2][int(personnes.index(personne))]:
        
        print("Bonne réponse !")
        
    else:
        print("\nMauvaise réponse. La réponse était : ", verbe[:-2] + conjugaisons[indice1][indice2][int(personnes.index(personne))])

def entrainement():
    
    rep = ""
    
    while rep != "stop" :
        
        temps = random.choice(temp)
        personne = random.choice(personnes)
        
        verbe = verbChoice()
        rep = userInput(verbe, temps, personne)
        verif(rep, verbe, temps, personne)
        
entrainement()    
