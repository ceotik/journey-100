print("Welcome to the Tip Calculator!")

bill = float(input("Enter the total bill: "))
tip_percent = int(input("Tip percentage (e.g. 10, 12, 15): "))
people = int(input("How many people are splitting the bill? "))

tip_amount = bill * (tip_percent / 100)
total = bill + tip_amount
per_person = total / people

print(f"\nTotal bill (with tip): {total:.2f}")
print(f"Each person should pay: {per_person:.2f}")

