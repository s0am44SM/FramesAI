import pandas as pd

# 🔹 1. Load Excel File
df = pd.read_excel("holding_responses.xlsx")

# 🔹 2. Compare Holding Responses with Expected Responses
df["Holding Response Accuracy"] = df["Holding Response"] == df["Expected Holding Response"]

# 🔹 3. Calculate Holding Response Accuracy
holding_accuracy = df["Holding Response Accuracy"].mean() * 100

# 🔹 4. Optionally, Store Results (User Feedback and Accuracy)
df["Pass/Fail"] = df["Holding Response Accuracy"].apply(lambda x: "Pass" if x else "Fail")

# 🔹 5. Save the Results to a New Excel File
df.to_excel("holding_responses_with_results.xlsx", index=False)

# 🔹 6. Output Results
print("\n📊 Holding Response Accuracy Report:")
print(df[["Request Type", "Holding Response", "Holding Response Accuracy", "Pass/Fail"]])

print(f"\n✅ Overall Holding Response Accuracy: {holding_accuracy:.2f}%")
