# Ask user for how many burritos.
# Tell them how much their order costs.
# Don't forget 7% sales tax.
burritos = input("How many burritos do you want? ")
burritos = int(burritos)
subtotal = burritos * 6
print("Subtotal: $",subtotal)
subtotal = int(subtotal)
total = subtotal * 1.07
print("Total Price: $",total)


