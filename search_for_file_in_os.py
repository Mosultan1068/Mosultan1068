import os
def list_all_files_recursive(directory="C:\\testfiles\\"):
    """
    List all files in the given directory and its subdirectories.
    """
    file_paths = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_paths.append(os.path.join(root, file))
    return file_paths

# Example usage:
all_files = list_all_files_recursive("C:\\testfiles\\")
print("All files including subdirectories:")
for file in all_files:
    print(file)
    if file.endswith(".py"):
        print("File is a python type")
    elif file.endswith(".txt"):
        print(f"File is a text type:", file)



