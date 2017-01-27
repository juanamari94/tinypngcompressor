# TinyPNGCompressor

TinyPNGCompressor is a simple tool written in Python that consumes the TinyPNG API. It compresses a given directory and all of its subdirectories' PNG or JPG files.

## Requirements

- An internet connection.

- TinyPNGCompressor was built around **Python 2.7.10**, although it should work with any Python 2.7.x version, and more than likely with previous versions as well. You can download Python 2.7.13 from [python.org's official site.](https://www.python.org/downloads/release/python-2713/)

- **You have to install TiniPNG's Package with pip. You can do this by typing** `pip install --upgrade tinify` ** if it throws an error you more than likely have to use `sudo`, just so: `sudo pip install --upgrade tinify`.

## How to use

- TinyPNGCompressor is run through the console and takes two parameters from it:
    - The **full** path of the directory where the PNGs or JPGs are in.
    - An optional path called `--verbose` which will output which file has been compressed after it has been sent to TinyPNG.
    - TinyPNGCompressor will create a folder in the same directory the folder to be compressed is in, and it will have the same name with a _tiny suffix. If you compress the contents of **somefolder** the output will be **somefolder_tiny**

- Examples of how to use it
    - Navigate to the directory where tinypngcompressor.py is (or just use its path) and type:
    - `python tinypngcompressor.py [directory to be compressed path] [OPTIONAL --verbose]`
    - A real example: `python tinypngcompressor.py /Users/me/Documents/somefolderwithpngsorjpgs --verbose`
    - Without `--verbose` it would look like this: `python tinypngcompressor.py /Users/me/Documents/somefolderwithpngsorjpgs`
    - If you can assign executions permissions to the file, you can run it like this: `./tinypngcompressor.py [directory to be compressed path] [OPTIONAL --verbose]`
