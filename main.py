# In order to import every library needed run the following command "pip install -r requirements.txt"

import random # Imported random library
import qrcode # Imported qrcode library
from PIL import Image # Imported Image library from PILLOW

repeat = 's'
email_array = []

while repeat != 'n':
    email_array.append(input("Inserisci la mail: "))
    repeat = input("Vuoi generare un QR Code anche per un'altra mail?\nRisposta: ")

for email in email_array:
    random_number_one = random.randint(1000,9999) # Generate first 4 digit string
    random_number_two = random.randint(1000,9999) # Generate second 4 digit string

    month = input("Inserisci un mese (tra 01 e 12): ") # User writes the month
    day = input("Inserisci un giorno (tra 01 e 31): ") # User writes the day

    string_wrap = f"{random_number_one}|{random_number_two}|2022-{month}-{day}|UNINA\\{email}" # Wraps every information into a single variable
    data = qrcode.make(string_wrap) # Creates the QRCode (I think at least)
    
    surname = email.split('.') # Saves in an array the name and the surname
    
    data.save(f"QRCodes\\{surname[1]}[2022-{month}-{day}].png") # Saves the QRCode as a png with the surname and the date in a folder called QRCodes