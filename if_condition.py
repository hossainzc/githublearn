temperature = 6

if temperature > 30:
    print("it's a hot day")
    print("Drink water")
elif temperature > 20:
    print("it is nice day")
elif temperature > 10:
    print("it is bit cold")
else:
    print ("it is cold")
print("Done")


weight= int(input("Weight: "))
unit=input ("(K)g or (L)bs :" )
if unit.upper()== "L":
    converted = weight * 0.453592
    print("Weight in kg: ", converted)
elif unit.upper()== "K":
    print ("Weight in kg: ", weight)
else:
    print ( "Enter K or L")
print ( "Done")

