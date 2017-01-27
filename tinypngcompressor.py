#!/usr/bin/python
import os
import shutil
import sys
import tinify
import subprocess

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
            shutil.copytree(source_dir, destination_dir)
            print("\nCompressing... This might take a while.")
            for root, subfolders, files in os.walk(destination_dir): #Walk the directory
                for file in files:
                    if file.endswith('.png'):
                        source_full_path = root + "/" +file # Gotta get the full path
                        print("Compressing file: " + file)
                        tinify.from_file(source_full_path).to_file(source_full_path)
            print("Done!\n")
            script_path = os.path.dirname(os.path.realpath(__file__)) # Get script path
            subprocess.call(script_path + "/sizecalculator.sh " + source_dir + " " + destination_dir, shell=True) # Running shell command because it's faster to get size this way.
    else:
        print("Invalid arguments.")

if __name__ == "__main__":
    main()
