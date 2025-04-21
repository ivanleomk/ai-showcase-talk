---
layout: default
---

# Getting Started with Kura

````md magic-move
```python {6}
from kura import Kura
from kura.types import Conversation
import asyncio

# Initialise the Kura object
kura = Kura()
```

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
```

```python {14,15}
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
````
