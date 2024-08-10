import os
import shutil
import zipfile

def extract_fonts(zip_file_path, destination_folder):
    print(f"Extracting fonts from {zip_file_path} to {destination_folder}/Helvetica...")
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        for member in zip_ref.namelist():
            if member.endswith(('.otf', '.ttf', '.woff', '.woff2')):
                font_file_name = os.path.basename(member)
                target_folder = os.path.join(destination_folder, 'Helvetica')
                os.makedirs(target_folder, exist_ok=True)
                target_path = os.path.join(target_folder, font_file_name)
                print(f"Extracting {font_file_name} to {target_path}...")
                with zip_ref.open(member) as source, open(target_path, 'wb') as target:
                    shutil.copyfileobj(source, target)
    print("Extraction complete.")

if __name__ == "__main__":
    zip_file_path = "C:\\Users\\Admin\\Downloads\\ForPy.zip"
    destination_folder = "C:\\Users\\Admin\\Downloads\\PyExtracted"

    extract_fonts(zip_file_path, destination_folder)
