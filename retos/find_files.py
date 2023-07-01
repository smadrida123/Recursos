#Write a program that takes a directory path as input and recursively finds all files with a given file extension (e.g., ".txt").
#Display the list of file names with their respective file sizes.
import os
def find_paths():

 folder_path = input("Ingrese path de carpeta a verificar: ")
 extension= input("Extension de archivos a mostrar: ")

# Check if the folder exists
 if os.path.exists(folder_path) and os.path.isdir(folder_path):
    # Get the list of files in the folder
    file_list = os.listdir(folder_path)
    
    # Display the files
    for file_name in file_list:
        if extension in file_name:
         print(file_name)
 else:
    print("Folder does not exist or is not a directory.")
    


find_paths()
 