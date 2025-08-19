age = 20
name = "Swaroop"
#can be used with numbers or without
print("{0} was {1} years old when he wrote his book.".format(name, age))
print("Why is {0} playing with that python?".format(name))
#without
print("{} was {} years old when he wrote his book.".format(name, age))
print("Why is {} playing with that python?".format(name))
#dont use this
print("{name} was {age} years old when he wrote his book.".format(name=name, age=age))
print("Why is {name} playing with that python?".format(name=name))