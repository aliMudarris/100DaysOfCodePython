#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculater.")

bill = float(input("What was the total bill? $"))
tip = int(input("how much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

percent_tip = tip / 100
total_tip = bill * percent_tip
total_bill = bill + total_tip
total_per_person = total_bill / people
final_amount = "{:.2f}".format(total_per_person)


print(f"Each person should pay: ${final_amount}")
