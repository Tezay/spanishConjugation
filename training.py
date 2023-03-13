import random
import csvReader

listPronouns = ["yo", "tú", "él", "nosotros", "vosotros", "ellos"]

correspondanceTime = {
        "Conditional": csvReader.Conditional,
        "Futuro": csvReader.Futuro,
        "Presente de indicativo": csvReader.Presente_de_indicativo,
        "Presente de subjonctivo": csvReader.Presente_de_subjonctivo,
        "Pretérito imperfecto de indicativo": csvReader.Preterito_imperfecto_de_indicativo,
        "Pretérito indefinido": csvReader.Preterito_indefinido,
        "Prétero imperfecto de subjonctivo": csvReader.Pretero_imperfecto_de_subjonctivo,
    }



def TimesChoice():
    
    nbr = ["1", "2", "3", "4", "5", "6", "7"] 
       
    listTimes = ["Conditional",
         "Futuro",
         "Presente de indicativo",
         "Presente de subjonctivo",
         "Pretérito imperfecto de indicativo",
         "Pretérito indefinido",
         "Prétero imperfecto de subjonctivo"]
    
    timesQuestion = input(
        "Choisir les temps à réviser parmis la liste suivante :
        \n[1] Conditional
        \n[2] Futuro
        \n[3] Presente de indicativo
        \n[4] Presente de subjonctivo
        \n[5] Pretérito imperfecto de indicativo
        \n[6] Pretérito indefinido
        \n[7] Prétero imperfecto de subjonctivo    :"
    )
        
    for i in range(len(timesQuestion))
            
       if timesQuestion[i] in nbr:
            
                listActiveTimes.append(listTimes[int(timesquestion[i])-1])
    
    return listActiveTimes


def userInput(verb, time, pronouns):
    
    response = input(f"[{time}] [{pronouns}] {verb} :")

    return response

def verification(response, verb, time, pronouns): #time = "Conditional" (par exemple)
    
    termination = str(verb[-2:])
    
    correspondanceTermination = ["ar","er","ir"]
    
    correction = correspondanceTime[time]()[listPronouns.index(pronouns)][correspondanceTermination.index(termination)]
    
    if (response == verb[:-2] + correction and time != "Futuro" and time != "Conditional") or ((time == "Futuro" or time == "Conditional") and response == verb + correction)):
        print("✅")
    
    elif (time == "Futuro" or time == "Conditional") and response != verb + correction):
        print("\n❌ Answer was: ", verb + correction)
        
    else:
        print("\n❌ Answer was: ", verb[:-2] + correction)

def traning():
    
    print("Choose time(s) you want to revise among the following list:")
    
    #Afficher liste verbes

    print("Done! You can stop at any moment the program with the keyword 'stop'")

    response = ""
    listActiveTimes = TimesChoice()

    while response != "stop" :
                
        time = random.choice(listActiveTimes)
        pronouns = random.choice(listPronouns)
        
        verb = csvReader.verbChoice()
        response = userInput(verb, time, pronouns)
        verification(response, verb, time, pronouns)
        
traning()
