from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "only-for-practice-not-for-real-projects"
DEBUG = True
ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = []
MIDDLEWARE = []
ROOT_URLCONF = "docker_demo.urls"
TEMPLATES = []
DATABASES = {}

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
