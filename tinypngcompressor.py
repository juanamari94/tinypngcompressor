#!/usr/bin/python
import os
import shutil
import sys
import tinify
import subprocess
import traceback

tinify.key = None

# Credit to monkut from Stackoverflow for this function. http://stackoverflow.com/a/1392549/5655734
def get_size_in_kilobytes(start_path = '.', directory_list = None):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size / 1000

# You have to install the tinify package with pip: pip install --upgrade tinify
# If that doesn't work run it with sudo: sudo pip install --upgrade tinify
# For more information: https://github.com/tinify/tinify-python
# Receives source directory and creates a _tiny directory in the same parent directory.
# You NEED to provide your own tinify API Key. Unless you pay (something around 0.009c for each compression) after 500 free API calls.
# https://tinypng.com/developers to retrieve your key.

def main():
    # Gotta validate that user input
    args_len = len(sys.argv)
    if args_len >= 2 and args_len <= 3:

        source_dir = sys.argv[1]
        if not os.path.isdir(source_dir): # If source path doesn't exist.
            print("\nSource directory does not exist. Provide the full path of the directory as the first parameter when you run the script.") # Notify it.
            return # Finish execution.

        print("\nWelcome to TinyPNGCompressor!\nPlease enter a TinyPNG API Key.")
        tinify.key = raw_input()

        is_verbose = None
        try:
            is_verbose = sys.argv[2]
        except IndexError:
            print("By default Verbosity is disabled.")

        destination_dir = source_dir + "_tiny"

        error_string = ""

        if os.path.isdir(destination_dir): # Delete the _tiny directory if it exists.
            shutil.rmtree(destination_dir)
        shutil.copytree(source_dir, destination_dir) # Create a copy of the tree
        print("\nCompressing... This might take a while.")
        for root, subfolders, files in os.walk(destination_dir): #Walk the directory
            for file in files:
                if file.endswith(".png") or file.endswith(".jpg"):
                    source_full_path = root + "/" +file # Gotta get the full path
                    try:
                        tinify.from_file(source_full_path).to_file(source_full_path) # This will fail if you run out of compression calls to the TinyPNG API.
                        if is_verbose is not None and is_verbose.lower() == "--verbose":
                            print("Compressed " + file)
                        else:
                            sys.stdout.write(".")
                            sys.stdout.flush()
                    except tinify.errors.AccountError, e:
                        print str(e)
                        return
                    except tinify.errors.ServerError, e:
                        print(str(e))
                        error_string += "\nThere was an error compressing file: " + file + ": " + str(e)

        if(error_string != ""):
            print(error_string)

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
        print("You can find the directory with the compressed files in: " + destination_dir)
    else:
        print("Invalid arguments.")

if __name__ == "__main__":
    main()
