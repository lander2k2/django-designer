import os
from django.core.management.base import BaseCommand, CommandError
from designer.render import template

class Command(BaseCommand):
    args = '<template>'
    help = 'Renders templates into html files for designers.'

    def handle(self, *args, **options):
        if os.path.isfile(args[0]):
            template(args[0])
        else:
            raise CommandError('Template "{0}" does not exist'.format(args[0]))

