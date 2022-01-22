from dictionaries import dictionary
import sys
import argparse


program_epilog = (
    "",
    "EXAMPLES:",
    "",
    "python3 check_pattern.py -l en -k m,1 -k s,3 -i rab cjddjke",
    "",
    "  this would identify a word with the pattern cjddjke, where c is known to",
    "  represent the letter m, d is known to represent the letter s, the letters r, a",
    "  and b are known to be missing."
)


class KnownLetter:
    def __init__(self, letter, position):
        self.letter = letter
        self.position = int(position)

    def is_here(self, word):
        if len(word) >= self.position + 1 and word[self.position] == self.letter:
            return True
        return False


def known_letter_argument(argument):
    argument = argument.split(",")
    return KnownLetter(argument[0], argument[1])


def check_known_letters(wordlist, config):
    output = []
    for word in wordlist:
        is_compliant = True
        for letter in config.known:
            if not letter.is_here(word):
                is_compliant = False
        if is_compliant:
            output.append(word)
    return output


def check_illegal_letters(wordlist, config):
    output = []
    for word in wordlist:
        is_compliant = True
        for letter in config.illegal:
            if letter in word:
                is_compliant = False
        if is_compliant:
            output.append(word)
    return output


def check_aca_illegal_letters(wordlist, config):
    output = []
    for word in wordlist:
        is_compliant = True
        for index, letter in enumerate(word):
            if letter == config.pattern[index]:
                is_compliant = False
        if is_compliant:
            output.append(word)
    return output


def main():
    argument_parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="A program to check word patterns against a dictionary to help solve cryptograms.",
        epilog="\n".join(program_epilog)
    )
    argument_parser.add_argument("-k", "--known", action="append", type=known_letter_argument, help="A known letter and its position, comma-separated (starting from 0 for the first character).")
    argument_parser.add_argument("-i", "--illegal", action="append", help="A letter that can't be part of the word.")
    argument_parser.add_argument("-l", "--language", required=True, help="The dictionary to be used.")
    argument_parser.add_argument("-a", "--aca", action="store_true", help="Flag if ACA rules should be applied.")
    argument_parser.add_argument("pattern", help="The pattern word that you're looking for.")
    configuration = argument_parser.parse_args()
    wordlist = dictionary.lookup_pattern(configuration.pattern, configuration.language)
    if configuration.known is not None:
        wordlist = check_known_letters(wordlist, configuration)
    if configuration.illegal is not None:
        wordlist = check_illegal_letters(wordlist, configuration)
    if configuration.aca:
        wordlist = check_aca_illegal_letters(wordlist, configuration)
    for word in wordlist:
        print(word)


if __name__ == "__main__":
    main()
