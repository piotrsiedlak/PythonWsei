# autor Piotr Siedlak
# numer albumu 12460

# zadanie 1
# import shutil
# import os

# os.makedirs("kopie", exist_ok=True)
# with open("raport.txt", "w") as report_file:
#     for folder in os.listdir():
#         if os.path.isdir(folder):
#             report_file.write(f"{os.path.abspath(folder)}\n")
#             for file in os.listdir(folder):
#                 if file.split(".")[-1].lower() in ["jpg", "png"]:
#                     shutil.copy(f"{folder}/{file}", f"kopie/{folder}_{os.listdir(folder).index(file)}.{file.split('.')[-1]}")
#                     report_file.write(f"{os.path.abspath(file)}\n")

# zadanie 2
# Napisz skrypt, który odczyta treść pliku o podanej nazwie, a następnie wyśle maila z tą treścią
# oraz ustaloną nazwą nadawcy i tytułem (zahardkodowane lub pobrane przez input).Wykorzystaj wbudowane
# moduły email i smtp do połączenia się z serwerem i wysłania maila. Skorzystaj np. z ustawień 
# prywatnej lub uczelnianej skrzynki, ale odpowiednio zanonimizuj dane w końcowym skrypcie -
# na przykład odczytując hasło z lokalnego pliku, używając jakiegoś szyfrowania lub wpisując 
# hasło podczas używania programu (input).

import smtplib
import email

with open("letter.txt") as mail_file:
    mail = mail_file.read()

#print(mail)

from_address = "papamek@poczta.fm"
to_address = "papamek@gmail.com"
subject = "Mail from Python"
msg = email.message.EmailMessage()
msg.set_content(mail)
msg["From"] = from_address
msg["To"] = to_address
msg["Subject"] = subject

server = smtplib.SMTP("poczta.interia.pl", 587)
server.starttls()
#haslo = input("Podaj hasło: ")
haslo = "2qrNWJwuPF4cF87Y"
server.login(from_address, haslo)
server.send_message(msg)
server.quit()

# zadanie 3
import datetime
import calendar

def get_last_work_day(year):
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    
    for month in range(1, 13):
        last_day = calendar.monthrange(year, month)[1]
        date = datetime.date(year, month, last_day)
        
        while date.weekday() >= 5: 
            date -= datetime.timedelta(days=1)
        
        formatted_date = date.strftime("%d-%m-%Y")
        
        print(f"{months[month - 1]}: {formatted_date}")

get_last_work_day(2024)
