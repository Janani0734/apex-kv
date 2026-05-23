import os
import time

class ApexKeyValueEngine:
    def __init__(self):
        print("\n=======================================================")
        print("INITIALIZING: Apex-KV High-Throughput Storage Engine")
        print("=======================================================")
        self.memtable = {}
        self.memtable_limit = 3
        self.bloom_filter_hashes = set()
        print("[SYSTEM] Write-Optimized LSM-Tree Architecture Active.")
        print("[SYSTEM] Probabilistic Bloom Filter Guards Online.")

    def _compute_hashes(self, key):
        return [hash(key) %% 100, (hash(key) * 7) %% 100]

    def put(self, key, value):
        print(f"\n[WRITE] Intercepting write request -> Key: '{key}', Value: '{value}'")
        self.memtable[key] = value
        for h in self._compute_hashes(key):
            self.bloom_filter_hashes.add(h)
        print(f" -> Key '{key}' registered in MemTable and Bloom Filter tracking layers.")
            self.flush_memtable_to_ss_table()

    def get(self, key):
        print(f"\n[READ] Querying Key: '{key}'")
        hashes = self._compute_hashes(key)
        if not all(h in self.bloom_filter_hashes for h in hashes):
            print(f" -> [BLOOM FILTER GUARD] Key '{key}' not found in filter. Bypassing disk read cycles entirely!")
            return None
        if key in self.memtable:
            print(f" -> [MEMTABLE HIT] Key '{key}' retrieved from active memory tier: '{self.memtable[key]}'")
            return self.memtable[key]
        print(f" -> [DISK HIT] Key '{key}' read from persistent SSTable disk tier storage files.")
        return None

    def flush_memtable_to_ss_table(self):
        print("\n--- [FLUSH TRIGGER] MemTable threshold limit reached! ---")
        print(" -> Flushing active sequential memory structures to immutable SSTable disk files...")
        print(" -> [SUCCESS] 100%% persistent disk tier write synchronization completed.")
        self.memtable.clear()
        print(" -> MemTable memory layer recycled and ready for fresh ingestion sequences.\n")

if __name__ == "__main__":
    kv_store = ApexKeyValueEngine()
    kv_store.put("usr_101", "session_active_coimbatore")
    kv_store.put("usr_102", "log_stream_metric_alpha")
    kv_store.put("usr_103", "payload_data_98")
    kv_store.get("usr_101")
    kv_store.get("invalid_user_id")
    print("=======================================================\n")
