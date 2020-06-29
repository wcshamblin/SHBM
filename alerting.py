#!/usr/bin/python3
import smtplib
import argparse
from json import load

ps = argparse.ArgumentParser()
ps.add_argument("hostname", type=str, help="Hostname")
ps.add_argument("ip", type=str, help="IP address")

args = ps.parse_args()

conffile = open("./config.json", "r")
config = load(conffile)

def send_email(user, pwd, recipient, subject, body):
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (user, ", ".join(recipient if isinstance(recipient, list) else [recipient]), subject, body)
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(user, pwd)
    server.sendmail(user, recipient if isinstance(recipient, list) else [recipient], message)
    server.close()
print("Sending alert")
send_email(config["smtpusr"], config["smtppass"], config["email-to"], args.hostname+" down", args.hostname+" @ "+args.ip+" - down")