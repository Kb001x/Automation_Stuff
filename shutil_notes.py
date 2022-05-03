import shutil

src = "C:\\Users\\Charles\\Desktop\\voice assistant"
#dst = "E:\\Unsorted Desktop Stuff\\julefort"  # do not create destination folder ahead of time!
dst = "C:\\Users\\Charles\\Desktop\\voice assistant2"

# copy all files and folders
# shutil.copytree(src=src, dst=dst) #works!!!

# same as b4, copy files only
shutil.copyfile(src=src, dst=dst)

# copy file + folder with permission bits #shutil.copy(src=src +"/filename.jpg", dst=dst)
#shutil.copy(src=src, dst=dst)