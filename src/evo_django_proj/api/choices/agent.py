from django.db import models


class AgentType(models.TextChoices):
    LLM = "llm", "LLM"
    SEQUENTIAL = "sequential", "Sequential"
    PARALLEL = "parallel", "Parallel"
    LOOP = "loop", "Loop"
    A2A = "a2a", "A2A"
    WORKFLOW = "workflow", "Workflow"
    CREW_AI = "crew_ai", "CrewAI"
    TASK = "task", "Task"
