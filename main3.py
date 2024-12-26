def count_words_and_paragraphs(text):
    if not text.strip():
        return "The input is empty. Please enter some text."

    # Split the text into words
    words = text.split()
    word_count = len(words)

    # Split the text into paragraphs
    paragraphs = text.split('\n')
    # Filter out empty paragraphs
    paragraphs = [p for p in paragraphs if p.strip()]
    paragraph_count = len(paragraphs)

    return word_count, paragraph_count

# Example usage
input_text = input("Enter the text or paragraph: ")
word_count, paragraph_count = count_words_and_paragraphs(input_text)

if isinstance(word_count, str):
    print(word_count)  # This will print the message if the input is empty
else:
    print(f"The number of words in the given text is: {word_count}")
    print(f"The number of paragraphs in the given text is: {paragraph_count}")
