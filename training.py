import random
import csvReader

pronouns = ["yo", "tú", "él", "nosotros", "vosotros", "ellos"]


list = []





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
        
    
    if response == verb[:-2] + csvReader.time[indice1][indice2][int(personnes.index(pronouns))]:
        
        print("✅")
        
    else:
        print("\n❌ Answer was: ", verb[:-2] + csvReader.time[indice1][indice2][int(personnes.index(pronouns))])





def traning():
    
    print("Choose time(s) you want to revise among the following list:")
    
    #Afficher liste verbes

    print("Done! You can stop at any moment the program with the keyword 'stop'")

    response = ""
    
    while response != "stop" :
        
        time = random.choice(temp)
        pronouns = random.choice(personnes)
        
        verb = csvReader.verbChoice()
        response = userInput(verb, time, pronouns)
        verification(response, verb, time, pronouns)
        
traning()