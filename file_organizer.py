import os
import shutil
from pathlib import Path

def organize_files(src_dir):
    # Create destination directories for each file type
    dest_dirs = {
        ".pdf": "pdf_files",
        ".docx": "word_files",
        ".jpg": "image_files",
        ".mp3": "audio_files",
        ".mp4": "video_files",
        ".avi": "video_files",
        ".mov": "video_files",
        ".webm": "video_files",
        ".mkv": "video_files",
        ".avchd": "video_files",
        ".zip": "archive_files",
        ".txt": "text_files",
        ".py": "python_files",
        ".exe": "executable_files",
        ".dll": "dll_files",
        ".iso": "iso_files",
        ".rar": "rar_files",
        ".7z": "7z_files",
        ".tar": "tar_files",
        ".gz": "gz_files",
        ".bz2": "bz2_files",
        ".xz": "xz_files",
        ".7z": "7z_files",
        # Add more file extensions as needed
    }

    # Create destination directories if they don't exist
    for dir_name in dest_dirs.values():
        dir_path = os.path.join(src_dir, dir_name)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

    # Iterate through files in the source directory
    for file_name in os.listdir(src_dir):
        # Get the file extension
        file_ext = Path(file_name).suffix.lower()

        # Check if the file extension is in the destination directories
        if file_ext in dest_dirs:
            src_path = os.path.join(src_dir, file_name)
            dest_dir = os.path.join(src_dir, dest_dirs[file_ext])
            dest_path = os.path.join(dest_dir, file_name)

            # Move the file to the appropriate destination directory
            shutil.move(src_path, dest_path)
            print(f"Moved {file_name} to {dest_dir}")

    print("File organization completed.")

# Prompt the user to enter the source directory path
src_dir = input("Enter the path to the directory you want to organize: ")

# Check if the source directory exists
if os.path.exists(src_dir):
    organize_files(src_dir)
else:
    print("The specified directory does not exist.")