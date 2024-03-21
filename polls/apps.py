from django.apps import AppConfig


class PollsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'polls'

class MyPollsConfig(AppConfig):
    name = 'polls'

    def ready(self):
        from .utils import load_currencies
        load_currencies()
