from dictionaries import dictionary
import sys


class KnownLetter:
    def __init__(self, letter, position):
        self.letter = letter
        self.position = position

    def is_here(self, word):
        if len(word) >= self.position + 1 and word[self.position] == self.letter:
            return True
        return False


class CheckPatternConfig:
    def __init__(self):
        self.language = None
        self.known_letters = []
        self.illegal_letters = []
        self.pattern = None

    def set_pattern(self, pattern):
        self.pattern = pattern

    def set_known_letter(self, known_letter_arg):
        if "," not in known_letter_arg:
            raise ValueError("Wrong known letter definition: " + known_letter_arg)
        letter = known_letter_arg.split(",")[0]
        position = int(known_letter_arg.split(",")[1]) - 1
        if position < 0:
            raise ValueError("Wrong known letter definition: the position must be greater than zero!")
        self.known_letters.append(KnownLetter(letter, position))

    def set_illegal_letter(self, illegal_letter):
        if len(illegal_letter) < 1:
            raise ValueError("Wrong illegal letter definition: " + illegal_letter)
        for letter in illegal_letter:
            if letter not in self.illegal_letters:
                self.illegal_letters.append(letter)

    def set_language(self, language):
        self.language = language


def parse_arguments(arguments):
    configuration = CheckPatternConfig()
    switcher = {
        'i': configuration.set_illegal_letter,
        'k': configuration.set_known_letter,
        'l': configuration.set_language
    }
    parse_state = None
    for index, argument in enumerate(arguments):
        if argument.startswith("-"):
            if len(argument) != 2 or argument[1] == "-":
                raise ValueError("Unknown argument: " + argument)
            parse_state = argument[1]
        else:
            if parse_state is None:
                if index == len(arguments) - 1:
                    configuration.set_pattern(argument)
                else:
                    raise ValueError("Illegal arguments!")
            else:
                if parse_state not in switcher.keys():
                    raise ValueError("Illegal arguments!")
                else:
                    switcher[parse_state](argument)
            parse_state = None
    if configuration.pattern is None:
        raise ValueError("Illegal arguments: a pattern/word must be specified!")
    if configuration.language is None:
        raise ValueError("Illegal arguments: a language must be specified!")
    return configuration


def check_known_letters(wordlist, config):
    output = []
    for word in wordlist:
        is_compliant = True
        for letter in config.known_letters:
            if not letter.is_here(word):
                is_compliant = False
        if is_compliant:
            output.append(word)
    return output


def check_illegal_letters(wordlist, config):
    output = []
    for word in wordlist:
        is_compliant = True
        for letter in config.illegal_letters:
            if letter in word:
                is_compliant = False
        if is_compliant:
            output.append(word)
    return output


def main():
    arguments = sys.argv[1:]
    arguments = [string.lower() for string in arguments]
    configuration = parse_arguments(arguments)
    wordlist = dictionary.lookup_pattern(configuration.pattern, configuration.language)
    wordlist = check_known_letters(wordlist, configuration)
    wordlist = check_illegal_letters(wordlist, configuration)
    for word in wordlist:
        print(word)


if __name__ == "__main__":
    main()
