from django.apps import AppConfig


class AccountsConfig(AppConfig):
    # Specify the default auto field type for models in this app
    default_auto_field = 'django.db.models.BigAutoField'
    # Name of the app
    name = 'accounts'