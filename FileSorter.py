#  This code is written for python 2.7.10
#  Copyright 2015 James Benson

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Execution: python2 FileSorter.py
#
# DESCRIPTION: 
#   A folder contains several date-time stamped files in the format of:
#              2015-12-10-17-15-56.jpg
#   This program will look into the folder, seperate each collection of files
#   by year, month, and day and automatically create new sets of folders to 
#   contain each of them.  No empty folders will be created.  Any additional 
#   files created where a folder already exists will be added to the existing
#   folder.
#
#  Note: This is a nice sorting program which can be used for photos or logs 
#  which are created every X seconds and automatically sort them.
#

#   import pdb; pdb.set_trace()
import shutil
import os
import glob


# Check each file in directory
# Find the appropriate folder name
# If folder exists; put file in folder
# If folder doesn't exist, create folder and put file in it


def get_all_files_in_directory_if_jpg():
    """Returns a list of files with .jpg extension
    """
    all_directories = glob.glob('/Users/james/Downloads/*.jpg')
    if all_directories == []:
        print "There are no jpg files in this directory."
    else:
        print "jpg files are {0}".format(all_directories)
    return all_directories
    
    
def get_folder_name(file_name):
    """Returns a folder name format given a file name
    """
    new_file_name = file_name.split('/')[-1]
    folder_name = "{}-{}-{}".format(
        new_file_name[:4],
        new_file_name[5: 7],
        new_file_name[8: 10]
    )
    return folder_name
    

def does_folder_exist(folder_name, directory_path):
    """Returns True or False depending on whether a folder is in a directory
    """
    folder_list = []
    for (dirpath, dirnames, filenames) in os.walk(directory_path):
        folder_list.extend(dirnames)
        break
    folder_exists = folder_name in folder_list
    """  Debugging
    """
#    if folder_exists:
#        print("{0} is in {1}".format(folder_name, folder_list))
#    else:
#        print("{0} is in not in {1}".format(folder_name, folder_list))
    return folder_exists


def create_folder(folder_name, creation_path):
    """Create a folder in a path
    """
    print "Creating folder {0} in path {1}".format(folder_name, creation_path)
    return os.makedirs(creation_path + '/' + folder_name)
    

def put_file_in_folder(file_loc, destination):
    """Put a file in a folder
    """
    print "putting file: {0} in directory {1}".format(file_loc, destination)
    shutil.move(file_loc, destination)
    return

def start_file_movements():
    """Kick off entire process
    """
    print "Starting process"
    current_path = os.getcwd()
    print "Current path is {0}".format(current_path)
    for jpg_file in get_all_files_in_directory_if_jpg():
        folder_name = get_folder_name(jpg_file)
        if does_folder_exist(folder_name, current_path):
            folder_path = current_path + '/' + folder_name
            put_file_in_folder(jpg_file, folder_path)
        else:
            folder_path = create_folder(folder_name, current_path)
            folder_path = current_path + '/' + folder_name
            put_file_in_folder(jpg_file, folder_path)
    print "Finished process"

if __name__ == '__main__':
    start_file_movements()