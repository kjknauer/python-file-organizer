import os
import shutil

# Folder you want to organize
folder_path = r"C:\Users\kayla\OneDrive\Desktop\TestFolder"

  # Change this to any folder you want

# File type categories
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Audio": [".mp3", ".wav"],
    "Videos": [".mp4", ".mov"],
    "Archives": [".zip", ".rar"],
    "Code": [".py", ".js", ".html", ".css"]
}

# Create folders if they don't exist
for folder in file_types:
    folder_path_full = os.path.join(folder_path, folder)
    if not os.path.exists(folder_path_full):
        os.makedirs(folder_path_full)

# Sort files
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)

    if os.path.isfile(file_path):
        file_ext = os.path.splitext(filename)[1].lower()

        for folder, extensions in file_types.items():
            if file_ext in extensions:
                shutil.move(file_path, os.path.join(folder_path, folder, filename))
                print(f"Moved {filename} to {folder}")
                break
