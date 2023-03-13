import csv
import random
import os

pronouns = ["yo", "tú", "él", "nosotros", "vosotros", "ellos"]

def verbChoice():
    
    with open('spanishVerbsList.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        rows = [row for row in reader]
        random_verbe = random.choice(rows)[0]
        
        return random_verbe


def verbConjugation(verb, time, pronouns, termination):

    

    

def userInput(verb, time, pronouns):
    
    response = input(f"[{time}] [{pronouns}] {verb} :")

    return response



def verification(response, verb, time, pronouns):
    
    termination = str(verb[-2:])
    
    if termination == "ar" :
        indice2 = 0
    
    elif termination == "er":
        indice2 = 1
        
    else:
        indice2 = 2
     
        
    if time == "Imparfait":
        indice1 = 0
        
    else:
        indice1 = 1
        
    
    if response == verb[:-2] + conjugaisons[indice1][indice2][int(personnes.index(pronouns))]:
        
        print("Bonne réponse !")
        
    else:
        print("\nMauvaise réponse. La réponse était : ", verb[:-2] + conjugaisons[indice1][indice2][int(personnes.index(pronouns))])

def traning():
    
    response = ""
    
    while response != "stop" :
        
        time = random.choice(temp)
        pronouns = random.choice(personnes)
        
        verb = verbChoice()
        response = userInput(verb, time, pronouns)
        verification(response, verb, time, pronouns)
        
traning()