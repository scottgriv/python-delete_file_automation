# Import Modules
import os 

# Define your File Path
file_path = '/YOUR/FILE/PATH'
print(file_path)

# Check if the File Path is Valid - Delete or Skip
if os.path.isfile(file_path):
    os.remove(file_path)
    print("Successfully Deleted File!")
else:
    print("The File Does Not Exist!")