playerPoints = {}

while True:
    namn = input("Ange spelarnamn")
    if namn == "exit":
        break
    points = int(input("Ange poäng"))
    playerPoints[namn] = points

#for boxNamnet in playerPoints:
#    print(f"{boxNamnet} har poäng {playerPoints[boxNamnet]}")

namn = input("Ange spelare som du vill söka på ") 
print(f" {namn} har {playerPoints[namn]} poäng")


suddenPoints = 13
suddenPoints = 14
#listOfNumbers = [1,344,5,66]
listOfNumbers = []
listOfScandinavianCountries = ["Sweden", "Denmark", "Norway"]
listOfScandinavianCountries[2] = "Norge"

listOfScandinavianCountries.sort()
listOfScandinavianCountries.pop()


for countryName in listOfScandinavianCountries:
    print(countryName)


land = input("Vilket land ska from nu också vara skandinaviskt?")
listOfScandinavianCountries.append(land)
for countryName in listOfScandinavianCountries:
    print(countryName)

print(f"Nu är så här många {listOfScandinavianCountries.count()}")

for i in listOfNumbers:
    print(i)










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

