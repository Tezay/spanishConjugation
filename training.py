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
        "Conditional": csvReader.Conditional,
        "Futuro": csvReader.Futuro,
        "Presente de indicativo": csvReader.Presente_de_indicativo,
        "Presente de subjonctivo": csvReader.Presente_de_subjonctivo,
        "Pretérito imperfecto de indicativo": csvReader.Preterito_imperfecto_de_indicativo,
        "Pretérito indefinido": csvReader.Preterito_indefinido,
        "Prétero imperfecto de subjonctivo": csvReader.Pretero_imperfecto_de_subjonctivo,
    }

    if response == verb[:-2] + correspondanceTime[time]()[listPronouns.index(pronouns)][correspondanceTermination.index(termination)]:
        print("✅")
        
    else:
        print("\n❌ Answer was: ", verb[:-2] + correspondanceTime[time]()[listPronouns.index(pronouns)][correspondanceTermination.index(termination)])



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