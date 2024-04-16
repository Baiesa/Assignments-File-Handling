'''
Objective:
The goal of this assignment is to deepen your understanding of the OS module in Python. 
You will engage in tasks that involve file and directory operations, path manipulations, 
and practical applications of these operations in real-world scenarios.

Task 1: Directory Inspector:

Problem Statement:
Create a Python script that lists all files and subdirectories in a given directory. 
Your script should prompt the user for the directory path and then display the contents.

Code Example:
```python
import os
def list_directory_contents(path):
    # List and print all files and subdirectories in the given path
```

'''

# import os

# def list_directory_contents(path):
#     try:
#         contents = os.listdir(path)
#         print("Contents of directory:", path)
#         for item in contents:
#             print(item)
#     except FileNotFoundError:
#         print("Directory not found:", path)
#     except PermissionError:
#         print("Permission denied for directory:", path)


# directory_path = input("Enter the directory path: ")
# list_directory_contents(directory_path)

'''
Task 2: File Size Reporter:

Problem Statement:
Write a Python program that reports the sizes of all files in a specific directory. 
The program should ask the user for a directory path and then print each file's name and size within that directory.

Code Example:
```python
def report_file_sizes(directory):
# Iterate through files in the directory and print their names and sizes
'''


# import os

# def report_file_sizes(directory):
#     try:
#         files = os.listdir(directory)
#         print("File sizes in directory:", directory)
#         for file in files:
       
#             file_path = os.path.join(directory, file)
        
#             if os.path.isfile(file_path):
              
#                 size = os.path.getsize(file_path)
#                 print(f"File: {file}, Size: {size} bytes")
#     except FileNotFoundError:
#         print("Directory not found:", directory)
#     except PermissionError:
#         print("Permission denied for directory:", directory)

# directory_path = input("Enter the directory path: ")
# report_file_sizes(directory_path)


'''
Task 3: File Extension Counter:

Problem Statement:
Develop a Python script that counts the number of files of each extension type in a directory. 
For instance, in a directory with five '.txt' files and three '.py' files, the script should report "TXT: 5" and "PY: 3".

Code Example:
python def count_file_extensions(directory): # Count and print the number of files of each extension type in the directory
'''
import os

def count_file_extensions(directory):
    try:
        extension_counts = {}

    
        files = os.listdir(directory)

    
        for file in files:
    
            _, extension = os.path.splitext(file)
      
            extension = extension[1:]

        
            if os.path.isfile(os.path.join(directory, file)):
        
                extension_counts[extension] = extension_counts.get(extension, 0) + 1

     
        print("File extension counts in directory:", directory)
        for ext, count in extension_counts.items():
            print(f"{ext.upper()}: {count}")
    except FileNotFoundError:
        print("Directory not found:", directory)
    except PermissionError:
        print("Permission denied for directory:", directory)


directory_path = input("Enter the directory path: ")


count_file_extensions(directory_path)