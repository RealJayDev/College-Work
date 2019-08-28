Users = [ #Usernames and Passwords
   ["Username", "Wibble", "A", 5],
   ]

Tariffs = ["A", "B", "C"]

Charges = [
   [0.3, 0.05, 15],
   [0.1, 0.02, 20],
   [0.9, 0, 30],
   ]

def Return():
   Choice = input("return to menu? yes / no\n")
   while (Choice.lower() != "yes") and (Choice.lower() != "no"):
       print("This value is not correct, please try again")
       Choice = input("return to menu or quit? yes / no\n")
  
   if Choice.lower() == "yes":
     Menu()
   elif Choice.lower() == "no":
     None


def Bills():
   print("We will help you calculate your current bill.")
   Peak = input("Please input the amount of peak minutes you use \n")
   offpeak = input("Please input the amount of off-peak minutes you use \n")
   try:
       int(Peak) and int(offpeak)
   except ValueError:
       Peak = input("This value is incorrect, Please input the amount of peak minutes you use \n")
       offpeak = input("This value is incorrect, Please input the amount of off-peak minutes you use \n")

   #tried to make this run more than once but it just kept spitting out errors and closing the program

   CurrentTariff = Tariffs.index(Users[0][2])
   PeakRate = Charges[CurrentTariff][0]
   OffPeakRate = Charges[CurrentTariff][1]
   PeakCharge = float(Peak) * PeakRate
   OffPeakCharge = float(offpeak) * OffPeakRate
   print("Your current peak charge is", PeakCharge, "pounds")
   print("Your current off-peak charge is", OffPeakCharge, "pounds")
   print("With a line rental of", Charges[CurrentTariff][2], "pounds")
   total = PeakCharge + OffPeakCharge + float(Charges[CurrentTariff][2])
   print("Your total payment required is:", (total * 1.2),"pounds")
   Return()

def Bal():
   print("Your Balance is", Users[0][3] ,"pounds")
   Return()

def Tariff():
   print("Your current tariff is:", Users[0][2])
   print("We have multiple tariffs to choose from, these include:")
   print("Tariff\tPeak rate\tOff-peak\tLine rental")
   print("A\t0.30\t\t0.05\t\t15.00")
   print("B\t0.10\t\t0.02\t\t20.00")
   print("C\t0.90\t\tNone\t\t30.00")
   Chosen = input("Please select a tariff\n")
   while (Chosen.upper() != "A") and (Chosen.upper() != "B") and (Chosen.upper() != "C"):
       print("This value is incorrect, please try again.")
       Chosen = input("Please select a tariff\n")
   Up = Chosen.upper()
   if Up == "A":
       Users[0][2] = "A"
       print("You have chosen tariff A")
       Return()
   elif Up == "B":
       Users[0][2] = "B"
       print("You have chosen tariff B")
       Return()
   elif Up == "C":
       Users[0][2] = "C"
       print("You have chosen tariff C")
       Return()

def Menu():
   print("Welcome to the Menu\n")
   print("There are 4 options:")
   print("1)\tBalance")
   print("2)\tTariffs")
   print("3)\tMy bills")
   print("4)\tExit")
   Inputs = input("Please select an option\n")
  
   while (Inputs != "1") and (Inputs != "2") and (Inputs != "3") and (Inputs != "4"):
       print("This value is not acceptable, please try again.")
       Inputs = input("Please select an option\n")
  
  
   if Inputs == "1":
       Bal()
   elif Inputs == "2":
       Tariff()
   elif Inputs == "3":
       Bills()
   elif Inputs == "4":
       None

def LogIn():
   Tries = 0
   User = input("Please insert your username\n")
   Pass = input("Please insert your password\n")
   Enabled = False
   while Tries <= 1 and Enabled == False: #For some reason when I put in 2 or 3 it did it 5 times, however 1 worked.
     if (User != Users[0][0]) and (Pass != Users[0][1]):
       Tries += 1
       print("This information is incorrect, please try again. Current tries:", Tries)
       User = input("Please insert your username\n")
       Pass = input("Please insert your password\n")
     else:
       Enabled = True
  
  
   if Tries >= 2:
       print("You have entered the wrong data too many times.")
   else:
       print("Login Accepted.")
       Menu()

print("User is", Users[0][0], "\nPassword is", Users[0][1])
LogIn()



print("Program terminated. Have a nice day! C:")
