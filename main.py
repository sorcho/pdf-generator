# In order to import every library needed run the following command "pip install -r requirements.txt"

import os # Imported os library used for clearing the terminal
import random # Imported random library used for generating random 4-string codes
import qrcode # Imported qrcode library
from PIL import Image # Imported Image library from PILLOW

repeat = 's' # Initializing a char variable to 's' in order to imitate a do while loop in line :13
email_list = [] # Initializing email list
month = [] # Initializing month list
day = [] # Initializing day list

# TODO controllare che nella mail sia presente un solo punto
while repeat != 'n': # Do while-ish loop
    email_list.append(input("Inserisci la mail (nome.cognome): ")) # Loading several email in a list
    repeat = input("Vuoi generare un QR Code anche per un'altra mail?\nRisposta: ") # The users says if he wants to load another email or not

for email in email_list: # For each loop used to iterate through every email
    os.system('cls') # Clears the terminal
    
    repeat = 's' # Re-initializing the char to 's' since another do while kinda loop is used in line :24

    print(f"Utente: {email}") # Prints the user currently loaded

    # TODO controllare l'effettiva esistenza della data
    while repeat != 'n': # The other do while loop
        month.append(input("Inserisci un mese (tra 01 e 12): ")) # User writes the month
        day.append(input("Inserisci un giorno (tra 01 e 31): ")) # User writes the day

        repeat = input(f"Vuoi inserire un'altra data per l'utente {email}?\nRisposta: ") # Again, the program asks the user if he wants to load more months and days

    for i in range(len(month)):
        random_number_one = random.randint(1000,9999) # Generate first 4 digit string
        random_number_two = random.randint(1000,9999) # Generate second 4 digit string
        
        string_wrap = f"{random_number_one}|{random_number_two}|2022-{month[i]}-{day[i]}|UNINA\\{email}" # Wraps every information into a single variable
        data = qrcode.make(string_wrap) # Creates the QRCode (I think at least)

        surname = email.split('.') # Saves in an array the name and the surname
        
        data.save(f"QRCodes\\{surname[1]}[2022-{month[i]}-{day[i]}].png") # Saves the QRCode as a png with the surname and the date in a folder called QRCodes
        
        image = Image.open(f"QRCodes\\{surname[1]}[2022-{month[i]}-{day[i]}].png") # Saves the image in a variable
        
        qr_code = image.resize((83, 83)) # Resizes the image 83x83px
        qr_code.save(f"QRCodes\\{surname[1]}[2022-{month[i]}-{day[i]}].png") # Saves the image with the same name
