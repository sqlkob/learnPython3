from sys import argv
from os.path import exists

script, from_file, to_file = argv
print(f"Copying from {from_file} to {to_file}")

#we could do these twon on one line, how?

in_file = open(from_file)
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long")