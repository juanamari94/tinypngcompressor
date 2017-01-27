#!/usr/bin/python
import os
import shutil
import sys
import tinify

tinify.key = "9x6LTmWtvaeaMcb3Bna5cwIxEctgP5Pv"

# Receives source directory and creates a _tiny directory in the same parent directory.

def main():
    # Gotta validate that user input
    if len(sys.argv) == 2:
        source_dir = sys.argv[1]

        if not os.path.isdir(source_dir): # If source path doesn't exist.
            print("Source directory does not exist.") # Notify it.
        else:
            destination_dir = source_dir + "_tiny"
            print(tinify.key)
            shutil.copytree(source_dir, destination_dir)
            for root, subfolders, files in os.walk(destination_dir):
                for file in files:
                    print(file)
    else:
        print("Invalid arguments.")

if __name__ == "__main__":
    main()
