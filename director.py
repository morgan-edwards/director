import os

# Intro to CLI
print("Welcome to Director!\n\nUse this tool to automatically find files and copy them to a new folder.")

# Allows you to specificy a sub folder
source_path = './' + raw_input("Enter the source directory (blank if already there):  ")

# Choose a name for the folder you want to move the new files to
target_path = './' + raw_input("Enter a name for the new folder:  ")

# Creates that new folder
os.mkdir(target_path)

# Choose the search term to grab target files with
keyword = raw_input("Enter the file keyword you wish to target:  ")

# Create a list of all the files in the
all_files = os.listdir(source_path)

# filter out the files that match your keyword -- lower the case the it is case insensitive
to_relocate = [file for file in all_files if keyword.lower() in file.lower()]

# iterate over the name matches and move the files, while keeping track of how many
file_count = 0

for file in to_relocate:
    os.rename(source_path + '/' + file, target_path + '/' + file)
    file_count += 1

print("\n\n\n-------------------------------------------")
print("Director successfully relocated " + str(file_count) + " files")
print("-------------------------------------------")
for file in to_relocate:
    print(file)
