fruits = ['pear', 'pineapple', 'apple', 'orange']

print(fruits, "\n------------")

fruits.sort()
print(fruits, "\n------------")

for fruit in fruits:
    print(fruit)

print("------------")

for fruit in fruits:
    if fruit.startswith("a"):
        print(fruit)