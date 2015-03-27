from django.core.management.base import BaseCommand
from designer.render import template

class Command(BaseCommand):
    args = '<template>'
    help = 'Renders templates into html files for designers.'

    def handle(self, *args, **options):
        template(args[0])

