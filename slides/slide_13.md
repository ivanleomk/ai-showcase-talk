---
theme: default
---

# Entire Code Example

```py {*}{maxHeight:'350px'}
import asyncio
import instructor
from pydantic import BaseModel, Field
from kura import Kura
from kura.types import Conversation, ExtractedProperty
from kura.summarisation import SummaryModel


class Language(BaseModel):
    language_code: str = Field(
        description="The language code of the conversation. (Eg. en, fr, es)",
        pattern=r"^[a-z]{2}$",
    )


async def language_extractor(
    conversation: Conversation,
    sems: dict[str, asyncio.Semaphore],
    clients: dict[str, instructor.AsyncInstructor],
) -> ExtractedProperty:
    # Get the default semaphore and client limits
    sem = sems.get("default")
    client = clients.get("default")

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


summary_model = SummaryModel(extractors=[language_extractor])
kura = Kura(
    summarisation_model=summary_model,
    override_checkpoint_dir=True
)
conversations = Conversation.from_claude_conversation_dump("conversations.json")[:100]
asyncio.run(kura.cluster_conversations(conversations))
kura.visualise_clusters()
```

<!--
Being able to extract these conversations and label them with these models is a huge game changer.

For instance, we recently worked with a customer deploying chatbots to take orders at scale.

They thought our client's chatbot needed improvement handling niche queries like "Do you have parking?" However, analyzing their conversation data revealed a surprising truth: 75% of customer interactions were simple food orders, with 93% of those mentioning just one dish. The real opportunity emerged when we noticed that a simple "Is that all?" prompt resulted in a 66% upsell success rate. Customers were already primed to purchase more. The solution wasn't investing in complex query handling, but optimizing the prompt flow: suggest drinks with main courses, recommend combos with single-item orders.

Imagine just changing 3 lines of code, and increasing revenue by almost 20%.
-->
