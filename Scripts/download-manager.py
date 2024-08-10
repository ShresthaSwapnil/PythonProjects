import os
import shutil

downloads_folder = "C:\\Users\\Admin\\Downloads"  # Replace with the actual path to your downloads folder

# Create folders if they don't exist
folders = ["zip", "documents", "images", "other"]
for folder in folders:
    folder_path = os.path.join(downloads_folder, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# List all files in the downloads folder
files = [f for f in os.listdir(downloads_folder) if os.path.isfile(os.path.join(downloads_folder, f))]

# Define file types for each folder
file_types = {
    "zip": [".zip", ".rar"],
    "documents": [".pdf", ".doc", ".docx", ".txt"],
    "images": [".jpg", ".jpeg", ".png", ".gif"],
}

# Move files to respective folders
for file in files:
    file_path = os.path.join(downloads_folder, file)
    for folder, extensions in file_types.items():
        if any(file.lower().endswith(ext) for ext in extensions):
            destination_folder = os.path.join(downloads_folder, folder)
            shutil.move(file_path, os.path.join(destination_folder, file))
            print(f"Moved {file} to {folder} folder.")
            break
    else:
        destination_folder = os.path.join(downloads_folder, "other")
        shutil.move(file_path, os.path.join(destination_folder, file))
        print(f"Moved {file} to other folder.")
