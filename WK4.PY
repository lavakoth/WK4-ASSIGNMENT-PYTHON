# File Read & Write Challenge 
# This program reads a file and writes a modified version to a new file.

def modify_content(content):
    """Example modification: convert text to uppercase."""
    return content.upper()

try:
    # Error Handling Lab 
    filename = input("Enter the filename to read: ")
    
    # Open the file safely for reading
    with open(filename, "r") as infile:
        content = infile.read()
    
    # Modify the content
    modified_content = modify_content(content)
    
    # Write to a new file
    new_filename = "modified_" + filename
    with open(new_filename, "w") as outfile:
        outfile.write(modified_content)
    
    print(f" File modified successfully! Saved as '{new_filename}'")

except FileNotFoundError:
    print(" Error: The file does not exist. Please check the filename and try again.")
except PermissionError:
    print(" Error: You don’t have permission to read this file.")
except Exception as e:
    print(f" An unexpected error occurred: {e}")

