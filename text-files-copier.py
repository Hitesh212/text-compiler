#! /usr/bin/python3

# The purpose of this Python script is to transverse a directory, copy all the text within
# designated file types, and write them into a designated file. The script labels
# and formats the copied files based on their folder locations and file names.
# Can read files within sub x4 directories

import os
import sys
import re

## Globals
# adjust these variables

# the file you are writing or appending to
write_file_name = "/home/zhiwen/Desktop/copier-test.txt"
mode = "w"
# check to see if there currently is a file of same name
if os.path.isfile(write_file_name):
    replace = input("{} is already a file, to replace file, input 'y': ".format(write_file_name))
    if replace != 'y':
        print("Not replacing")
        sys.exit()
write_file = open(write_file_name, mode)

# file extensions that will be read
extension = (".py",".html",".js")

# number of sub directory levels to transverse [0-4]
level = 4

# path to initial directory
folder = ""
folder_directory_path = "/media/removable/SD Card/Lynda/" # needs a / at end
initial_directory_path = folder_directory_path + folder

# keywords to avoid reading or opening. Case sensitive. List None if not using.
exclude_file = None
exclude_folder = None

# initial for amount of files copied
count = 0



## Functions
        
# tests to make sure the globals are valid
def tests():
    # initial directory test and set initial directory
    try:
        os.chdir(initial_directory_path)
    except:
        print("Invalid initial directory path")
        sys.exit()

    # exclude file keyword test
    global patternfile
    if exclude_file != None:
        try:
            patternfile = re.compile(exclude_file)
        except:
            print("Invalid file keyword")
            sys.exit()
            
    # exclude folder keyword test
    global patternfolder
    if exclude_folder != None:
        try:
            patternfolder = re.compile(exclude_folder)
        except:
            print("Invalid folder keyword")
            sys.exit()


# exclude directories from directory list based on keywords
def exclude(directory_list):
    excluded_list = []

    if (exclude_folder != None) or (exclude_file != None):

        # patternfolder and patternfile are initalized in test()
        for directory in directory_list:
            if os.path.isdir(directory) and exclude_folder != None:
                if not re.search(patternfolder,directory):
                    excluded_list.append(directory)
                    
            elif os.path.isfile(directory) and exclude_file != None:
                if not re.search(patternfile, directory):
                    excluded_list.append(directory)
                    
            else:
                excluded_list.append(directory)
    else:
        excluded_list = directory_list
        
    return excluded_list


# sort a directory list in alphabetical order with folders first then files
def sort_dir_list(directory_list): 
    sorted_list = []
    
    directory_list.sort()

    for directory in directory_list:
        if os.path.isdir(directory):
            sorted_list.append(directory)
            
    for directory in directory_list:
        if os.path.isfile(directory):
            sorted_list.append(directory)
            
    return sorted_list


# create directory create and manipulate its directory list
def setdirectory(directory):
    # set directory
    os.chdir(directory)

    # get directory list
    directory_list = os.listdir()

    # exclude directory list
    directory_list = exclude(directory_list)
          
    # sort directory list
    directory_list = sort_dir_list(directory_list)
   
    # directory name format
    print("######## ",directory," ########", file = write_file)
    print(' ', file = write_file)

    print("Going into directory \"{}\"".format(directory))
    print()
    return directory_list


# read and write file
def copyfile(file):
    # file header format
    print("##### ", file, " #####", file = write_file)
    print(' ', file = write_file)
    read_file = open(file, 'r')
    
    # iterate through every line in file and write
    for line in read_file:
        print(line, file = write_file, end = '')

    # file ending format    
    print('_______________________________________', file = write_file)
    print(' ', file = write_file)
    print(' ', file = write_file)
    
    print('Copying "{}" '.format(file))
    print(' ')
    
    global count
    count += 1

    
## main
def main():
    tests()
                      
    # write the folder name into file
    print("############ ", folder, " ############", file = write_file)
    print(" ", file = write_file)
      
    # create directory list and sort it
    directory_list = os.listdir(initial_directory_path)
    directory_list = exclude(directory_list)
    directory_list = sort_dir_list(directory_list)
    
    # iterate through all folders and files down to sub x4 directories
    for directory in directory_list:
        os.chdir(initial_directory_path)
        if os.path.isdir(directory) and (level >= 1):
            sub_directory_list = setdirectory(directory)
            sub_directory_path = os.getcwd()
            for sub_directory in sub_directory_list:
                os.chdir(sub_directory_path)
                if os.path.isdir(sub_directory) and (level >= 2):
                    sub2_directory_list = setdirectory(sub_directory)
                    sub2_directory_path = os.getcwd()
                    for sub2_directory in sub2_directory_list:
                        os.chdir(sub2_directory_path)
                        if os.path.isdir(sub2_directory) and (level >= 3):
                            sub3_directory_list = setdirectory(sub2_directory)
                            sub3_directory_path = os.getcwd()
                            for sub3_directory in sub3_directory_list:
                                os.chdir(sub3_directory_path)
                                if os.path.isdir(sub3_directory) and (level >= 4):
                                    sub4_directory_list = setdirectory(sub3_directory)
                                    sub4_directory_path = os.getcwd()
                                    for sub4_directory in sub4_directory_list:
                                        #os.chdir(sub4_directory_path)
                                        if sub4_directory.endswith(extension):
                                            copyfile(sub4_directory)

                                elif sub3_directory.endswith(extension):
                                    copyfile(sub3_directory)
                                else: pass
                                               
                        elif sub2_directory.endswith(extension):
                            copyfile(sub2_directory)
                        else: pass
                            
                elif sub_directory.endswith(extension):
                    copyfile(sub_directory)
                else: pass
                
        elif directory.endswith(extension):
            copyfile(directory)
        else: pass

    # close file
    write_file.close()
    print("Done! Copied {} files into {}".format(count, write_file_name))
    

if __name__ == "__main__":
    main()

