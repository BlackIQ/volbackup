import zipfile
import os

def zip_directory(directory_path, zip_filename):
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, directory_path)
                zipf.write(file_path, arcname)
            
            for dir in dirs:
                dir_path = os.path.join(root, dir)
                arcname = os.path.relpath(dir_path, directory_path)

                zipf.write(dir_path, arcname + '/')

    print(f"Directory '{directory_path}' has been zipped into '{zip_filename}'")
