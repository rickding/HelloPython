import numpy
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        seed = 7
        numpy.random.seed(seed)

        return 'api cmd %d' % numpy.random.randint(seed)
