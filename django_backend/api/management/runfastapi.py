from django.core.management.base import BaseCommand
import uvicorn

class Command(BaseCommand):
    help = 'Run FastAPI server'

    def handle(self, *args, **kwargs):
        uvicorn.run("fastapi_app:app", host="0.0.0.0", port=8000, reload=True)
