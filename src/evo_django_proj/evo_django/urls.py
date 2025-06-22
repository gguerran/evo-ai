from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from evo_django_proj.api.views import index
from evo_django_proj.api.viewsets import (
    ClientViewSet,
    UserViewSet,
    AgentFolderViewSet,
    AgentViewSet,
    ApiKeyViewSet,
    MCPServerViewSet,
    ToolViewSet,
    SessionViewSet,
    AuditLogViewSet,
)

router = DefaultRouter()
router.register(r"clients", ClientViewSet)
router.register(r"users", UserViewSet)
router.register(r"folders", AgentFolderViewSet)
router.register(r"agents", AgentViewSet)
router.register(r"api-keys", ApiKeyViewSet)
router.register(r"mcp-servers", MCPServerViewSet)
router.register(r"tools", ToolViewSet)
router.register(r"sessions", SessionViewSet)
router.register(r"audit-logs", AuditLogViewSet)

urlpatterns = [
    path("", index, name="index"),
    path("api/", include(router.urls)),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path("admin/", admin.site.urls),
]
