---
theme: default
---

# Language Detection for Conversations

````md magic-move
```python {4-9} {maxHeight:"300px"}
import asyncio
import instructor
from pydantic import BaseModel, Field

class Language(BaseModel):
    language_code: str = Field(
        description="The language code of the conversation. (Eg. en, fr, es)",
        pattern=r"^[a-z]{2}$",
    )
```

```python {3-4,7-8} {maxHeight:"300px"}
async def language_extractor(
    conversation: Conversation,
    sems: dict[str, asyncio.Semaphore],
    clients: dict[str, instructor.AsyncInstructor],
) -> ExtractedProperty:
    # Get the default semaphore and client limits
    sem = sems.get("default")
    client = clients.get("default")
```

```py {1,18-21} {maxHeight:"300px"}
    async with sem:
        resp = await client.chat.completions.create(
            model="gemini-2.0-flash",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant that extracts the language of the following conversation.",
                },
                {
                    "role": "user",
                    "content": "\n".join(
                        [f"{msg.role}: {msg.content}" for msg in conversation.messages]
                    ),
                },
            ],
            response_model=Language,
        )
        return ExtractedProperty(
            name="language_code",
            value=resp.language_code,
        )
```
````

<!--
This slide shows how a simple language detector can be implemented for conversation analysis:

- We define a Pydantic model to validate the language code format
- We create an async function that takes conversation data, semaphores, and API clients
- The function uses a semaphore to manage API request concurrency
- It formats conversation messages into a simple string format
- The function calls an LLM to detect the language of the conversation
- It returns a structured ExtractedProperty with the detected language code

This approach allows for efficient language tagging with minimal code complexity.
-->
