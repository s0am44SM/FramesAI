import pandas as pd
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# 🔹 1. Load Excel
df = pd.read_excel("task_predictions.xlsx")

# 🔹 2. Get expected & predicted labels
expected = df["Expected_Label"]
predicted = df["Predicted_Label"]

# 🔹 3. Evaluate
accuracy = accuracy_score(expected, predicted)
print(f"\n✅ Accuracy: {accuracy * 100:.2f}%\n")

print("📊 Classification Report:\n")
print(classification_report(expected, predicted))

print("📌 Confusion Matrix:\n")
print(confusion_matrix(expected, predicted))

# 🔹 4. Optional: Add Result Column (Correct/Incorrect)
df["Result"] = ["Correct" if e == p else "Incorrect" for e, p in zip(expected, predicted)]

# 🔹 5. Save the updated file
df.to_excel("task_predictions_with_results.xlsx", index=False)
