"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    ...



def __init__(self, path):
  """gain access to txt file, then create a dict of the words by parsing file.
    Then return length of words."""

    dict_file = open(path)

    self.words = self.parse(dict_file)

    print(f"{len(self.words)} words read")


def parse(self, dict_file):
    """parse words from file, using strip method to remove blank spaces around words"""

    return [w.strip() for w in dict_file]

def random(self):
    """get random word"""
    return random.choice(self.words)