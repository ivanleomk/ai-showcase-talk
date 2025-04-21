---
layout: default
---

# Using our new model

```py {3-5}
from kura import Kura

kura = Kura(
    summarisation_model=UsagePatternModel()
)
```

<!--
When analyzing RAG system performance, distinguishing between inventory and capability issues is crucial:

- Knowledge Inventory failures occur when the right information simply isn't in your system
- Retrieval Capability failures happen when information exists but can't be effectively retrieved
- Generation Capability issues arise when retrieved content is misinterpreted or poorly synthesized
- Understanding this distinction helps target improvements to the right component
-->
