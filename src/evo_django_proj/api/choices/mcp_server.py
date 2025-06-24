from django.db import models


class ConfigType(models.TextChoices):
    STUDIO = "studio", "Studio"
    SSE = "sse", "SSE"


class MCPServerType(models.TextChoices):
    OFFICIAL = "official", "Official"
    COMMUNITY = "community", "Community"
