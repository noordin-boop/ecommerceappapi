from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class Command(BaseCommand):
    help = 'Generate a token for a specific user'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='The username of the user')

    def handle(self, *args, **kwargs):
        username = kwargs['username']
        try:
            user = User.objects.get(username=username)
            token, created = Token.objects.get_or_create(user=user)
            self.stdout.write(f"Token for {username}: {token.key}")
        except User.DoesNotExist:
            self.stderr.write(f"User with username {username} does not exist.")
