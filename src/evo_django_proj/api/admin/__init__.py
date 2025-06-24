from django.contrib import admin

from evo_django_proj.api.models.agent import Agent
from evo_django_proj.api.models.agent_folder import AgentFolder
from evo_django_proj.api.models.api_key import ApiKey
from evo_django_proj.api.models.audit_log import AuditLog
from evo_django_proj.api.models.client import Client
from evo_django_proj.api.models.mcp_server import MCPServer
from evo_django_proj.api.models.session import Session
from evo_django_proj.api.models.tool import Tool
from evo_django_proj.api.models.user import User

from evo_django_proj.api.admin.agent import AgentAdmin
from evo_django_proj.api.admin.agent_folder import AgentFolderAdmin
from evo_django_proj.api.admin.api_key import ApiKeyAdmin
from evo_django_proj.api.admin.audit_log import AuditLogAdmin
from evo_django_proj.api.admin.client import ClientAdmin
from evo_django_proj.api.admin.mcp_server import MCPServerAdmin
from evo_django_proj.api.admin.session import SessionAdmin
from evo_django_proj.api.admin.tool import ToolAdmin
from evo_django_proj.api.admin.user import UserAdmin

admin.site.register(Client, ClientAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(AgentFolder, AgentFolderAdmin)
admin.site.register(Agent, AgentAdmin)
admin.site.register(ApiKey, ApiKeyAdmin)
admin.site.register(MCPServer, MCPServerAdmin)
admin.site.register(Tool, ToolAdmin)
admin.site.register(Session, SessionAdmin)
admin.site.register(AuditLog, AuditLogAdmin)

__all__ = [
    "AgentAdmin",
    "AgentFolderAdmin",
    "ApiKeyAdmin",
    "AuditLogAdmin",
    "ClientAdmin",
    "MCPServerAdmin",
    "ToolAdmin",
    "SessionAdmin",
    "UserAdmin",
]
