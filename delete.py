import os
import file_type as ft

# Function to delete a file
def delete_file(source_dir):
    print("\nAvailable Folders: ")
    for folder in ft.file_categories.keys():
        print(folder)

    selected_folder = input("Enter the folder name to delete a file from (or type 'exit' to go back): ").capitalize()

    if selected_folder in ft.file_categories:
        folder_path = os.path.join(source_dir, selected_folder)
        if os.path.exists(folder_path):
            files_in_folder = os.listdir(folder_path)
            if files_in_folder:
                print(f"\nFiles in {selected_folder} Folder:")
                for index, file in enumerate(files_in_folder):
                    print(f"{index + 1}. {file} ({os.path.splitext(file)[1]})")

                try:
                    file_index = int(input("Enter the number of the file to delete (or type '0' to cancel): "))
                    if file_index == 0:
                        return
                    elif 1 <= file_index <= len(files_in_folder):
                        file_to_delete = os.path.join(folder_path, files_in_folder[file_index - 1])
                        os.remove(file_to_delete)
                        print(f"File '{files_in_folder[file_index - 1]}' has been deleted.")
                    else:
                        print("Invalid file number.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            else:
                print(f"No files in the {selected_folder} folder.")
        else:
            print(f"Folder '{selected_folder}' does not exist.")
    elif selected_folder.lower() == 'exit':
        return
    else:
        print("Invalid folder name.")