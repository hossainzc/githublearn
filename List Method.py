numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print( numbers)
numbers.remove(4)
print ( numbers)
numbers.insert(0, -1)
print ( numbers)
numbers.remove(3)
print(numbers)
numbers.clear()
print(numbers)


fruits = ["apple", "banana", "cherry"]
fruits.insert(1,"lemon")
print(fruits[-1])
print(fruits[2:6])
print(len(fruits))


print("Automating with Python is fun!")

print(12/(1+2)+2**2)

print(60*24)

print(26**3)


download_size_kb = 200*1024
total_computers = 200.0
total_kbs = download_size_kb*total_computers
print(total_kbs)


print(type("a"))
print(type(2))
print(type(2.5))


def my_function(name, department):
  print("Welcome " + name)
  print("You are part of " + department )
my_function("Tony", "IT support")