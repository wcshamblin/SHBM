from django.core.management.base import BaseCommand
from ...serializers import hostserializer
from ...models import host
from time import sleep, time
from subprocess import Popen
from json import load
import smtplib

conffile = open("./config.json", "r")
config = load(conffile)

server = smtplib.SMTP()
def smtpconn(server, usr, pas):
    server.connect('smtp.gmail.com', '587')
    server.ehlo()
    server.starttls()
    server.login(usr, pas)
smtpconn(server, config["smtpusr"], config["smtppass"])
def send_email(recipient, subject, body, server):
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s""" % ("SHBM Alerts", ", ".join(recipient if isinstance(recipient, list) else [recipient]), subject, body)
    server.sendmail("SHBM", recipient if isinstance(recipient, list) else [recipient], message)

class Command(BaseCommand):
    def handle(self, **options):
        while True:
            hosts=hostserializer(host.objects.all(), many=True).data
            for machine in hosts:
                if machine['active'] and not machine['down']:
                    if time()-61 > machine['heartrate']:
                        print(machine['hostname'], "is down, sending an alert to", machine["recipient1"], machine["recipient2"])
                        try:
                            send_email([machine["recipient1"], machine["recipient2"]], machine['hostname']+" down", machine['hostname']+" @ "+machine['ip']+" - down", server)
                        except:
                            print("Sending failed, retrying...")
                            smtpconn(server, config["smtpusr"], config["smtppass"])
                            send_email([machine["recipient1"], machine["recipient2"]], machine['hostname']+" down", machine['hostname']+" @ "+machine['ip']+" - down", server)
                        req = host.objects.get(pk=machine['idstr'])
                        req.down = True
                        req.save()

            sleep(1)