import os

def remove_prefix_from_mp3(directory):
    # List all files in the directory
    files = os.listdir(directory)
    
    # Filter only .mp3 files that start with 'y2mate.is - '
    mp3_files = [file for file in files if file.endswith('.mp3') and file.startswith('y2mate.is - ')]
    
    # Rename each file
    for file in mp3_files:
        old_name = os.path.join(directory, file)
        new_name = os.path.join(directory, file.replace('y2mate.is - ', '', 1))
        os.rename(old_name, new_name)
        print(f"Renamed '{old_name}' to '{new_name}'")

# Specify the directory containing the .mp3 files
directory = 'E:\\Music'

# Call the function
remove_prefix_from_mp3(directory)