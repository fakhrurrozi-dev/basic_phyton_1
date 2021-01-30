import smtplib, ssl

port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = input("masukkan email anda :")
receiver_email = input("masukkan email anda :")
password = input("masukkan password anda : ")
message = """\
Subject: Indonesia.AI batch 3

Pembelajaran Basic Phyton ."""


with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.ehlo()  
    server.starttls()
    server.ehlo()  
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
