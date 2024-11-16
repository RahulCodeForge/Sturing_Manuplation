# String Manipulation: Most Frequent Word Finder

This Python program helps you find the most frequent word in a sentence. It processes the sentence by removing punctuation, converting everything to lowercase, and then counting how many times each word appears. The program returns the word that appears the most.

## Features

- **Case Insensitive**: It makes all words lowercase so it doesn't matter if the word is in uppercase or lowercase.
- **Removes Punctuation**: It removes punctuation marks and focuses only on the words.
- **Counts Words**: It counts how many times each word appears in the sentence.
- **Handles Ties**: If two words appear the same number of times, it will return the first one that appears.

## How It Works

1. **Input**: You give the program a sentence (text).
2. **Process**:
   - The program converts the sentence to lowercase.
   - It removes any punctuation and splits the sentence into words.
   - It counts how many times each word appears.
3. **Output**: The program tells you which word appears the most.

### Example:
```python
sentence = "The quick brown fox jumps over the lazy dog. The fox was quick."
print(most_frequent_word(sentence))  # Output will be 'the'

## How to Run

### 1. Download and Extract the ZIP File
- Download the ZIP file containing the code.
- Extract the contents of the ZIP file to a folder on your computer.

### 2. Install Python (if not installed)
- Make sure you have **Python 3.x** installed on your system. You can download Python from the official website:  
  [Download Python](https://www.python.org/downloads/)

### 3. Open a Terminal or Command Prompt
- Open a terminal (Linux/Mac) or command prompt (Windows).

### 4. Navigate to the Folder Containing the Code
- Use the `cd` command to go to the folder where the ZIP file was extracted.
  - Example:  
    ```bash
    cd path/to/extracted/folder
    ```

### 5. Run the Program
- Once you're in the correct folder, run the Python script by typing the following command:
  ```bash
  python stringManipulation.py

