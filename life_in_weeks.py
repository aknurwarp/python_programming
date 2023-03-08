age = input("What is your current age? ")

age = int(age)
fixed_age = 90 
x = (365 * fixed_age) - (365 * age)
y = (52 * fixed_age) - (52 * age)
z = (12 * fixed_age) - (12 * age)

print(f"You have {x} days, {y} weeks, and {z} months left.")
