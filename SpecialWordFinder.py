class SpecialWordFinder(WordFinder):


    """editing parse function, so that comments are excluded"""

    def parse(self, dict_file):
    

        return [w.strip() for w in dict_file
        if w.strip() and not w.startswith('#')]
