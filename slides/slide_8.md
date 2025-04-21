---
theme: default
---

# Summarizing User Conversations

````md magic-move
```python {4-12} {maxHeight:"400px"}
from pydantic import BaseModel

# Define our Response Model
class UsagePattern(BaseModel):
    category: Literal["Learning", "QuestionAnswering", "Brainstorming", "TaskCompletion"] = Field(
        description="The primary usage pattern of this conversation"
    )
    summary: str = Field(
        description="A brief summary of what the user is trying to accomplish"
    )
```

```python {2,3,4,14-17} {maxHeight:"400px"}
from pydantic import BaseModel
from kura import Kura
from kura.summarisation import SummaryModel, ConversationSummary, GeneratedSummary
from kura.types import Conversation, Message

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
```

```python {10-20} {maxHeight:"400px"}
from pydantic import BaseModel
from kura import Kura
from kura.summarisation import SummaryModel, ConversationSummary, GeneratedSummary
from kura.types import Conversation, Message

class UsagePatternModel(SummaryModel):
    def __init__(self):
        super().__init__()

    async def summarise_conversation(
        self, conversation: Conversation
    ) -> ConversationSummary:
        client = self.clients.get("default")
        sem = self.sems.get("default")
        assert client is not None and isinstance(client, instructor.AsyncInstructor)
```

```py {3-22} {maxHeight:"400px"}
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
```

```py {*}
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
````

<!--
This slide shows how Anthropic transformed topic modeling insights into product features:

- Topic modeling revealed that students were engaging in four distinct interaction styles, indicating different needs
- Instead of just focusing on improving answer accuracy, they discovered a need for a different interaction model
- This led to prioritizing a Learning Mode that emphasizes the Socratic method - asking questions back to students
- The product was designed to clarify concepts, generate thoughtful questions, and guide students toward understanding
- Topic modeling helped them prioritize this feature that might not have been obvious through traditional product development
- By quantifying conversation patterns, they could justify the development effort for this specialized education mode
-->
