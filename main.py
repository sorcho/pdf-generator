# In order to import every library needed run the following command "pip install -r requirements.txt"

import os # Imported os library used for clearing the terminal
import random # Imported random library used for generating random 4-string codes
import qrcode # Imported qrcode library
import datetime # Imported datetime library
from PIL import Image # Imported Image library from PILLOW
from reportlab.pdfgen import canvas
from PyPDF2 import PdfFileWriter, PdfFileReader

x = 470
i = 0

repeat = 's' # Initializing a char variable to 's' in order to imitate a do while loop in line :13
email_list = [] # Initializing email list

# From line 13 to 26 there is a function that extrapolates every day starting from user input and incrementing the date by 5 days
data = input("Inserisci il primo mese-giorno della settimana: ")
data = data.split("-")

test_date = datetime.datetime(2022, int(data[0]), int(data[1]))

K = 5
giorni = []

res = [test_date + datetime.timedelta(days=idx) for idx in range(K)]

for date in res:
    periodo = str(date)
    divisione = periodo.split("-")
    giorni.append(divisione[2].split(" "))

# TODO controllare che nella mail sia presente un solo punto
while repeat != 'n': # Do while-ish loop
    email_list.append(input("Inserisci la mail (nome.cognome): ")) # Loading several email in a list
    repeat = input("Vuoi generare un QR Code anche per un'altra mail?\nRisposta: ") # The users says if he wants to load another email or not

repeat = 's' # Re-initializing the char to 's' since another do while kinda loop is used in line :24

for email in email_list: # For each loop used to iterate through every email
    os.system('cls') # Clears the terminal
    c = canvas.Canvas('base.pdf')
    y = 615

    for date in giorni:
        random_number_one = random.randint(1000,9999) # Generate first 4 digit string
        random_number_two = random.randint(1000,9999) # Generate second 4 digit string
        
        string_wrap = f"{random_number_one}|{random_number_two}|2022-0{data[0]}-{date[0]}|UNINA\\{email}" # Wraps every information into a single variable
        dati = qrcode.make(string_wrap) # Creates the QRCode (I think at least)

        surname = email.split('.') # Saves in an array the name and the surname
        
        dati.save(f"QRCodes\\{surname[1]}[2022-0{data[0]}-{date[0]}].png") # Saves the QRCode as a png with the surname and the date in a folder called QRCodes
        
        image = Image.open(f"QRCodes\\{surname[1]}[2022-0{data[0]}-{date[0]}].png") # Saves the image in a variable
        
        qr_code = image.resize((83, 83)) # Resizes the image 83x83px
        qr_code.save(f"QRCodes\\{surname[1]}[2022-0{data[0]}-{date[0]}].png") # Saves the image with the same name
        
        c.drawImage(f"QRCodes\\{surname[1]}[2022-0{data[0]}-{date[0]}].png", x, y)
        
        y -= 100
        
    c.save()
    
    # Get the watermark file you just created
    watermark = PdfFileReader(open("base.pdf", "rb"))

    # Get our files ready
    output_file = PdfFileWriter()
    input_file = PdfFileReader(open("prenotazione.pdf", "rb"))

    # Number of pages in input document
    page_count = input_file.getNumPages()

    # Go through all the input file pages to add a watermark to them
    for page_number in range(page_count):
        print("Watermarking page {} of {}".format(page_number, page_count))
        # merge the watermark with the page
        input_page = input_file.getPage(page_number)
        input_page.mergePage(watermark.getPage(0))
        # add page from input file to output document
        output_file.addPage(input_page)

    # finally, write "output" to document-output.pdf
    with open(f"prenotazione{surname[1]}.pdf", "wb") as outputStream:
        output_file.write(outputStream)
    i += 1