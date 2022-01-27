import random
import qrcode
from PIL import Image

random_number_one = random.randint(1000,9999)
random_number_two = random.randint(1000,9999)

email = input("Inserisci la mail: ")
month = input("Inserisci un mese (tra 01 e 12): ")
day = input("Inserisci un giorno (tra 01 e 31): ")

data = qrcode.make(str(random_number_one) + '|' + str(random_number_two) + '|2022-' + str(month) + '-' + str(day) + '|UNINA\\' + email)

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

qr.add_data(data)
qr.make(fit=True)
data.save("sample.png")