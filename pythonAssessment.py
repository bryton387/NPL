import re


# Backup article text in case the text file is not in the same folder.
ARTICLE_TEXT = """ACME Inc. Unveils Revolutionary Apple Pie Machine, Transforming Baking with Automation

ACME Inc., a leading innovator in culinary technology, has launched a groundbreaking new device that promises to revolutionize the way apple pies are made. Dubbed the "Apple Pie Master," this machine combines cutting-edge technology with traditional baking techniques to automate the entire pie-making process, ensuring perfect pies every time.

At a press conference held at ACME Inc.'s headquarters in Springfield, the company's CEO, Jane Doe, introduced the Apple Pie Master to an eager audience of journalists, culinary experts, and industry insiders. "Our goal has always been to make cooking and baking accessible and enjoyable for everyone, and with the Apple Pie Master, we are making a giant leap forward," Doe stated.

The Apple Pie Master is designed to simplify the baking process while maintaining the quality and taste of a homemade pie. The machine is equipped with AI-driven sensors that can analyze the quality of ingredients, adjust cooking times, and even replicate intricate baking techniques perfected by master chefs. "This isn't just about saving time; it's about enhancing the baking experience and ensuring consistent results," Doe explained.

Unpacking the Technology

The heart of the Apple Pie Master lies in its advanced artificial intelligence system. This system is programmed to perform tasks such as peeling and slicing apples, mixing ingredients, and rolling out pie crusts. According to ACME Inc.'s head of product development, Dr. Emily Clark, "The AI not only replicates human actions but learns from each pie made, adjusting its techniques to improve the next one."

Another innovative feature of the Apple Pie Master is its real-time monitoring capabilities. Cameras and sensors inside the machine provide continuous feedback during the pie-making process, allowing the AI to make micro-adjustments to the temperature and cooking times as needed. This ensures that each pie is baked to golden perfection.

User-Friendly Features

ACME Inc. has designed the Apple Pie Master with user experience in mind. The machine features a sleek, user-friendly interface with pre-programmed settings for different pie recipes."""


def read_article(filename):
    # This tries to read the article from a file first.
    try:
        with open(filename, "r", encoding="utf-8") as file:
            article = file.read()
    except FileNotFoundError:
        article = ARTICLE_TEXT

    return article


def count_specific_word(text, search_word):
    # Convert both strings to lowercase so the search is not case sensitive.
    if search_word == "":
        return 0
    else:
        count = text.lower().count(search_word.lower())
        return count


def identify_most_common_word(text):
    # Regex gets words without punctuation.
    words = re.findall(r"\b\w+\b", text.lower())

    if len(words) == 0:
        return None
    else:
        word_counts = {}

        for word in words:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1

        most_common_word = words[0]

        for word in word_counts:
            if word_counts[word] > word_counts[most_common_word]:
                most_common_word = word

        return most_common_word


def calculate_average_word_length(text):
    words = re.findall(r"\b\w+\b", text)

    if len(words) == 0:
        return 0.0
    else:
        total_length = 0

        for word in words:
            total_length += len(word)

        average_length = total_length / len(words)
        return average_length


def main():
    article = read_article("news_article.txt")
    search_word = "Apple"

    word_count = count_specific_word(article, search_word)
    most_common_word = identify_most_common_word(article)
    average_word_length = calculate_average_word_length(article)

    print("News Article Text Analysis")
    print("--------------------------")
    print("Specific word:", search_word)
    print("Specific word count:", word_count)
    print("Most common word:", most_common_word)
    print("Average word length:", average_word_length)


if __name__ == "__main__":
    main()
