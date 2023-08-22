#Write a Python program to check if a given function is a generator or not. Use types.GeneratorType()
import types
def a(x):
    yield x
        
def b(x):
    return x

def add(x, y):
    return x + y

print(isinstance(a(456), types.GeneratorType))
print(isinstance(b(823), types.GeneratorType))
print(isinstance(add(8,2), types.GeneratorType))


#Write a Python program to construct a seeded random number generator, also generate a float between 0 and 1, excluding 1.
import random
print("Construct a seeded random number generator:")
print(random.Random().random())
print(random.Random(0).random())
print("\nGenerate a float between 0 and 1, excluding 1:")
print(random.random())



#Write a Python program to write (without writing separate lines between rows) and read a CSV file with a specified delimiter. Use csv.reader
import csv     
fw = open("test.csv", "w", newline='')
writer = csv.writer(fw, delimiter = ",")
writer.writerow(["a","b","c"])
writer.writerow(["d","e","f"])
writer.writerow(["g","h","i"])
fw.close()
 
fr = open("test.csv", "r")
csv = csv.reader(fr, delimiter = ",")
for row in csv:
  print(row) 
fr.close()