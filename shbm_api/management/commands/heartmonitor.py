from django.core.management.base import BaseCommand
from ...serializers import hostserializer
from ...models import host
from time import sleep, time
from subprocess import Popen
class Command(BaseCommand):
    def handle(self, **options):
        while True:
            hosts=hostserializer(host.objects.all(), many=True).data
            for machine in hosts:
                if machine['active'] and not machine['down']:
                    if time()-10 > machine['heartrate']:
                        Popen(["./alerting.py", machine['hostname'], machine['ip']])
                        req = host.objects.get(pk=machine['idstr'])
                        req.down = True
                        req.save()

            sleep(1)