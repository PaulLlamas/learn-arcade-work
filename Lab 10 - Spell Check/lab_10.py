import re

# This function takes in a line of text and returns
# a list of words in the line.


def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)


def read_dictionary():
    dictionary = open("dictionary.txt")

    dictionary_list = []

    for line in dictionary:
        line = line.strip()
        dictionary_list.append(line)

    dictionary.close()

    print(f"There are {len(dictionary_list)} words in the document.")


def read_story():
    story = open("AliceInWonderLand200.txt")

    story_list = []

    for line in story:
        line = line.strip()
        story_list.append(line)

    story.close()

    print(f"There are {len(story_list)} words in the document.")


def main():
    print("--- Linear Search ---")

    dictionary = open("dictionary.txt")

    dictionary_list = []

    for line in dictionary:
        line = line.strip()
        dictionary_list.append(line)

    dictionary.close()

    story = open("AliceInWonderLand200.txt")

    error_position = 0
    for line in story:
        word_list = split_line(line)
        error_position += 1
        for word in word_list:
            current_list_position = 0
            while current_list_position < len(dictionary_list) \
                    and dictionary_list[current_list_position] != word.upper():
                current_list_position += 1
            if current_list_position == len(dictionary_list):
                print(f"The mistake is in line {error_position} and the word is {word}.")
    story.close()

    print("--- Binary Search ---")
    dictionary = open("dictionary.txt")

    dictionary_list = []

    for line in dictionary:
        line = line.strip()
        dictionary_list.append(line)

    dictionary.close()

    story = open("AliceInWonderLand200.txt")

    error_position = 0
    for line in story:
        word_list = split_line(line)
        error_position += 1
        for word in word_list:
            lower_bound = 0
            upper_bound = len(dictionary_list) - 1
            found = False
            while lower_bound <= upper_bound and not found:
                middle_pos = (lower_bound + upper_bound) // 2
                if dictionary_list[middle_pos] < word.upper():
                    lower_bound = middle_pos + 1
                elif dictionary_list[middle_pos] > word.upper():
                    upper_bound = middle_pos - 1
                else:
                    found = True
            if not found:
                print(f"The mistake is in line {error_position} and the word is {word}.")
    story.close()


main()
