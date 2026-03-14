from cat.mad_hatter.decorators import tool
from cat.mad_hatter.decorators import hook
from datetime import datetime

from cat.log import log

@tool(examples=["What time is it?"])
async def what_time_is_it(topic, caller):
    """Use this tool to get the current time"""

    log.info("Hello World: Tool 'what_time_is_it' has been called")

    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


@tool(examples=["Which time zone is it?"])
async def time_timezone(topic, caller):
    """Use this tool to get the current time"""

    log.info("Hello World: Tool 'time_timezone' has been called")

    return "CET"

@hook("before_agent_execution")
async def before_agent_execution(value, caller):
    log.info("Hello World: This is a hook that runs before every agent execution")