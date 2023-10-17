year = eval(input("Enter birth year: "))
sign = year % 12

if sign == 8:
    zodiac = "dragon"
elif sign == 9:
    zodiac = "snake"
elif sign == 10:
    zodiac = "horse"
elif sign == 11:
    zodiac = "sheep"
elif sign == 0:
    zodiac = "monkey"
elif sign == 1:
    zodiac = "rooster"
elif sign == 2:
    zodiac = "dog"
elif sign == 3:
    zodiac = "pig"
elif sign == 4:
    zodiac = "rat"
elif sign == 5:
    zodiac = "ox"
elif sign == 6:
    zodiac = "tiger"
else:
    zodiac = "rabbit"

print("Your Chinese zodiac sign is " + zodiac.title())
