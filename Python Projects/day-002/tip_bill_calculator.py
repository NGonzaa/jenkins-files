#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
bill = float(input("What is the total bill?: $"))
tip = 1 + (int(input("How much tip are you leaving? (in percent): ")) / 100)
people = int(input("How many people are paying?: "))

to_pay = bill * tip
per_person = to_pay / people

rounded_total = "{:.2f}".format(to_pay)
rounded_per_person = "{:.2f}".format(per_person)
print(f"The total to pay is ${rounded_total}, and each person pays ${rounded_per_person}.")