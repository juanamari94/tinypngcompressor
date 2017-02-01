# TinyPNGCompressor

TinyPNGCompressor is a simple tool written in Python that consumes the TinyPNG API. It compresses a given directory and all of its subdirectories' PNG or JPG files.

- If you'd like to use the somewhat "experimental" (but not really experimental) version that has the **added feature of retrying for failed files**, check out the other branch (feature/retries-for-failed-files)

## Requirements

- An internet connection.

- TinyPNGCompressor was built around **Python 2.7.10**, although it should work with any Python 2.7.x version, and more than likely with previous versions as well. You can download Python 2.7.13 from [python.org's official site](https://www.python.org/downloads/release/python-2713/). You can check your Python version by running `python --version` in your console.

- **You have to install TinyPNG's Package with pip. You can do this by typing** `pip install --upgrade tinify` if it throws an error you more than likely have to use `sudo`, just so: `sudo pip install --upgrade tinify`.

- **You need a TinyPNG API Key which you can get by making a Developer Account at [TinyPNG](https://tinypng.com/developers)**. It will send you an email with a link to your dashboard where the API Key will be.

## How to use

- TinyPNGCompressor is run through the console and takes two parameters from it:
    - The **full** path of the directory where the PNGs or JPGs are in.
    - An optional parameter called `--verbose` which will output which file has been compressed after it has been sent to TinyPNG.
    - TinyPNGCompressor will create a folder in the same directory the folder to be compressed is in, and it will have the same name with a _tiny suffix. If you compress the contents of **somefolder** the output will be **somefolder_tiny.**

- Examples of how to use it
    - Navigate to the directory where tinypngcompressor.py is (or just use its path) and type:

    `python tinypngcompressor.py [directory to be compressed path] [OPTIONAL --verbose]`
    - A real example:

    `python tinypngcompressor.py /Users/me/Documents/somefolderwithpngsorjpgs --verbose`
    - Without `--verbose` it would look like this:

    `python tinypngcompressor.py /Users/me/Documents/somefolderwithpngsorjpgs`
    - If you can assign execution permissions to the file, you can run it like this (you can assign it with `chmod 754 tinypngcompressor.py`)

    `./tinypngcompressor.py [directory to be compressed path] [OPTIONAL --verbose]`

- **After you've started running the program, it will ask for an API Key which you must provide in order to compress the file.**

- **If the script takes too long before it has started compressing, it more than likely has something to do with the amount of files that the script has to copy in order to create a cloned directory.** I recommend that you use the directory with the assets as the root directory rather than the entire project.

## Details

- TinyPNGCompressor will create a copy of the directory and start compressing that copy, leaving the original directory unmodified.
- If the copy with the _tiny suffix already exists, it will delete it and start all over.
- Due to the nature of the operations that are performed, such as copying the directory and processing it when sent to TinyPNG, the compressed files' metadata might change.
- Sometimes the API will fail to compress a file and return an error. Out of around 250 files it happened with two in my case. Usually just uploading the files with errors to [TinyPNG by hand](https://tinypng.com) will work.
- From behind the scenes, the script is **recurvise**, you can see this by checking out the `os.walk` and `shutil.copytree` and `shutil.rmtree`.
