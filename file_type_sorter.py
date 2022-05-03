import shutil
import os

# path variable = this is the folder we wish to organize
path = input("Enter Path: ").replace("\\", "//")

# files variable = contains a list of files in the path variable
files = os.listdir(path)

# loop through every file in the files variable
for file in files:
    filename, extension = os.path.splitext(file)
    extension = extension[1:]

    # check if the path to the folder exists, if it does, move the file to the folder
    if os.path.exists(path + '//' + extension):
        shutil.move(path + '//' + file, path + '//' + extension + '//' + file)
    else:
        # if the file didn't exist before, make the file now, based on the extension and move the file there
        os.makedirs(path + '//' + extension)
        shutil.move(path + '//' + file, path + '//' + extension + '//' + file)
