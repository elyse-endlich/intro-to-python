from collections import OrderedDict

# converting roman to arabic
numeral = input("Write in your Roman numeral!")

rom2arab = {"I": 1, "X": 10, "C": 100, "M": 1000, "V": 5, "L": 50, "D": 500}
total = 0

for char in numeral:
    if char in rom2arab:
        total += rom2arab[char]
    else:
        print("Input invalid. Valid characters: I, V, C, D, X, M, L")
print(total)

# arabic to roman

roman = OrderedDict([
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I"),
])

number = input("Please enter a number you would like to convert.")
numeral = ""

for key in roman:
    count = int(number) // int(key)
    number = int(number) - (int(key) * count)
    numeral = numeral + (roman.get(key) * count)

print(numeral)
