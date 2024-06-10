"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start = 0):
        self.start = self.next = start

    def __repr__(self):


        return f"<SerialGenerator start={self.start} next={self.next}>"

    def generate(self):
        """ generate number, needs to be incrimented by 1 everytime called.  I had to check soltuion, I believe self.next -1 in return
        is because .next is alreader returning the next iterable, but still needs to be incrimented."""
        
        self.next += 1
        return self.next - 1

    def reset(self):
        """ reset number """

        self.next = self.start

