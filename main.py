"""
Performs various operations in the file.
Prints some to the console.
While others are written to the output file.
"""

import sys
import os
import uuid
import re
import logging

logging.basicConfig(filename="log.txt",
                    filemode='a',
                    format='%(asctime)s %(levelname)s-%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=1,
                    )


class ReadWrite:
    """
    Reads a file. Writes a unique file
    """

    unique_file = str(uuid.uuid4()) + ".txt"

    def __init__(self, file):
        """
        ReadWrite Constructor
        :param file: The file which you want to read
        """
        self.file = file

    def get_file_content(self):
        """
        Reads the file
        :return: File content
        """
        logging.info('Receiving data from input text file')
        return self.file.read()

    def append_unique_file(self, content):
        """
        Writes content to the unique file which is generated
        :param content: The content which you want to write to the file
        :return: True if writing content to the file is success
        """
        with open(self.unique_file, mode='a', encoding='UTF-8') as my_file:
            my_file.write(content)

        return True


class Operations(ReadWrite):
    """
    Performs various string operations
    """
    content = ""
    list_words = []
    prefix_to = []
    end_ing = []
    palindrome = []
    rep_dict = {}
    unique_words = []
    count_dict = {}
    vowel_words = []
    cap_third = []
    cap_fifth = []
    new_string = ""

    def __init__(self, file):
        """
        Operations Constructor
        :param file: The file from which you want to perform the operations.
        """
        ReadWrite.__init__(self, file)

    def get_content(self):
        """
        Gets string content and list of words from file
        :return: True if the content is received
        """
        self.content = ReadWrite.get_file_content(self)
        self.list_words = self.content.split()
        return True

    def prefix_to_fn(self, word):
        """
        Checks if a word has prefix "to" and adds it to list
        :param word: The word which you want to check
        :return: True if word has prefix "to"
        """
        ans = True
        if word[0:2] == "to":
            self.prefix_to.append(word)
        else:
            ans = False

        return ans

    def end_ing_fn(self, word):
        """
        Checks if a word ends with "ing" and adds it to list
        :param word: The word which you want to check
        :return: True if word ends with "ing"
        """
        ans = True
        if word[-3:] == "ing":
            self.end_ing.append(word)
        else:
            ans = False

        return ans

    def palindrome_fn(self, word):
        """
        Checks if a word is a palindrome and adds it to list
        :param word: The word which you want to check
        :return: True if word is a palindrome
        """
        ans = True

        if word == word[::-1]:
            self.palindrome.append(word)
        else:
            ans = False

        return ans

    def rep_dict_fn(self, word):
        """
        Adds the word to dict to check how many times its repeating
        :param word: The word which you want to add to dict
        :return: True after completing
        """
        if not self.rep_dict.get(word):
            self.rep_dict[word] = 1
            self.unique_words.append(word)

        if self.rep_dict.get(word):
            self.rep_dict[word] += 1

        return True

    def count_dict_fn(self, count, word):
        """
        Adds the word to a dict which indexes it
        :param count: The index of the word
        :param word: The word which you want to add to the dict
        :return: True after completing
        """
        self.count_dict[count + 1] = word

    def split_vowels_fn(self, word):
        """
        Splits the word based on vowels and adds it to the list
        :param word: The word which you want to split by vowels
        :return: The list of split words
        """
        split_vowels = re.split('[aeiou]', word)
        self.vowel_words.append(split_vowels)

        return split_vowels

    def cap_third_fn(self, word):
        """
        Capitalises the third letter of the word and adds it to list
        :param word: The word who's third letter you want to capitalise
        :return: The string after capitalising third letter
        """
        list_word = list(word)
        list_word[2] = list_word[2].upper()
        string = ''.join(list_word)
        self.cap_third.append(string)

        return string

    def cap_fifth_fn(self):
        """
        Capitalises the fifth word of the file
        :return: True after completing
        """
        self.cap_fifth = self.list_words[::]
        self.cap_fifth[4] = self.cap_fifth[4].upper()

        return True

    def replace_fn(self):
        """
        Replaces space with "-" and new line with ";" in the file
        :return: True after completing
        """
        self.new_string = self.content.replace(" ", "-")
        self.new_string = self.new_string.replace("\n", ";")

        return True

    def make_operations(self):
        """
        Performs all the operations
        :return: True after completing
        """
        logging.info('Started doing operations')
        for count, word in enumerate(self.list_words):
            self.prefix_to_fn(word)
            self.end_ing_fn(word)
            self.palindrome_fn(word)
            self.rep_dict_fn(word)
            self.count_dict_fn(count, word)
            self.split_vowels_fn(word)
            self.cap_third_fn(word)
        self.cap_fifth_fn()
        self.replace_fn()
        logging.info('Finished doing operations')

        return True

    def print_to_console(self):
        """
        Prints content to the console
        :return: True after completing
        """
        logging.info('Started printing to console')
        print(f"There are {len(self.prefix_to)} words with prefix 'to'")
        print(f"There are {len(self.end_ing)} words ending with 'ing'")
        most_rep = max(zip(self.rep_dict.values(), self.rep_dict.keys()))[1]
        print(f"The word that was repeated the maximum number of times is '{most_rep}'")
        print(f"The palindromes present in the file are :\n{self.palindrome}")
        print(f"Unique words in the list are: \n{self.unique_words}")
        print(f"The counter dict of the file is: \n{self.count_dict} ")
        logging.info('Finished printing to console file')

        return True

    def write_to_file(self):
        """
        Writes content to the output file
        :return: True after completing
        """
        logging.info('Started writing content to output file')
        ReadWrite.append_unique_file \
            (self, f"Split the words based on the vowels\n{str(self.vowel_words)}\n\n")
        ReadWrite.append_unique_file \
            (self, f"Capitalize 3rd letter of every word\n{str(self.cap_third)}\n\n")
        ReadWrite.append_unique_file \
            (self, f"Capitalize 5th word of the file\n{str(self.cap_fifth)}\n\n")
        ReadWrite.append_unique_file \
            (self,
             f"Content after replacing space with '-' and new line with ';'\n{self.new_string}")
        logging.info('Finished writing content to output file')

        return True


if __name__ == "__main__":
    input_file = sys.argv[1]
    if os.stat(input_file).st_size == 0:
        logging.warning('Input file is empty')
        print("Input text file is empty")


    else:
        with open(input_file, mode='r', encoding='UTF-8') as f:
            rr = Operations(f)
            rr.get_content()
            rr.make_operations()
            rr.print_to_console()
            rr.write_to_file()
            f.close()
            logging.info('Program successfully finished')
