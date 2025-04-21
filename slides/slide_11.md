---
layout: default
---

# Understanding RAG Systems - Inventory vs Capability

<div class="grid grid-cols-1 gap-y-0">
  <div v-click>
    <h3 class="text-2xl font-bold text-blue-400">Knowledge Inventory</h3>
    <p class="mt-2 text-white opacity-90">Document coverage, freshness, and granularity of information in your vector store</p>
  </div>

  <div v-click>
    <h3 class="text-2xl font-bold text-blue-400">Retrieval Capability</h3>
    <p class="mt-2 text-white opacity-90">Effectiveness of embedding models, chunking strategies, and query reformulation</p>
  </div>

  <div v-click>
    <h3 class="text-2xl font-bold text-blue-400">Generation Capability</h3>
    <p class="mt-2 text-white opacity-90">LLM's ability to synthesize retrieved content into accurate, coherent responses</p>
  </div>
</div>

<!--
When analyzing RAG system performance, distinguishing between inventory and capability issues is crucial:

- Knowledge Inventory failures occur when the right information simply isn't in your system
- Retrieval Capability failures happen when information exists but can't be effectively retrieved
- Generation Capability issues arise when retrieved content is misinterpreted or poorly synthesized
- Understanding this distinction helps target improvements to the right component
-->
