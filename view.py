import os
import file_type as ft

# Function to view files in a specific folder
def view_files(source_dir):
    print("\nAvailable Folders to View: ")
    for folder in ft.file_categories.keys():
        print(folder)

    selected_folder = input("Enter the folder name to view (or type 'exit' to go back): ").capitalize()
    
    if selected_folder in ft.file_categories:
        folder_path = os.path.join(source_dir, selected_folder)
        if os.path.exists(folder_path):
            files_in_folder = os.listdir(folder_path)
            if files_in_folder:
                print(f"\nFiles in {selected_folder} Folder:")
                for file in files_in_folder:
                    print(f"- {file} ({os.path.splitext(file)[1]})")
            else:
                print(f"No files in the {selected_folder} folder.")
        else:
            print(f"Folder '{selected_folder}' does not exist.")
    elif selected_folder.lower() == 'exit':
        return
    else:
        print("Invalid folder name.")