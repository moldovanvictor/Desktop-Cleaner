# Desktop Cleaner

Desktop Cleaner is a script for organizing a directory based on file types.

### app.py

This file contains the following functions:

- **getAllFiles(directory)**: Returns a list of all files in the given directory.
- **makeFolders(dic, directory)**: Creates folders for each file type (based on extension) if they don't exist, and returns a dictionary with folder paths.
- **organizeFiles(directory)**: Organizes the files in the specified directory by moving them into folders based on their file extension.

### run.py

This file provides a command-line interface (CLI) for running the file organizer. It uses the `argparse` library to parse the directory path from the user's input and runs the `organizeFiles` function.

## Prerequisites

- Python 3.x
- Required Python libraries: `os`, `shutil`, and `argparse`. These are all part of Python's standard library, so no additional installation is necessary.

## Running the script

1. Clone or download this repository.
2. Open a terminal and navigate to the directory containing `run.py`.
3. Run the following command to organize a directory of files:

```bash
python run.py -d <absolute-path-to-directory>
```

### For Example
```bash
python run.py -d "C:/Users/YourUsername/Downloads"
```

### Example
Given a folder structure like this:
```bash
Downloads
├── file1.txt
├── file2.jpg
├── file3.txt
└── script.py
```

After running the script, the structure will be:
```bash
Downloads
├── .txt
│   ├── file1.txt
│   └── file3.txt
├── .jpg
│   └── file2.jpg
└── .py
    └── script.py
```

### Notes
The script will skip any files that already exist in the target directory with the same name. It will notify you if a file was skipped due to a name conflict.
If two files have the same name but different contents, rename one of them before running the script.

### License
This project is licensed under the MIT License. See the LICENSE file for details.



