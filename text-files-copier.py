#! /usr/bin/python3

# The purpose of this Python script is to go through a folder, copy all the text within
# a designated file type, and write them into a designated text file. The script labels
# and formats the copied files based on their folder locations and file names.

# Can read files within sub-sub-directories.

import os
import time
import sys


# Adjust these variables

# The file you are writing or appending to
write_file = open("/home/zhiwen/Desktop/notes.txt", "a+")

# Extension of file that will be read
extension = ".py"

# Path to initial directory
folder = "Python 3 Essential Training"
folder_directory_path = "/media/removable/SD Card/Lynda/"
initial_directory_path = folder_directory_path + folder



# copy and write entire file
def copy_file(file):
    print("### ", file, " ###", file = write_file)
    print(' ', file = write_file)
    read_file = open(file, 'r')
    
    # iterate through every line in file and write
    for line in read_file:
        print(line, file = write_file, end = '')
        
    print("#==========#", file = write_file)
    print(' ', file = write_file)
    
    print('Copied {} '.format(file))
    print(' ')


# sort a directory list in alphabetical order with folders first then files
def sort_dir_list(directory_list):
    directory_list.sort()
    sorted_list = []
    
    for list in directory_list:
        if os.path.isdir(list):
            sorted_list.append(list)
            
    for list in directory_list:
        if os.path.isfile(list):
            sorted_list.append(list)
            
    return sorted_list

# create subdirectory and return its directory list
def subdirectory(directory):
    # set directory
    os.chdir(directory)
    
    # get list and sort
    sub_directory_list = os.listdir()
    sub_directory_list = sort_dir_list(sub_directory_list)
    
    # write the directory name to file
    print("###### ",directory," ######", file = write_file)
    print(' ', file = write_file)
    return sub_directory_list



def main():
    # write the folder name into file
    print("######### ", folder, " #########", file = write_file)
    print(" ", file = write_file)
    
    # set working directory
    try:
        os.chdir(initial_directory_path)
    except:
        print("Invalid initial directory path")
        time.sleep(4)
        sys.exit()
        
    # create directory list and sort it
    directory_list = os.listdir(initial_directory_path)
    directory_list = sort_dir_list(directory_list)

    # iterate through all folders and files down to sub sub directories
    for directory in directory_list:
        os.chdir(initial_directory_path)
        if os.path.isdir(directory):
            sub_directory_list = subdirectory(directory)
            sub_directory_path = os.getcwd()
            for sub_directory in sub_directory_list:
                os.chdir(sub_directory_path)
                if os.path.isdir(sub_directory):
                    sub_sub_directory_list = subdirectory(sub_directory)
                    for sub_sub_directory in sub_sub_directory_list:
                        if sub_sub_directory.endswith(extension):
                            copy_file(sub_sub_directory)
                            
                elif sub_directory.endswith(extension):
                    copy_file(sub_directory)
                else: pass
                
        elif directory.endswith(extension):
            copy_file(directory)
        else: pass

    # close file
    write_file.close()

if __name__ == "__main__":
    main()

