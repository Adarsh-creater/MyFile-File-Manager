
import organize as of
import delete as df
import view as vf

# Main function
if __name__ == "__main__":
    source_directory = input("Enter the path of the directory to organize: ")
    of.organize_files(source_directory)

    while True:
        print("\nOptions:")
        print("1. View files in a folder")
        print("2. Delete a file")
        print("3. Exit")
        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            vf.view_files(source_directory)
        elif choice == '2':
            df.delete_file(source_directory)
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
