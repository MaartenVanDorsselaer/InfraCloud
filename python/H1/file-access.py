devices=[]
file=open("devices.txt","r")
#er word gebruik gemaakt van de read functie in open
#==>er wordt info gelezen uit de file
for item in file:
    item=item.strip()
    #origineel blanco regels onder elk device
    #==> door strip wordt deze weg gedaan
    devices.append(item)
    #append ==> item wordt toegevoegd aan devices
    #print(item)
file.close()
print(devices)