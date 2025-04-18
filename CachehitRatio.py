import pandas as pd

# Load the log data
df = pd.read_excel("cache_log.xlsx")

# Normalize and verify entries
df["Response Source"] = df["Response Source"].str.lower().str.strip()

# Count hits and misses
total_requests = df.shape[0]
hits = df[df["Response Source"] == "cache"].shape[0]
misses = total_requests - hits

# Calculate ratio
cache_hit_ratio = (hits / total_requests) * 100 if total_requests else 0

# Add column for tracking
df["Cache Status"] = df["Response Source"].apply(lambda x: "Hit" if x == "cache" else "Miss")

# Save with results
df.to_excel("cache_log_with_status.xlsx", index=False)

# Print stats
print(f"✅ Cache Hit Ratio: {cache_hit_ratio:.2f}%")
print(f"🔍 Total Requests: {total_requests}, Hits: {hits}, Misses: {misses}")
