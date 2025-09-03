import sys
import string
from collections import Counter

def analyze_text(filepath):
    """
    Analyzes a text file to count words, sentences, and characters,
    and finds the top 5 most common words.

    Args:
        filepath (str): The path to the text file.
    """
    try:
        # A common cause of the error you received is a different file encoding.
        # This is a more robust way to open files that may not be standard UTF-8.
        # It tries 'utf-8' first, then falls back to 'utf-16'.
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                text = file.read()
        except UnicodeDecodeError:
            with open(filepath, 'r', encoding='utf-16') as file:
                text = file.read()
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

    # 1. Character Count
    char_count = len(text)

    # 2. Word Count
    words = text.split()
    word_count = len(words)

    # 3. Sentence Count
    # A simple approach is to count common sentence-ending punctuation.
    sentence_count = text.count('.') + text.count('?') + text.count('!')

    # 4. Most Common Words (Top 5)
    # Remove punctuation and convert to lowercase for accurate counting
    translator = str.maketrans('', '', string.punctuation)
    clean_text = text.lower().translate(translator)
    
    # Split the clean text into a list of words
    clean_words = clean_text.split()
    
    # Use collections.Counter to find the most common words
    word_counts = Counter(clean_words)
    most_common = word_counts.most_common(5)

    # 5. Print Results
    print("\n--- Text Analysis Report ---")
    print(f"File: {filepath}")
    print("-" * 28)
    print(f"Total Characters: {char_count}")
    print(f"Total Words: {word_count}")
    print(f"Total Sentences: {sentence_count}")
    print("\nTop 5 Most Common Words:")
    for word, count in most_common:
        print(f"  - '{word}': {count} times")
    print("----------------------------\n")

if __name__ == "__main__":
    # Check if a file path was provided as a command-line argument
    if len(sys.argv) < 2:
        print("Usage: python text_analyzer.py <filename>")
        print("Example: python text_analyzer.py my_document.txt")
    else:
        file_path = sys.argv[1]
        analyze_text(file_path)
