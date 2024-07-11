# Import the AppConfig class from django.apps
from django.apps import AppConfig

# Define a configuration class for the 'api' application
class ApiConfig(AppConfig):
    # Specify the default auto field type for models in this app
    default_auto_field = 'django.db.models.BigAutoField'
    # Name of the app
    name = 'api'
