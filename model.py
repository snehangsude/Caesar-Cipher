from data import alphabet


class Cipher:
    """class contains methods to encrypt and decryot a text based on move"""

    def __init__(self):
        self.list = []
        self.new_word = []

    def convert(self, text=""):
        """Converts the input text into a list"""
        for letter in text:
            self.list.append(letter)

    def encrypt(self, text="", move=0):
        """Encrypts the user input based on move"""
        self.new_word.clear()
        self.convert(text)
        move = move % 26
        for letter in self.list:
            if letter not in alphabet:
                self.new_word.append(letter)
            else:
                position = alphabet.index(letter)
                self.new_word.append(alphabet[position + move])
        self.list.clear()
        return "".join(self.new_word)

    def decrypt(self, text="", move=0):
        """Decrypts the user input based on move"""
        self.new_word.clear()
        self.convert(text)
        move = move % 26
        for letter in self.list:
            if letter not in alphabet:
                self.new_word.append(letter)
            else:
                position = alphabet.index(letter)
                self.new_word.append(alphabet[position - move])
        self.list.clear()
        return "".join(self.new_word)
