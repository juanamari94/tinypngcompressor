#!/usr/bin/python
import os
import shutil
import sys
import tinify
import subprocess

tinify.key = "9x6LTmWtvaeaMcb3Bna5cwIxEctgP5Pv"

def get_size_in_kilobytes(start_path = '.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size / 1000

# Receives source directory and creates a _tiny directory in the same parent directory.

def main():
    # Gotta validate that user input

    if len(sys.argv) == 2:
        source_dir = sys.argv[1]

        if not os.path.isdir(source_dir): # If source path doesn't exist.
            print("Source directory does not exist.") # Notify it.
        else:
            destination_dir = source_dir + "_tiny"
            shutil.copytree(source_dir, destination_dir)
            print("\nCompressing... This might take a while.")
            for root, subfolders, files in os.walk(destination_dir): #Walk the directory
                for file in files:
                    if file.endswith('.png'):
                        source_full_path = root + "/" +file # Gotta get the full path
                        tinify.from_file(source_full_path).to_file(source_full_path)
            print("Done!\n")
            print("Differences in directories:")
            print("Uncompressed directory: " + str(get_size_in_kilobytes(source_dir)) + " KB")
            print("Comrpessed directory: " + str(get_size_in_kilobytes(destination_dir)) + " KB")
    else:
        print("Invalid arguments.")

if __name__ == "__main__":
    main()
