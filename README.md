# High-Throughput Log-Structured Ingestion Engine (Apex-KV)

A high-performance, local key-value storage engine designed from scratch to implement the foundational computer science mechanics of low-latency stream ingestion and structural storage space optimization.

## 🛠️ Architectural Infrastructure
* **Pipeline Infrastructure:** Built a write-optimized Log-Structured Merge-Tree (LSM-Tree) architecture that processes high-velocity sequential write operations natively in memory (MemTable layer) before flushing logs to persistent disk tiers, eliminating storage engine write bottlenecks.
* **Algorithmic Filtering:** Integrated probabilistic Bloom Filter memory guards to intercept search queries, reducing unnecessary disk read cycles and accelerating system lookup operations.

## Storage Engine Blueprint Usage
To initialize local storage stream and memory guard validations, execute:
```bash
python engine.py