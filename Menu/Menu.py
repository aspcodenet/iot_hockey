def SkapaNySpelare():
    print("Nu är vi inne i Skapa spelare")
    input("Tryck enter för att fortsätta")

def SokSpelare():
    print("Nu är vi inne i Sök spelare")
    input("Tryck enter för att fortsätta")


def Listtest2(): #lower - och skapa listkopia
    lista = ["Sverige", "Finland", "Norge"]
    while True:
        land = input("Ange land")
        if land in lista:
            print("Det finns")
        else:
            print("Det finns inte")

def dictTest(): #Key value - association
    befolkning = dict()
    befolkning["Stockholm"] = 1000000
    befolkning["Uppsala"] = 120000
    befolkning["Nacka"] = 101000

    for k in befolkning:
        print(f"{k} har befolkning {befolkning[k]}")

    key = input("Ange en stad")            
    if key in befolkning:
        print(f"Befolkning {befolkning[key]}")
    else:
        print("Hittar inte")


def Listtest():
    lista = []
    lista.append(245)
    lista.append(13)
    lista.append(1)
    lista.append(999)
    lista.append(56)
    for i in lista:
        print(i)
    lista.sort()
    for i in lista:
        print(i)
    lista.remove(245)            
    for i in lista:
        print(i)


def strings():#https://www.w3schools.com/python/python_strings.asp
    pass


strings()
dictTest()
Listtest2()
while True:
    print("*** Meny ***")
    print("1. Skapa ny hockeyspelare")
    print("2. Sök hockeyspelare")
    print("3. Avsluta")
    selection = input("Välj:>")
    if selection == "1":
        SkapaNySpelare()
    elif selection == "2":
        SokSpelare()
    elif selection == "3":
        break
    else:
        print("Felaktig inmatning")
