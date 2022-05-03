import shutil
import os
import fnmatch

folder = input("Enter Path: ").replace("\\", "//")  # add \ to the end, CLI
# folder = "C://Users//Charles//Documents//pdf//pdf//"  # for speedy testing

search_term = input("Enter Search Term: ")  # add * to the end, Regex
# search_term = "Coursera*"  # for speedy testing

dest_folder = input("Enter Destination Folder: ")
# dest_folder = "Coursera"  # for speedy testing

for file in os.listdir(folder):
    if os.path.isfile(folder + file):
        if os.path.isfile(folder + file):
            if fnmatch.fnmatch(file, search_term):
                # print(file) # if theres an file name match it can be logged or printed here. Conditionals to follow
                if os.path.exists(folder + '//' + dest_folder):
                    print("Moving '{}' to '{}' Folder".format(file, dest_folder))
                    shutil.move(folder + file, folder + dest_folder)
                else:
                    print("{} Folder Created.".format(dest_folder))
                    # if the file didn't exist before, make the file now, based on the extension and move the file there
                    os.makedirs(folder + dest_folder)
                    shutil.move(folder + file, folder + dest_folder)
