import os
import random
from tkinter import Image
import qrcode
from PIL import Image
from reportlab.pdfgen import canvas
from PyPDF2 import PdfFileWriter, PdfFileReader


def calcolo_date(giorno, mese):
    giorni_dei_mesi = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    giorni = []
    mesi = []

    for i in range(5):
        if giorno > giorni_dei_mesi[mese - 1]:
            mese += 1
            giorno = 1

        giorni.append(giorno)
        mesi.append(mese)

        giorno += 1

    for i in range(len(giorni)):
        if giorni[i] > 0 and giorni[i] < 10:
            giorni[i] = f"0{giorni[i]}"
        else:
            giorni[i] = str(giorni[i])

    for i in range(len(mesi)):
        if mesi[i] > 0 and mesi[i] < 10:
            mesi[i] = f"0{mesi[i]}"
        else:
            mesi[i] = str(mesi[i])

    return giorni, mesi


def salva_email():
    email = []

    f = open("mail.txt", "r")
    
    for line in f:
        email.append(line.strip())

    return email


def genera_qrcodes(giorno_, mese_, email_):
    primo_numero = random.randint(1000, 9999)
    secondo_numero = random.randint(1000, 9999)

    for email in email_:
        for (giorno, mese) in zip(giorno_, mese_):
            dati = f"{primo_numero}|{secondo_numero}|2022-{mese}-{giorno}|UNINA\\{email}"

            qrcode.make(dati).save(f"{email}-{mese}-{giorno}.png")

            imagine = Image.open(f"{email}-{mese}-{giorno}.png")

            imagine.resize((83, 83)).save(f"{email}-{mese}-{giorno}.png")


def genera_canvas(giorno_, mese_, email_):
    c = canvas.Canvas("base.pdf")
    i = 0

    for email in email_:
        y = 615
        
        for (giorno, mese) in zip(giorno_, mese_):
            c.drawImage(f"{email}-{mese}-{giorno}.png", 470, y)
            y -= 100
            i += 1
    print(i)
    c.save()


def genera_pdf(email_):
    for email in email_:
        watermark = PdfFileReader(open("base.pdf", "rb"))

        input_file = PdfFileReader(open("prenotazione.pdf", "rb"))
        output_file = PdfFileWriter()

        input_page = input_file.getPage(0)
        input_page.mergePage(watermark.getPage(0))

        output_file.addPage(input_page)
        output_file.write(open(f"PDF/prenotazione-{email}.pdf", "wb"))


def elimina_qrcodes(giorno_, mese_, email_):
    for email in email_:
        for (giorno, mese) in zip(giorno_, mese_):
            os.remove(f"{email}-{mese}-{giorno}.png")
