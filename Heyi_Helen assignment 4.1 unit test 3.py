"""
This program calculates prices for custom house signs.
"""

# Declare and initialize variables here.
charge= 35.00
numChars= 20
color= "gold"
woodType= "pine"
# Charge for this sign.
# Number of characters.
if numChars > 5:
 extraCharCost = numChars-5
charge+= extraCharCost*4.00
# Color of characters.
if color=="gold":
 charge+= 15.00
# Type of wood.
if woodType=="oak":
 charge += 20.00

# Write assignment and if statements here as appropriate.

# Output Charge for this sign.
print("The charge for this sign is $" + str(charge))