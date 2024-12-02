import pandas as pd

def calculate_jaccard_similarity(file1, column1, file2, column2):
    """
    Calculate Jaccard similarity between two word lists stored in Excel files.
    
    Parameters:
        file1 (str): Path to the first Excel file.
        column1 (str): Column name containing the word list in the first file.
        file2 (str): Path to the second Excel file.
        column2 (str): Column name containing the word list in the second file.
        
    Returns:
        float: Jaccard similarity score.
    """
    # Load word lists from Excel files
    words1 = pd.read_excel(file1)[column1].dropna().unique()
    words2 = pd.read_excel(file2)[column2].dropna().unique()

    # Convert to sets
    set1 = set(words1)
    set2 = set(words2)

    # Calculate Jaccard similarity
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    jaccard_similarity = intersection / union if union != 0 else 0

    return jaccard_similarity

# Example usage
file1 = "word_list1.xlsx"  # Path to the first Excel file
column1 = "Words"         # Column name for the first file
file2 = "word_list2.xlsx"  # Path to the second Excel file
column2 = "Words"         # Column name for the second file

similarity = calculate_jaccard_similarity(file1, column1, file2, column2)
print(f"Jaccard Similarity: {similarity}")
