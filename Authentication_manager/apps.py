from django.apps import AppConfig
from django.apps import AppConfig


class AuthenticationManagerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Authentication_manager'

    def ready(self):
        import Authentication_manager.signals  # Import the signals module when the app is ready
