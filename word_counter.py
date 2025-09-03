import sys
import string
from collections import Counter

def word_counter(text):
    """
    Analyzes a string of text to count words, characters, and lines,
    and finds the top 3 most common words.

    Args:
        text (str): The text to be analyzed.
    """
    # 1. Character Count
    char_count = len(text)

    # 2. Word Count
    # A simple split() is enough for a basic word count.
    words = text.split()
    word_count = len(words)

    # 3. Line Count
    # Count the number of newline characters to get a line count.
    line_count = text.count('\n') + 1

    # 4. Most Common Words (Top 3)
    # Remove punctuation and convert to lowercase for accurate counting.
    translator = str.maketrans('', '', string.punctuation)
    clean_text = text.lower().translate(translator)
    
    # Split the clean text into a list of words.
    clean_words = clean_text.split()
    
    # Use collections.Counter to find the most common words.
    word_counts = Counter(clean_words)
    most_common = word_counts.most_common(3)

    # 5. Print Results
    print("\n--- Text Analysis Report ---")
    print("-" * 28)
    print(f"Total Characters: {char_count}")
    print(f"Total Words: {word_count}")
    print(f"Total Lines: {line_count}")
    print("\nTop 3 Most Common Words:")
    # Handle case where there are fewer than 3 unique words
    if most_common:
        for word, count in most_common:
            print(f"  - '{word}': {count} times")
    else:
        print("  - No words found.")
    print("----------------------------\n")

if __name__ == "__main__":
    # Check if a command-line argument was provided
    if len(sys.argv) < 2:
        print("Usage: python word_counter.py \"your text here\"")
        print("Example: python word_counter.py \"This is a simple text. This text is simple.\"")
    else:
        # Join all arguments to handle multi-word text within quotes
        input_text = " ".join(sys.argv[1:])
        word_counter(input_text)
