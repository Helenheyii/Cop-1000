# a program that calculates an employee's productivity bonus and prints the employee's name and bonus
employeeName= "Jenna Jenkins"
numOfShifts= 15
numOfTrans= 30
transDollarValue= 25000

productivityScore= transDollarValue/(numOfTrans*numOfShifts)
bonus= 0.00

if productivityScore<=30:
    bonus= 50.00
elif 31<= productivityScore<=69:
    bonus=75.00
elif 70<= productivityScore<=199:
    bonus=100.00
elif productivityScore>=200:
    bonus=200.00

print(f"employee Name: {employeeName}")
print(f"employee Bonus: ${bonus:.2f}")