# Python File Organizer

The Python File Organizer is a simple yet powerful script that helps you keep your files organized and easily accessible. It automatically sorts files in a directory based on their file types and moves them into separate folders.

## Features

- Organizes files based on their file extensions (e.g., .pdf, .docx, .jpg) you can add more
- Creates separate directories for each file type
- Moves files into their respective directories
- Supports customization for additional file extensions

## Usage

1. Clone or download the repository to your local machine.
2. Open a terminal or command prompt and navigate to the directory containing the `file_organizer.py` script.
3. Run the script with the following command:

```
python file_organizer.py
```

4. When prompted, enter the path to the directory you want to organize.
5. The script will create separate directories for the specified file types and move the corresponding files into those directories.
6. Once completed, you'll see a "File organization completed" message in the terminal.

## Customization

You can easily customize the script to suit your needs by modifying the `dest_dirs` dictionary in the `file_organizer.py` file. Add or remove key-value pairs to include or exclude file extensions and their corresponding destination directory names.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## Acknowledgments

- [Python](https://www.python.org/) - The programming language used for this project.
- [os](https://docs.python.org/3/library/os.html) - Python module for interacting with the operating system.
- [shutil](https://docs.python.org/3/library/shutil.html) - Python module for file operations.
- [pathlib](https://docs.python.org/3/library/pathlib.html) - Python module for handling file paths.
