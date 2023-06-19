import os
import win32com.client as win32

# Create a list of all files in a folder
folder = "F:\\document\\dev-docs\\01_cpp\\02_CPP"
files = os.listdir(folder)

# Initialize MS Word application
word = win32.gencache.EnsureDispatch('Word.Application')
word.Visible = False

# Loop through all files in the folder
for file in files:
    # Check if file is a doc file
    if file.endswith(".doc"):
        # Get the new filename with docx extension
        new_file = file.replace(".doc", ".docx")
        new_path = os.path.join(folder, new_file)
        if not os.path.exists(new_path):
            # Get the full path of the file
            doc_path = os.path.join(folder, file)
            # Open the doc file
            doc = word.Documents.Open(doc_path)
            # Save the doc file as docx file
            doc.SaveAs(new_path, FileFormat=16) # 16 is for docx format
            # Close the original doc file
            doc.Close()
            print(file)
            os.remove(doc_path)



# Quit MS Word application
word.Quit()
print("finished")