devices=[]
file=open("devices.txt","a") 
#er word gebruik gemaakt van de append functie in open
#==>er wordt info toegevoegd aan de file
while True:
    newItem=input("Enter device name: ")
    if newItem !="exit":
        file.write(newItem + "\n")
    elif newItem =="exit":
        print("All done!")
        break