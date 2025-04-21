---
theme: default
---

# Entire Code Example

```py {*}{maxHeight:'350px'}
from pydantic import BaseModel
from kura import Kura
from kura.summarisation import SummaryModel, ConversationSummary, GeneratedSummary
from kura.types import Conversation, Message
from typing import Literal
from pydantic import Field
import instructor

# Define our Response Model
class UsagePattern(BaseModel):
    category: Literal["Learning", "QuestionAnswering", "Brainstorming", "TaskCompletion"] = Field(
        description="The primary usage pattern of this conversation"
    )
    summary: str = Field(
        description="A brief summary of what the user is trying to accomplish"
    )

class UsagePatternModel(SummaryModel):
    def __init__(self):
        super().__init__()

    async def summarise_conversation(
        self, conversation: Conversation
    ) -> ConversationSummary:
        client = self.clients.get("default")
        sem = self.sems.get("default")
        assert client is not None and isinstance(client, instructor.AsyncInstructor)

        async with sem:  # type: ignore
            resp = await client.chat.completions.create(  # type: ignore
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": """
You are a helpful assistant that summarises interactions between a custom service chatbot and a customer.
                Here is the conversation that you should summarise
    <messages>
    {% for message in messages %}
        <message>{{message.role}}: {{message.content}} </message>
    {% endfor %}
    </messages>
    """,
                    },
                ],
                context={"messages": conversation.messages},
                response_model=GeneratedSummary,
            )

        metadata = await self.apply_hooks(conversation)
        return ConversationSummary(
            chat_id=conversation.chat_id,
            summary=resp.summary,
            metadata={
                "conversation_turns": len(conversation.messages),
                **conversation.metadata,
                **metadata,
            },
        )
```
