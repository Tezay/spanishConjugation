import random
import csvReader

listPronouns = ["yo", "tú", "él", "nosotros", "vosotros", "ellos"]

def userInput(verb, time, pronouns):
    
    response = input(f"[{time}] [{pronouns}] {verb} :")

    return response



def verification(response, verb, time, pronouns): #time = "Conditional" (par exemple)
    
    termination = str(verb[-2:])
    
    correspondanceTermination = ["ar","er","ir"]

    correspondanceTime = {
        "Conditional": Conditional,
        "Futuro": Futuro,
        "Presente de indicativo": Presente_de_indicativo,
        "Presente de subjonctivo": Presente_de_subjonctivo,
        "Pretérito imperfecto de indicativo": Preterito_imperfecto_de_indicativo,
        "Pretérito indefinido": Preterito_indefinido,
        "Prétero imperfecto de subjonctivo": Pretero_imperfecto_de_subjonctivo,
    }

    if response == verb[:-2] + csvReader.correspondanceTime[time]()[listPronouns.index(pronouns)][correspondanceTermination.index(terminaisons)]:
        print("✅")
        
    else:
        print("\n❌ Answer was: ", verb[:-2] + csvReader.correspondanceTime[time]()[indice1][indice2][int(personnes.index(pronouns))])



def traning():
    
    print("Choose time(s) you want to revise among the following list:")
    
    #Afficher liste verbes

    print("Done! You can stop at any moment the program with the keyword 'stop'")

    response = ""
    
    while response != "stop" :
        
        time = "Futuro"
        pronouns = random.choice(listPronouns)
        
        verb = csvReader.verbChoice()
        response = userInput(verb, time, pronouns)
        verification(response, verb, time, pronouns)
        
traning()