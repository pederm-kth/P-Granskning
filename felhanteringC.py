import re

def epost(inmatning):
    while True:
            var = input(inmatning)
            validator = bool(re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', var))
            if validator == True:
                return var
            elif validator == False:
                print("Vänligen mata in en epostadress med godtyckligt format: ")

def adress(inmatning):
    while True:
            var = input(inmatning)
            validator = bool(re.match('[åäöÅÄÖA-Za-z0-9" ",]*$', var))    
            if validator == True:
                return var
            elif validator == False:
                print("Vänligen mata in en godtycklig adress: ")

def namn(inmatning):
    """Funktionen kontrollerar ifall variabeln består av endast en sträng"""
    while True:
            var = input(inmatning)
            validator = bool(re.match('[åäöÅÄÖA-Za-z" "-]*$', var))    
            if validator == True:
                return var
            elif validator == False:
                print("Vänligen mata in ett namn utan siffror: ")
    
def telefonnummer(inmatning):
    """Funktionen kontrollerar ifall variabeln är ett heltal med siffror"""
    while True:
            var = input(inmatning)
            validator = bool(re.match('[0-9-]*$', var))    
            if validator == True:
                return var
            elif validator == False:
                print("Vänligen mata in ett telefonnummer utan bokstäver: ")
