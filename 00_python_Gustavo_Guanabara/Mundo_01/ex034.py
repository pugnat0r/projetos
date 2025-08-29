wage = int(input("How much is your wage?  "))

if wage > 1250:
    newwage = wage + (wage*0.10)
    print(newwage)

else:
    newwage = wage + (wage*0.15)
    print(newwage)