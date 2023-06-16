###
# append_text.py takes .txt files from the path described by
# the variable folder_path, and appends the content of each file
# into one single file with a blank line separating each entry.
###

import os

def extract_number(file_name):
    # Extract the number between parentheses
    start = file_name.find('(') + 1
    end = file_name.find(')')
    return int(file_name[start:end])

def merge_text_files(folder_path, output_file):
    # Get a list of all files in the folder
    files = os.listdir(folder_path)
    
    # Sort the files based on the number in parentheses
    files.sort(key=extract_number)
    
    # Open the output file in 'write' mode
    with open(output_file, 'w') as output:
        for file_name in files:
            # Construct the full path to the file
            file_path = os.path.join(folder_path, file_name)
            
            # Check if the current item is a file
            if os.path.isfile(file_path):
                with open(file_path, 'r') as file:
                    # Read the contents of the file
                    file_contents = file.read()
                    
                    # Write the file contents to the output file
                    output.write(file_contents)
                    
                    # Add a blank line after each file
                    output.write('\n\n')

# Provide the path to the folder containing the text files
folder_path = 'in'

# Provide the name for the output file
output_file = 'combined_text_file.txt'

# Call the function to merge the text files
merge_text_files(folder_path, output_file)