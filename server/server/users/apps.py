from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'server.users'

    def ready(self):
        """
        Method called when the app is ready. Imports signals from users.
        """
        import server.users.signals
