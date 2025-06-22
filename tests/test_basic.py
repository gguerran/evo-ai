import os
from pathlib import Path
import sys
import django
from django.test import Client as DjangoClient


def setup_module(module):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "evo_django.settings")
    base = Path(__file__).resolve().parents[1] / "src"
    sys.path.append(str(base))
    sys.path.append(str(base / "evo_django_proj"))
    django.setup()
    from django.conf import settings

    settings.ALLOWED_HOSTS.append("testserver")
    settings.REST_FRAMEWORK["DEFAULT_PERMISSION_CLASSES"] = [
        "rest_framework.permissions.AllowAny"
    ]
    from django.core.management import call_command

    call_command("migrate", run_syncdb=True, verbosity=0)
    call_command("flush", verbosity=0, interactive=False)


def test_index_view():
    client = DjangoClient()
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to Evo AI Django API"}


def test_model_str():
    from evo_django_proj.api.models.client import Client as ClientModel

    obj = ClientModel(name="Foo", email="foo@example.com")
    assert str(obj) == "Foo"
