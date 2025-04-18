import pandas as pd
from difflib import SequenceMatcher

def similarity(a, b):
    return SequenceMatcher(None, a.lower().strip(), b.lower().strip()).ratio()

df = pd.read_excel("memory_recall_tests.xlsx")

threshold = 0.9  # 90% similarity threshold
verdicts = []
accuracies = []

for _, row in df.iterrows():
    expected = row["Expected Recall"]
    actual = row["LLM Response"]
    sim = similarity(expected, actual)
    accuracy = sim * 100
    verdict = "Pass" if sim >= threshold else "Fail"
    
    accuracies.append(accuracy)
    verdicts.append(verdict)

df["Accuracy (%)"] = accuracies
df["Verdict"] = verdicts

# Save results
df.to_excel("memory_recall_results.xlsx", index=False)

# Overall stats
overall_accuracy = sum(1 for v in verdicts if v == "Pass") / len(verdicts) * 100
print(f"🧠 Overall Memory Recall Accuracy: {overall_accuracy:.2f}%")
