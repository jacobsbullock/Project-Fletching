import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
from collections import Counter

def load_excel_file():
    """Opens a file dialog to select an Excel file."""
    file_path = filedialog.askopenfilename(
        filetypes=[("Excel Files", "*.xlsx *.xls"), ("All Files", "*.*")]
    )
    return file_path

def calculate_similarity(words1, words2):
    """Calculates the percentage similarity between two lists of words."""
    words1_set = set(words1)
    words2_set = set(words2)
    intersection = words1_set.intersection(words2_set)
    union = words1_set.union(words2_set)
    return round((len(intersection) / len(union)) * 100, 2) if union else 0.0

def compare_lists(corpus_file, comparison_files):
    """Compares words in the standard corpus against selected files."""
    try:
        corpus_data = pd.read_excel(corpus_file)
        corpus_words = corpus_data.iloc[:, 0].dropna().str.strip().tolist()

        results = []
        for file in comparison_files:
            comp_data = pd.read_excel(file)
            comp_words = comp_data.iloc[:, 0].dropna().str.strip().tolist()
            similarity = calculate_similarity(corpus_words, comp_words)
            results.append((file, similarity))
        return results
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
        return []

def browse_corpus():
    global corpus_path
    corpus_path = load_excel_file()
    corpus_label.config(text=f"Corpus Loaded: {corpus_path}")

def browse_files():
    global comparison_paths
    comparison_paths = filedialog.askopenfilenames(
        filetypes=[("Excel Files", "*.xlsx *.xls"), ("All Files", "*.*")]
    )
    files_label.config(text=f"{len(comparison_paths)} Files Selected")

def compare_action():
    if not corpus_path:
        messagebox.showerror("Error", "Please load the standard corpus file.")
        return
    if not comparison_paths:
        messagebox.showerror("Error", "Please select files to compare.")
        return

    results = compare_lists(corpus_path, comparison_paths)
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, "Comparison Results:\n")
    for file, similarity in results:
        result_text.insert(tk.END, f"{file}: {similarity}% similarity\n")

# GUI Setup
root = tk.Tk()
root.title("Word List Similarity Checker")

# Load Corpus Button
corpus_label = tk.Label(root, text="No Corpus Loaded")
corpus_label.pack(pady=5)
corpus_button = tk.Button(root, text="Load Corpus", command=browse_corpus)
corpus_button.pack(pady=5)

# Select Files Button
files_label = tk.Label(root, text="No Files Selected")
files_label.pack(pady=5)
files_button = tk.Button(root, text="Select Files to Compare", command=browse_files)
files_button.pack(pady=5)

# Compare Button
compare_button = tk.Button(root, text="Compare", command=compare_action)
compare_button.pack(pady=10)

# Results Text Box
result_text = tk.Text(root, wrap=tk.WORD, width=60, height=20)
result_text.pack(pady=10)

# Global Variables
corpus_path = None
comparison_paths = []

root.mainloop()
