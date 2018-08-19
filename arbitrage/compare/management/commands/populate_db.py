from django.core.management.base import BaseCommand


# wow... used def instead of class and couldn't figure out why things
# weren't working
class Command(BaseCommand):
    args = ''
    help = "Pulls data from ccxt and populates the app's db"

    # methods that begin with a single underscore _ are ignored by
    # from package import * commands (= (pseudo)private methods)
    def _my_print(self):
        print("yoooooO!")

    # subclasses of BaseCommand must provide a handle() method
    def handle(self, *args, **options):
        self._my_print()
