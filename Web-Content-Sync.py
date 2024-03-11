import os
from time import sleep
import io
import sys

# Try to import 'requests' module, install if not available
try:from requests import get
except:
    os.system("pip install requests")
    os.system("cls")
    from requests import get


yeni = 3
error = 3

# Name of the local file to save the text
file="230202017.txt"

# Define a function to manipulate text format
def Edit_Text(text):
    original_stdout = sys.stdout
    fake_stdout = io.StringIO()
    sys.stdout = fake_stdout
    print(text)
    output = fake_stdout.getvalue().encode().decode('unicode_escape')
    sys.stdout = original_stdout
    return output



# URL of the Google document
# Change it to your own link
url="https://docs.google.com/document/d/141qDqFGjuyMHyf0VVaiymR7cTFtxG-sAlaKpgfy7oCk/edit?usp=sharing"

# Get the content of the Google document
ll = get(url).text

# Define start and end markers to extract the desired text
start = '#((('
end = ')))#'
# Write the code you want to send between (start) and (end).

# Extract text between start and end markers
req=(ll[ll.find(start)+len(start):ll.rfind(end)])

# Format the extracted text
req=Edit_Text(req)


# Write the formatted text to the local file
f = open(file, "a")
f = open(file, "r")
f = open(file, "w", encoding="utf-8")
f.write(req)
f.close()
old_command=req


# Define a function to continuously check for updates in the Google document
def main():
    status=True
    index=0
    while status:
        
        ll = get(url).text # Retrieve the content of the Google document
        
        req=(ll[ll.find(start)+len(start):ll.rfind(end)]) # Extract text between start and end markers
        
        req=Edit_Text(req) # Format the extracted text
        
        # Open the local file to compare with the previous content
        f = open(file, "a", encoding="utf-8")
        f = open(file, "r", encoding="utf-8")
        old_command=f.read()
        
        # Write the new content to the file if it's different from the previous content
        f = open(file, "w", encoding="utf-8")
        f.write(req)
        f.close()
        if req==old_command:req=""

        if req != "":
            
            f = open(file, "w", encoding="utf-8") # Write the new content to the file
            f.write(req)
            f.close()
            status=False
        else:
            index += 1
            print("no text found "+str(index))
            sleep(yeni)


# Main loop to continuously check for updates
while True:
    os.system("cls")
    try:
        
        main() # Call the function to check for updates
        
        print("start agin after "+str(yeni))
        sleep(yeni)
    except:
    
        print("ERROR") # Print error messages if there's an issue
        print("trying agin after "+str(error))
        sleep(error)
    os.system("cls")
