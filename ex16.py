from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want to eat that, hit RETURN")
print("if you do want that, hit return.)

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")
    line1 = input("line:1 ")
    line2 = input("line:2 ")
    line3 = input("
    ")

print("I'm going to write these")

target.write(line1)
target.write(":\n")
target.write(line2)
target.write("\n")
target.write("line3")
target.write("\n")

printI("And finally, we close it.")
target.close()
# This is a test