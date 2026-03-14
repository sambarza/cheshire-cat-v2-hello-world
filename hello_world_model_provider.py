import asyncio

import random

from collections.abc import Awaitable, Callable

from cat.services.model_providers.base import ModelProvider
from cat.protocols.model_context.type_wrappers import TextContent
from cat.types import Message

from cat.mad_hatter.decorators import Tool

from cat.log import log

class HelloWorldModelProvider(ModelProvider):
    # This is an example of a custom model provider. It simulates an LLM streaming tokens and tool calls requests.
    slug = "hello_world_model_provider"
    name = "Hello World model provider"
    description = "Example of custom model provider simulating an LLM."

    async def setup(self):
        pass

    async def list_llms(self) -> list[str]:
        return ["hello-world"]

    async def list_embedders(self) -> list[str]:
        return ["hello-world-embedder"]

    async def llm(
        self,
        model: str,
        messages: list[Message],
        system_prompt: str = "",
        tools: list["Tool"] = [],
        on_token: Callable[[str], Awaitable[None]] | None = None,
    ) -> Message:
        
        log.info("Hello World: LLM simulator has received a call")

        # simulate streaming tokens with on_token callback, one token per second
        await self.simulate_token_stream(on_token)  # don't await, let it run in background   

        # simulate a tool call request if the user message contains the word "time"
        if messages[-1].role == "user" and "time" in messages[-1].text.lower():
            return Message(
                role="assistant",
                content=[TextContent(type="text", text="Let me check the time for you...")],
                tool_calls=[
                    {
                        "id": "dummy_tool_call_id",
                        "name": "what_time_is_it",
                        "args": {"topic": "current_time"}
                    }
                ],
            )
 
        # if we already have the current time simulate a LLM response using the tool call result
        if messages[-1].role == "tool" and messages[-1].tool_name == "what_time_is_it":
            text = f"The current time is `{messages[-1].text}`"
            return Message(role="assistant", content=[TextContent(text=text)])
            

        text = "You did not ask for the time. Try asking 'What time is it?'"
        return Message(role="assistant", content=[TextContent(text=text)])

    async def simulate_token_stream(self, on_token):
        await on_token("Thinking")

        for i in range(5):
            await asyncio.sleep(0.333)
            await on_token(".")

    async def embed(self, model: str, text: str) -> list[float]:
        return [random.random() for _ in range(8)]
