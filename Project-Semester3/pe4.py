# Prompt the user for their age
age = int(input("Please enter your age: "))

# Check the age and inform about discounts
if age <= 19:
    print("You qualify for student discounts!")
elif 20 <= age <= 54:
    print("You qualify for no age discounts.")
else:
    print("You can receive senior discounts!")
