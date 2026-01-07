import smtplib, ssl
from email.message import EmailMessage
import inghdr
#https://myaccount.google.com/apppasswords
def saada_email(saaja_email):
    kiri="Tere! See on test e-kiri Pythonist"
    teema="Test e-kiri Pythonist"
    saatja_email="arsenibogan@gmail.com"
    parool=input("Sisesta rakenduse parool: ")
    smtp_server="smtp.gmail.com"
    port=587 #465
    context=ssl.create_default_context()
    msg=EmailMessage()
    msg.set_content(kiri.subtype='html')
    msg.set_content(kiri)
    msg["Subject"]=teema
    msg["From"]=saatja_email
    msg["To"]=saaja_email
    try:
        with smtplib.SMTP(smtp_server,port) as server:
            server.starttls(context=context)
            server.login(saatja_email, parool)
            server.send_message(msg)
    except Exception as e:
        print(f"Midagi läks valesti... {e}")

kellele=input("Sisesta saaja e-posti aadress: ")
saada_email(kellele)