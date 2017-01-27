#!/usr/bin/python
import os
import shutil
import sys
import tinify
import subprocess

tinify.key = "9x6LTmWtvaeaMcb3Bna5cwIxEctgP5Pv"

def get_size_in_kilobytes(start_path = '.', directory_list = None):
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
            if os.path.isdir(destination_dir): # Delete the _tiny directory if it exists.
                shutil.rmtree(destination_dir)
            shutil.copytree(source_dir, destination_dir)
            print("\nCompressing... This might take a while.")
            for root, subfolders, files in os.walk(destination_dir): #Walk the directory
                for file in files:
                    if file.endswith(".png"):
                        source_full_path = root + "/" +file # Gotta get the full path
                        sys.stdout.write(".")
                        sys.stdout.flush()
                        tinify.from_file(source_full_path).to_file(source_full_path) # This will fail if you run out of compression calls to the TinyPNG API.
            print("\nDone!")

            # Parsing and assigning variables so that printing doesn't look like a complete mess
            compressed_dir_size = get_size_in_kilobytes(source_dir)
            uncompressed_dir_size = get_size_in_kilobytes(destination_dir)
            size_difference_between_dirs = compressed_dir_size - uncompressed_dir_size
            shortened_source_name = source_dir[source_dir.rfind('/')+1:len(source_dir)]
            shortened_destination_name = destination_dir[destination_dir.rfind('/')+1:len(destination_dir)]
            table_label = "Size in KB\tName"

            display_list = ["\nSize in KB\tName",
            str(compressed_dir_size) + "\t\t" + shortened_source_name,
            str(uncompressed_dir_size) + "\t\t" + shortened_destination_name,
            str(size_difference_between_dirs) + "\t\tDifference"]
            maximum_length = len(max(display_list, key=len))
            for label in display_list:
                print(label)
                print("-" * (maximum_length + 10))
    else:
        print("Invalid arguments.")

if __name__ == "__main__":
    main()
