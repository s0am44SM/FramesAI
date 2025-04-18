import pandas as pd
from nltk.tokenize import word_tokenize
import difflib

# -----------------------------
# Helper: Get punctuation only
# -----------------------------
def extract_punctuation(text):
    tokens = word_tokenize(text)
    return [t for t in tokens if not t.isalnum()]

# -----------------------------
# Helper: Calculate accuracy
# -----------------------------
def punctuation_accuracy(transcribed, reference):
    trans_punct = extract_punctuation(transcribed)
    ref_punct = extract_punctuation(reference)

    correct = sum(1 for t in trans_punct if t in ref_punct)
    accuracy = (correct / max(1, len(ref_punct))) * 100

    return round(accuracy, 2), trans_punct, ref_punct

# -----------------------------
# Helper: Show diff (optional)
# -----------------------------
def punctuation_diff(transcribed, reference):
    trans = ''.join([c for c in transcribed if not c.isalnum() and not c.isspace()])
    ref = ''.join([c for c in reference if not c.isalnum() and not c.isspace()])
    diff = difflib.ndiff(ref, trans)
    return '\n'.join(diff)

# -----------------------------
# Main Function
# -----------------------------
def evaluate_punctuation(file_path, output_path):
    df = pd.read_excel(file_path)

    results = []
    for _, row in df.iterrows():
        trans = row['Transcribed Text']
        ref = row['Reference Text']
        acc, trans_p, ref_p = punctuation_accuracy(trans, ref)
        diff = punctuation_diff(trans, ref)
        results.append({
            'Punctuation Accuracy (%)': acc,
            'Transcribed Punctuation': ''.join(trans_p),
            'Reference Punctuation': ''.join(ref_p),
            'Punctuation Diff': diff
        })

    # Append results to original DataFrame
    result_df = pd.concat([df, pd.DataFrame(results)], axis=1)
    result_df.to_excel(output_path, index=False)
    print(f"✅ Evaluation complete! Results saved to: {output_path}")

# -----------------------------
# Run
# -----------------------------
if __name__ == "__main__":
    import nltk
    nltk.download('punkt')

    input_excel = "transcripts.xlsx"     # <-- Your input file
    output_excel = "punctuation_results.xlsx"  # <-- Your output file
    evaluate_punctuation(input_excel, output_excel)
