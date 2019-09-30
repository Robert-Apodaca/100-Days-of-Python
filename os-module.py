#import os

#path = "C:/Users/robert/PycharmProjects"

#contents = os.listdir(path + "/untitled")

#print(contents)

#for x in contents:
#    print(path + "/" + x)

import os
import glob

path = "E:/Users/Rob/Desktop"

for current_folder, subfolders, file_names in os.walk(path):
    possible_files = os.path.join(current_folder, "*/*.png")

    for file_name in glob.glob(possible_files):
        print(file_name)




#    for file_name in file_names:
#        if file_name.lower().endswith(".png"):
#            #file_name = "/" + file_name
#            full_path = os.path.join(path, file_name)
#            new_file_name = full_path[:-4] + "_backup.png"
#            os.rename(full_path, new_file_name)

