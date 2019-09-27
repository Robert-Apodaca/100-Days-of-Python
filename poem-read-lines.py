#output_file = open("poem.txt", "r")
#for line in output_file.readlines():
#    print(line)
#output_file.close()

# with statement

#with open("poem.txt", "r") as input_file:
#    for line in input_file.readlines():
#        print(line)

#with open("poem.txt", "r") as source, open("poem-copied.txt", "w") as dest:
#    for line in source.readlines():
#        dest.write(line)

#append

with open("poem-copied.txt", "a") as appended_file:
    appended_file.writelines("\nAdd this!")
