


machineStop=False
machineStock={"Water":500,"Milk":150,"Coffee":176,"Money":0}
def getInput():
    customerInput=input("Choose the desired option\nWhat would you like to drink?(espresso/latte/cappuccino):\nGet report(report)\nTurn off the machine(off)\n")
    if customerInput=="off":
       exit()
    if customerInput=="report":
        print("Water "+str(machineStock["Water"])+"ml")
        print("Milk "+str(machineStock["Milk"])+"ml")
        print("Coffee "+str(machineStock["Coffee"])+"gr")
        print("Money "+str(machineStock["Money"])+"$")    
    if customerInput=="espresso" or customerInput=="latte" or customerInput=="cappuccino":
        drinkProccess(customerInput)

def drinkProccess(drink):
    global machineStock
    print("Insert coins")
    quarters=0.25*float(input("Specifiy number of quarters:"))
    dimes=0.10*float(input("Specify the number of dimes:"))
    nickles=0.05*float(input("Specify the number of nickles:"))
    pennies=0.01*float(input("Specify the number of pennies:"))
    totalcoins=quarters+dimes+nickles+pennies
    machineStock["Money"]=totalcoins
    if drink=="espresso" and machineStock["Water"]>100 and machineStock["Milk"]>30 and machineStock["Coffee"]>50 and machineStock["Money"]>5.5:
        machineStock["Water"]=machineStock["Water"]-100
        machineStock["Milk"]=machineStock["Milk"]-30
        machineStock["Coffee"]=machineStock["Coffee"]-50
        machineStock["Money"]=machineStock["Money"]-5.5
        print("Proccessing drink")
        print("YOUR DRINK IS READY!Enjoy.\n\n")
    
    elif drink=="latte" and machineStock["Water"]>100 and machineStock["Milk"]>50 and machineStock["Coffee"]>50 and machineStock["Money"]>4.5:
        machineStock["Water"]=machineStock["Water"]-100
        machineStock["Milk"]=machineStock["Milk"]-50
        machineStock["Coffee"]=machineStock["Coffee"]-50
        machineStock["Money"]=machineStock["Money"]-4.5
        print("Proccessing drink")
        print("YOUR DRINK IS READY!Enjoy.\n\n")

        
    elif drink=="cappuccino" and machineStock["Water"]>150 and machineStock["Milk"]>40 and machineStock["Coffee"]>70 and machineStock["Money"]>6:
        machineStock["Water"]=machineStock["Water"]-150
        machineStock["Milk"]=machineStock["Milk"]-40
        machineStock["Coffee"]=machineStock["Coffee"]-70
        machineStock["Money"]=machineStock["Money"]-6.0
        print("Proccessing drink")
        print("YOUR DRINK IS READY!Enjoy.\n\n")
    else:
        print("There was an error with your command.")

while machineStop==False:
    getInput()