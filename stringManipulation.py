def most_frequent_word(sentence):
    # Convert to lowercase to ignore case differences
    sentence = sentence.lower()

    # Remove punctuation and split into words
    words = ""
    for char in sentence:
        if char.isalnum() or char == " ":  # Keep letters and spaces only
            words += char

    # Split the cleaned sentence into words
    word_list = words.split()

    # Count frequency of each word
    word_count = {}
    for word in word_list:
        if word in word_count:
            word_count[word] += 1  # Increment if word already in dictionary
        else:
            word_count[word] = 1  # Add word with count of 1 if new

    # Find the most frequent word, resolving ties by first occurrence
    most_frequent = ""
    max_count = 0
    for word in word_list:
        if word_count[word] > max_count:
            max_count = word_count[word]
            most_frequent = word

    return most_frequent

# Test example
sentence = "The quick brown fox jumps over the lazy dog. The fox was quick."
print(most_frequent_word(sentence))  # Output should be 'the'

