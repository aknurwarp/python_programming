print("Welcome to the Tip Calculator")

bill = float(input("What is your bill? $"))
tip = int(input("How much tip would you like to give?10, 12, or 15? "))
peaple = int(input("how many peaple to split the bill? "))  

total_bill = bill + ((tip / 100) * bill)
bill_per_person = total_bill / peaple
#final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)
                    
print(f"Each person should pay: ${final_amount}")
