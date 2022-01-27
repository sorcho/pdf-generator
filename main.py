# In order to import every library needed run the following command "pip install -r requirements.txt"

import random # Imported random library
import qrcode # Imported qrcode library
from PIL import Image # Imported Image library from PILLOW

random_number_one = random.randint(1000,9999) # Generate first 4 digit string
random_number_two = random.randint(1000,9999) # Generate second 4 digit string

email = input("Inserisci la mail: ") # User writes his email
month = input("Inserisci un mese (tra 01 e 12): ") # User writes the month
day = input("Inserisci un giorno (tra 01 e 31): ") # User writes the day

stringWrap = str(random_number_one) + '|' + str(random_number_two) + '|2022-' + str(month) + '-' + str(day) + '|UNINA\\' + email # Wraps every information into a single variable
data = qrcode.make(stringWrap) # Creates the QRCode (I think at least)

# From now on I just brutally copy-pasted everything
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

qr.add_data(data)
qr.make(fit=True)
data.save("sample.png") # Saves the QRCode as "sample.png"