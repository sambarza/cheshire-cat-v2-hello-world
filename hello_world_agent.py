from cat.services.agents.base import Agent
from cat.types import Task, TaskResult

from cat.log import log


class HelloWorldModelProvider(Agent):
    """Hello world agent."""

    slug = "hello_world_agent"
    name = "Hello World Agent"
    description = "A simple hello world agent."

    async def __call__(self, task: Task) -> TaskResult:
        log.info("Hello World: Model Provider received a task")
        return await super().__call__(task) 
