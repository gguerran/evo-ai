import os
from pathlib import Path
import sys
import django
from django.apps import apps


def setup_module(module):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "evo_django.settings")
    base = Path(__file__).resolve().parents[1] / "src"
    sys.path.append(str(base))
    sys.path.append(str(base / "evo_django_proj"))
    django.setup()
    from django.core.management import call_command

    call_command("migrate", run_syncdb=True, verbosity=0)
    call_command("flush", verbosity=0, interactive=False)


def test_verbose_names():
    Agent = apps.get_model("api", "Agent")
    assert Agent._meta.verbose_name == "Agente"
    assert Agent._meta.verbose_name_plural == "Agentes"

    Client = apps.get_model("api", "Client")
    assert Client._meta.verbose_name == "Cliente"
    assert Client._meta.verbose_name_plural == "Clientes"

    Tool = apps.get_model("api", "Tool")
    assert Tool._meta.verbose_name == "Ferramenta"
    assert Tool._meta.verbose_name_plural == "Ferramentas"


def test_str_methods():
    Client = apps.get_model("api", "Client")
    client_obj = Client(name="Acme", email="acme@example.com")
    assert str(client_obj) == "Acme"

    Tool = apps.get_model("api", "Tool")
    tool_obj = Tool(name="Tool1")
    assert str(tool_obj) == "Tool1"

    Agent = apps.get_model("api", "Agent")
    agent_obj = Agent(client=client_obj, name="Agent1", type="llm")
    assert str(agent_obj) == "Agent1"
