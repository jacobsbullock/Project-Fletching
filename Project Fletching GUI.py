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
