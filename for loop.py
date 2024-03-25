numbers = [1, 2, 3, 4, 5]
print(numbers)
for item in numbers:   # print indivitual number
    print (item)
    if item <2:
        break

for x in "banana":
    print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

  for x in range(6):  # range value 0 to 5
      print(x)
print("done")
for x in range(2,6):  #which means values from 2 to 6 (but not including 6)
    print(x)
print("done")

for x in range(2, 30, 3):
    print(x)
print( "Done 2, 30, 3")

for x in range(6):
    print(x)
else:                     #Print all numbers from 0 to 5, and print a message when the loop has ended
    print("Finally Finished!")

print("else")

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]  #Print each adjective for every fruit:

for x in adj:
  for y in fruits:
    print(x, y)

for x in [0, 1, 2]:
  pass
print ( "for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.")


