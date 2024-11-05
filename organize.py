import os
import shutil
import file_type as ft

# Function to organize files
def organize_files(source_dir):
    # Create target folders if they don't exist
    for folder in ft.file_categories.keys():
        folder_path = os.path.join(source_dir, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    # Traverse the directory
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            file_ext = os.path.splitext(file)[1].lower()  # Get the file extension
            moved = False

            # Check the file type and move it to the appropriate folder
            for category, extensions in ft.file_categories.items():
                if file_ext in extensions:
                    target_folder = os.path.join(source_dir, category)
                    source_file = os.path.join(root, file)
                    target_file = os.path.join(target_folder, file)

                    # Move the file
                    shutil.move(source_file, target_file)
                    print(f'Moved: {file} to {target_folder}')
                    moved = True
                    break

            # If the file does not match any category, leave it untouched
            if not moved:
                print(f'No category found for: {file}')
