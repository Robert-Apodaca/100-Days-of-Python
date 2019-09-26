#output_file = open("hello.txt", "w")
#output_file.writelines("This is my first file.")
#output_file.close()

#list of lines to be written all at once

#output_file = open("hello.txt", "w")

#lines_to_write = [
#    "This is my file.",
#    "\nThere are many like it,",
 #   "\nbut this one is mine.",
  #  ]
#output_file.writelines(lines_to_write)
#output_file.close()

#output_file = open("hello.txt", "a")
#output_file.writelines("\nNON SEQUITUR")
#output_file.close()

#read mode
#input_file = open("hello.txt", "r")
#print(input_file.readlines())
#input_file.close()
#
input_file = open("hello.txt", "r")

for line in input_file.readlines():
    print(line)

input_file.close()

#save .readlines

lines_in_file = input_file.readlines()

#shortcut using with
with open("hello.txt", "r") as input_file:
    for line in input_file.readlines():
        print(line)

#multiple variables and multiple files

with open("hellot.txt", "r") as source, open("hi.txt", "w") as dest:
    for line in source.readlines():
        dest.write(line)