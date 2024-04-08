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


scriptlogo="""
░██╗░░░░░░░██╗███████╗██████╗░  ░█████╗░░█████╗░███╗░░██╗████████╗███████╗███╗░░██╗████████╗
░██║░░██╗░░██║██╔════╝██╔══██╗  ██╔══██╗██╔══██╗████╗░██║╚══██╔══╝██╔════╝████╗░██║╚══██╔══╝
░╚██╗████╗██╔╝█████╗░░██████╦╝  ██║░░╚═╝██║░░██║██╔██╗██║░░░██║░░░█████╗░░██╔██╗██║░░░██║░░░
░░████╔═████║░██╔══╝░░██╔══██╗  ██║░░██╗██║░░██║██║╚████║░░░██║░░░██╔══╝░░██║╚████║░░░██║░░░
░░╚██╔╝░╚██╔╝░███████╗██████╦╝  ╚█████╔╝╚█████╔╝██║░╚███║░░░██║░░░███████╗██║░╚███║░░░██║░░░
░░░╚═╝░░░╚═╝░░╚══════╝╚═════╝░  ░╚════╝░░╚════╝░╚═╝░░╚══╝░░░╚═╝░░░╚══════╝╚═╝░░╚══╝░░░╚═╝░░░

░██████╗██╗░░░██╗███╗░░██╗░█████╗░
██╔════╝╚██╗░██╔╝████╗░██║██╔══██╗
╚█████╗░░╚████╔╝░██╔██╗██║██║░░╚═╝
░╚═══██╗░░╚██╔╝░░██║╚████║██║░░██╗
██████╔╝░░░██║░░░██║░╚███║╚█████╔╝
╚═════╝░░░░╚═╝░░░╚═╝░░╚══╝░╚════╝░"""

print(scriptlogo)


# URL of the Google document
# Change it to your own link
url="https://docs.google.com/document/d/141qDqFGjuyMHyf0VVaiymR7cTFtxG-sAlaKpgfy7oCk/edit?usp=sharing"

file="230202017.txt"          # Name of the local file to save the text
start = '#((('                # Define start and end markers to extract the desired text
end = ')))#'                  # Write the code you want to send between (start) and (end).

refresh = 3
error = 3


# Define a function to manipulate text format
def Edit_Text(text):
    original_stdout = sys.stdout
    fake_stdout = io.StringIO()
    sys.stdout = fake_stdout
    print(text)
    output = fake_stdout.getvalue().encode().decode('unicode_escape')
    sys.stdout = original_stdout
    return output




# Get the content of the Google document
html_code = get(url).text





# Extract text between start and end markers
request=(html_code[html_code.find(start)+len(start):html_code.rfind(end)])

# Format the extracted text
request=Edit_Text(request)


# Write the formatted text to the local file
f = open(file, "a")
f = open(file, "r")
f = open(file, "w", encoding="utf-8")
f.write(request)
f.close()
old_command=request


# Define a function to continuously check for updates in the Google document
def main():
    status=True
    index=0
    while status:
        
        html_code = get(url).text # Retrieve the content of the Google document
        
        request=(html_code[html_code.find(start)+len(start):html_code.rfind(end)]) # Extract text between start and end markers
        
        request=Edit_Text(request) # Format the extracted text
        
        # Open the local file to compare with the previous content
        f = open(file, "a", encoding="utf-8")
        f = open(file, "r", encoding="utf-8")
        old_command=f.read()
        
        # Write the new content to the file if it's different from the previous content
        f = open(file, "w", encoding="utf-8")
        f.write(request)
        f.close()
        if request==old_command:request=""

        if request != "":
            
            f = open(file, "w", encoding="utf-8") # Write the new content to the file
            f.write(request)
            f.close()
            status=False
        else:
            index += 1
            print("no text found "+str(index))
            sleep(refresh)


# Main loop to continuously check for updates
while True:
    os.system("cls")
    try:
        
        main() # Call the function to check for updates
        
        print("start agin after "+str(refresh))
        sleep(refresh)
    except:
    
        print("ERROR") # Print error messages if there's an issue
        print("trying agin after "+str(error))
        sleep(error)
    os.system("cls")
