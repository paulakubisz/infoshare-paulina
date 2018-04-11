import secrets
import smtplib

adresat = secrets.login
nadawca = secrets.login
haslo = secrets.haslo

mailer = smtplib.SMTP("smtp.gmail.com", 587)
mailer.ehlo()
mailer.starttls()
mailer.login(nadawca, haslo)

temat = "Subject: Hello from Paulina\n"
wiadomosc = "To jes moja wiadomosc"

tresc = temat + wiadomosc

mailer.sendmail(nadawca, adresat, tresc)
print("Wysłano maila!")
mailer.close()