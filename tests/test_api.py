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
    from evo_django_proj.api.viewsets.client import ClientViewSet
    from rest_framework.permissions import AllowAny

    ClientViewSet.permission_classes = [AllowAny]


def test_create_and_list_client():
    client = DjangoClient()
    import json

    response = client.post(
        "/api/clients/",
        data=json.dumps({"name": "Acme", "email": "acme@example.com"}),
        content_type="application/json",
    )
    assert response.status_code == 201

    response = client.get("/api/clients/")
    assert response.status_code == 200
    data = response.json()
    assert data[0]["name"] == "Acme"
