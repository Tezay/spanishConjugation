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
    
    listActiveTimes = []
    
    nbr = ["1", "2", "3", "4", "5", "6", "7", " "] 
       
    listTimes = ["Conditional",
         "Futuro",
         "Presente de indicativo",
         "Presente de subjonctivo",
         "Pretérito imperfecto de indicativo",
         "Pretérito indefinido",
         "Prétero imperfecto de subjonctivo"]
    
    timesQuestion = input("Choisir les temps à réviser parmis la liste suivante : \n[1] Conditional \n[2] Futuro\n[3] Presente de indicativo \n[4] Presente de subjonctivo \n[5] Pretérito imperfecto de indicativo \n[6] Pretérito indefinido \n[7] Prétero imperfecto de subjonctivo    :")
     
    lQ1 = len(timesQuestion)
    dif = 7-len(timesQuestion)
    timesQuestion+= dif * " "
    lQ2 = len(timesQuestion) 
    
    while timesQuestion == "       " or len(timesQuestion) > 7 or not(timesQuestion[lQ2-1] in nbr) or not(timesQuestion[lQ2-2] in nbr) or not(timesQuestion[lQ2-3] in nbr) or not(timesQuestion[lQ2-4] in nbr) or not(timesQuestion[lQ2-5] in nbr) or not(timesQuestion[lQ2-6] in nbr) or not(timesQuestion[lQ2-7] in nbr):
        
            timesQuestion = input("Choose time(s) to revise among the following list: \n[1] Conditional \n[2] Futuro\n[3] Presente de indicativo \n[4] Presente de subjonctivo \n[5] Pretérito imperfecto de indicativo \n[6] Pretérito indefinido \n[7] Prétero imperfecto de subjonctivo    :")
    
    for i in range(lQ1):
        
        listActiveTimes.append(listTimes[int(timesQuestion[i])-1])
            
    return listActiveTimes


def userInput(verb, time, pronouns):
    
    response = input(f"[{time}] [{pronouns}] {verb} :")

    return response

def verification(response, verb, time, pronouns):
    
    termination = str(verb[-2:])
    
    correspondanceTermination = ["ar","er","ir"]
    
    correction = correspondanceTime[time]()[listPronouns.index(pronouns)][correspondanceTermination.index(termination)]
    
    if (response == verb[:-2] + correction and time != "Futuro" and time != "Conditional") or ((time == "Futuro" or time == "Conditional") and response == verb + correction):
        print("✅")
    
    elif (time == "Futuro" or time == "Conditional") and response != verb + correction:
        print("\n❌ Answer was: ", verb + correction)
        
    else:
        print("\n❌ Answer was: ", verb[:-2] + correction)

def traning():

    listActiveTimes = TimesChoice()
    print("Done! You can stop at any moment the program with the keyword 'stop'")

    response = ""

    while response != "stop" :
                
        time = random.choice(listActiveTimes)
        pronouns = random.choice(listPronouns)
        
        verb = csvReader.verbChoice()
        response = userInput(verb, time, pronouns)
        verification(response, verb, time, pronouns)
        
traning()
