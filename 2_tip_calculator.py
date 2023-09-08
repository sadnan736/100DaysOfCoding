print("Welcome to the Tip Calcutator!")
bill = float(input("What was the total bill? ৳"))
persons = int(input("How many people will split the bill? "))
tip = float((input("How much tip would you like to give? Standard is 15% ")))


pperson_pay = (bill+ (bill*tip/100))/persons
pperson_pay = round(pperson_pay, 2)

print(f"Each person should pay: ৳{pperson_pay}")