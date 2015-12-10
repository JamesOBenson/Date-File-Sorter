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
#


import shutil
import os
import glob

try:
    # Move all files with a year of 2010 to 2020
    for years in range(2010,2021):
        # Move every month of the year
        for months in range(1,13):
            # Move every possible day of the month
            for days in range(1, 32):
                # Day string
                day = str("%04d-%02d-%02d" %(years, months, days))
                # Look at only the files that exist
                Bool = glob.glob(day+'*')
                # For the files that exist
                for bools in Bool: 
                    # Check if folder exists & create the folder if it doesn't
                    if not os.path.exists(day):
                        os.makedirs(day)

                # Set source and Destination paths
                source = os.listdir("/Some/Source/Path/containing/files")
                destination = "/some/destination/path/to/create/the/folders/"+day
                # Move files
                for files in source:
                    if files.startswith(day) and files.endswith(".jpg"):
                        shutil.move(files,destination)
except:
    print "Failed moving images"