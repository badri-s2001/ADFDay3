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
    unique_file = str(uuid.uuid4()) + ".txt"

    def __init__(self, file):
        logging.info('ReadWrite constructor called')
        self.file = file

    def get_content(self):
        logging.info('Receiving data from input text file')
        return self.file.read()

    def append_unique_file(self, content):
        with open(self.unique_file, mode='a') as my_file:
            my_file.write(content)


class Operations(ReadWrite):
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
        logging.info('Operations constructor called')
        super().__init__(file)
        self.content = super().get_content()
        self.list_words = self.content.split()
        logging.info('Received list of words')

    def prefix_to_fn(self, word):
        if word[0:2] == "to":
            self.prefix_to.append(word)

    def end_ing_fn(self, word):
        if word[-3:] == "ing":
            self.end_ing.append(word)

    def palindrome_fn(self, word):
        if word == word[::-1]:
            self.palindrome.append(word)

    def rep_dict_fn(self, word):
        if not self.rep_dict.get(word):
            self.rep_dict[word] = 1
            self.unique_words.append(word)

        if self.rep_dict.get(word):
            self.rep_dict[word] += 1

    def count_dict_fn(self, count, word):
        self.count_dict[count + 1] = word

    def split_vowels_fn(self, word):
        split_vowels = re.split('[aeiou]', word)
        self.vowel_words.append(split_vowels)

    def cap_third_fn(self, word):
        a = list(word)
        a[2] = a[2].upper()
        s = ''.join(a)
        self.cap_third.append(s)

    def cap_fifth_fn(self):
        self.cap_fifth = self.list_words[::]
        self.cap_fifth[4] = self.cap_fifth[4].upper()

    def replace_fn(self):
        self.new_string = self.content.replace(" ", "-")
        self.new_string = self.new_string.replace("\n", ";")

    def make_operations(self):
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

    def print_to_console(self):
        logging.info('Started printing to console')
        print(f"There are {len(self.prefix_to)} words with prefix 'to'")
        print(f"There are {len(self.end_ing)} words ending with 'ing'")
        most_rep = max(zip(self.rep_dict.values(), self.rep_dict.keys()))[1]
        print(f"The word that was repeated the maximum number of times is '{most_rep}'")
        print(f"The palindromes present in the file are :\n{self.palindrome}")
        print(f"Unique words in the list are: \n{self.unique_words}")
        print(f"The counter dict of the file is: \n{self.count_dict} ")
        logging.info('Finished printing to console file')

    def write_to_file(self):
        logging.info('Started writing content to output file')
        super().append_unique_file(f"Split the words based on the vowels\n{str(self.vowel_words)}\n\n")
        super().append_unique_file(f"Capitalize 3rd letter of every word\n{str(self.cap_third)}\n\n")
        super().append_unique_file(f"Capitalize 5th word of the file\n{str(self.cap_fifth)}\n\n")
        super().append_unique_file(f"Content after replacing space with '-' and new line with ';'\n{self.new_string}")
        logging.info('Finished writing content to output file')


input_file = sys.argv[1]
if os.stat(input_file).st_size == 0:
    logging.warning('Input file is empty')
    print("Input text file is empty")


else:
    with open(input_file, mode='r') as f:
        rr = Operations(f)
        rr.make_operations()
        rr.print_to_console()
        rr.write_to_file()
        f.close()
        logging.info('Program successfully finished')
