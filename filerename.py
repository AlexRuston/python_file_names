from os import walk, rename

# the string we'll be removing from the file names
remove_string = "Tom Clancy's Rainbow Six  Siege "

# get all files in directory
# [] if no file
filenames = next(walk("e:\\Videos\\Tom Clancy's Rainbow Six  Siege"), (None, None, []))[2]

# count to print how many files were changed
count = 0

# loop the files
for name in filenames:
    if remove_string in name:
        # new name is base directory, plus the removed string
        new_name = name.replace(remove_string, "")
        # rename the file
        rename("e:\\Videos\\Tom Clancy's Rainbow Six  Siege\\" + name, "e:\\Videos\\Tom Clancy's Rainbow Six  Siege\\" + new_name)
        count = count + 1

# print a count of files renamed
print(count, " files renamed")