bill = float(input("What is the total bill? "))
tip = float(input("How much tip would you like to give? 10, 12, 15 ?"))
people = float(input("How many people to split the bill? "))

tip_percentage = tip / 100
total_tip_amount = bill * tip_percentage
total_bill = total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)

print(f"Each person should pay: ${final_amount}")
