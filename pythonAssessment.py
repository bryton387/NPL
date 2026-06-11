import re

# This program is a news article analyzer.
# It reads an article from a text file and gives information about the text.
# The program uses functions so each part has one clear job.


# Read the news article from the txt file.
def read_article(filename):

    with open(filename, "r", encoding="utf-8") as file:
        
        return file.read()


# Count number of times a specific word appears
def count_specific_word(text, search_word):
    
    
    words = re.findall(r"\b\w+\b", text.lower())

   
    return words.count(search_word.lower())


# Find the most common word
def identify_most_common_word(text):
    
    words = re.findall(r"\b\w+\b", text.lower())

    # If there are no words, the function returns None instead of causing an error.
    if len(words) == 0:
        return None

    
    word_count = {}

    
    for word in words:
        # If the word is already there, add 1 to its count.
        if word in word_count:
            word_count[word] += 1
        else:
            
            word_count[word] = 1

    
    most_common = max(word_count, key=word_count.get)

    return most_common


# Calculate average word length
def calculate_average_word_length(text):

    # If the text is empty, return 0 because there are no words to measure.
    if text.strip() == "":
        return 0

    # This finds all the words without changing their letters.
    words = re.findall(r"\b\w+\b", text)

    # This is another safety check in case no words are found.
    if len(words) == 0:
        return 0

    
    total_letters = 0

    
    for word in words:
        total_letters += len(word)

    # Average word length is total letters divided by number of words.
    average = total_letters / len(words)

    return average


# Count paragraphs
def count_paragraphs(text):
    # If the article is empty, this program counts it as 1 paragraph.
    if text.strip() == "":
        return 1

    
    paragraphs = text.split("\n\n")

    count = 0

    # This loop only counts paragraphs that are not empty.
    for paragraph in paragraphs:
        if paragraph.strip() != "":
            count += 1

    return count


# Count sentences
def count_sentences(text):

    # If the article is empty, this program counts it as 1 sentence.
    if text.strip() == "":
        return 1

    # re.split separates the text whenever it finds 
    sentences = re.split(r"[.!?]+", text)

    count = 0

    # This loop only counts sentence parts that are not empty.
    for sentence in sentences:
        if sentence.strip() != "":
            count += 1

    return count


# Main function
def main():

    # This reads the article from the file and stores it in the article variable.
    article = read_article("news_article.txt")

    print("News article analyzer")

    search_word = ""

    # This while loop keeps asking until the user enters a real word.
    while search_word.strip() == "":
        search_word = input("Enter a word to search for: ")

    # These lines call the functions above and store their results in variables.
    word_count = count_specific_word(article, search_word)
    common_word = identify_most_common_word(article)
    average_length = calculate_average_word_length(article)
    paragraph_count = count_paragraphs(article)
    sentence_count = count_sentences(article)

    # These print statements display the final results to the user.
    print("\n---Results---")
    print(f"Occurrences of '{search_word}': {word_count}")
    print(f"Most common word: {common_word}")
    print(f"Average word length: {average_length:.2f}")
    print(f"Number of paragraphs: {paragraph_count}")
    print(f"Number of sentences: {sentence_count}")


if __name__ == "__main__":
    # This means the main function runs when this file is opened directly.
    main()
