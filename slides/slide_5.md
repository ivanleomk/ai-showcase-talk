---
layout: default
---

# Loading Different Datasets in Kura

````md magic-move
```python {9-11}
from kura import Kura
from kura.types import Conversation
import asyncio

# Initialise the Kura object
kura = Kura()

# Load in a Conversation from Hugging Face
conversations = Conversation.from_hf_dataset(
    "ivanleomk/synthetic-gemini-conversations", split="train"
)

# Kick off the clustering step
asyncio.run(kura.cluster_conversations(conversations))
kura.visualise_clusters()
```

```python {9-19}
from kura import Kura
from kura.types import Conversation
import asyncio

# Initialize Kura
kura = Kura()

# Use it with a dataset that might not have the same created_at, chat_id and messages fields
conversations = Conversation.from_hf_dataset(
    "allenai/WildChat-nontoxic",
    split="train",
    max_conversations=2000,
    chat_id_fn=lambda x: x["conversation_id"],
    created_at_fn=lambda x: x["timestamp"],
    messages_fn=lambda row: [
        {"role": m["role"], "content": m["content"], "created_at": row["timestamp"]}
        for m in row["conversation"]
    ],
)


# Run clustering and visualization
asyncio.run(kura.cluster_conversations(conversations))
kura.visualise_clusters()
```

```python {7}
from kura import Kura
from kura.types import Conversation
import asyncio

kura = Kura()

conversations = Conversation.from_claude_conversation_dump("conversations.json")

asyncio.run(kura.cluster_conversations(conversations))

kura.visualise_clusters()
```
````
