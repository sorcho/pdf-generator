import functions as f

email = f.salva_email()

giorni, mesi = f.calcolo_date(int(input("Inserisci il giorno: ")), int(input("Inserisci il mese: ")))

f.genera_qrcodes(giorni, mesi, email)
f.genera_canvas(giorni, mesi, email)
f.genera_pdf(email)

f.elimina_qrcodes(giorni, mesi, email)