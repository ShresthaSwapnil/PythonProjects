import os
import shutil

def move_pptx_files(source_dir):
    # Iterate through files in the source directory
    for filename in os.listdir(source_dir):
        if (filename.endswith('.pptx') or filename.endswith('.pdf')):
            # Form paths for source file
            src_path = os.path.join(source_dir, filename)
            
            # Create destination directory if it doesn't exist
            dest_dir = os.path.join(source_dir, 'BDA101 Tutorials')
            if not os.path.exists(dest_dir):
                os.makedirs(dest_dir)

            # Move the file to the destination directory
            dest_path = os.path.join(dest_dir, filename)
            shutil.move(src_path, dest_path)
            print(f"Moved {filename} to {dest_dir}")

# Specify source directory
source_directory = 'C:\\Users\\Admin\\Desktop\\3rd Semester'

# Call the function to move .pptx files
move_pptx_files(source_directory)
