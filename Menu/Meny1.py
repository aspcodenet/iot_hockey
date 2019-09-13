
def SkapaNySpelare():
        print("******** Skapa ny spelare *******")
        namn = input("Ange namn på spelaren:")

def SokSpelare():
            print("******** Sök spelare *******")
            namn = input("Sök efter i namn:")

while True:
    print("*** HOCKEYMENY ***")
    print("1. Skapa ny spelare")
    print("2. Sök spelare")
    print("3. Avsluta")
    selection = int(input())
    if selection == 1:
        SkapaNySpelare()
        print("Spelare skapad...")
    elif selection == 2:
        SokSpelare()
    elif selection == 3:
        break

