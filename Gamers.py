unit = int(input("Enter your unit: "))
if unit <= 50:
    bill = unit * 0.50
elif unit >= 51 and unit <= 100:
    bill =  25 + ((unit - 50) * 0.75)
elif unit >= 101 and unit <= 200:
    bill = 25 + 37.5 + ((unit - 100) * 1.25)
else:
    bill = 25 + 37.5 + 125 + ((unit - 250) * 150)

bill = bill + bill*0.17
print(("Totaly Bill after adding additional surcharge:",bill))