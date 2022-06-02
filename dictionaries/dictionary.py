# Source: https://github.com/dwyl/english-words
import os
import shutil
import json


def is_pattern_word(word):
    alphabet = {}
    for character in word:
        if character in alphabet.keys():
            return True  # At least a letter is repeated, at least once
        else:
            alphabet[character] = 1
    return False


def get_dictionary(language):
    module_dir, module_file = os.path.split(__file__)
    if language in __dictionary__.keys():
        output = []
        with open(os.path.join(module_dir, __dictionary__[language]), "r") as infile:
            for line in infile:
                output.append(line.rstrip("\n").lower())
        return output
    return None


def list_dictionaries():
    return __dictionary__.keys()


def __remove_pattern_dir__(language):
    module_dir, module_file = os.path.split(__file__)
    patterns_dir = os.path.join(module_dir, "patterns")
    language_dir = os.path.join(patterns_dir, language)
    if os.path.exists(patterns_dir) and os.path.isdir(patterns_dir):
        if os.path.exists(language_dir):
            if os.path.isdir(language_dir):
                shutil.rmtree(language_dir)
            else:
                os.remove(language_dir)


def build_word_pattern(word, language):
    """Given a word and a language, calculate the word pattern and the number of unique character is has."""
    pattern = ""
    unique = 0
    char_map = {}
    for char in word:
        if char in ['\'', '-']:
            pattern += char
        else:
            if char not in char_map.keys():
                char_map[char] = unique
                unique += 1
            pattern += __alphabet__[language][char_map[char]]
    return pattern, unique


def __build_pattern_map__(language):
    patterns = {}
    wordlist = get_dictionary(language)
    for word in wordlist:
        if is_pattern_word(word):
            word_pattern, word_unique = build_word_pattern(word, language)
            if len(word) not in patterns.keys():
                patterns[len(word)] = {}
            if word_unique not in patterns[len(word)]:
                patterns[len(word)][word_unique] = {}
            if word_pattern not in patterns[len(word)][word_unique]:
                patterns[len(word)][word_unique][word_pattern] = []
            patterns[len(word)][word_unique][word_pattern].append(word)
    return patterns


def __build_pattern_map_directories__(language, patterns):
    module_dir, module_file = os.path.split(__file__)
    patterns_dir = os.path.join(module_dir, "patterns")
    if not os.path.exists(patterns_dir):
        os.mkdir(patterns_dir)
    language_dir = os.path.join(patterns_dir, language)
    os.mkdir(language_dir)
    for word_length in patterns.keys():
        os.mkdir(os.path.join(language_dir, str(word_length)))


def __save_pattern_map__(language, patterns):
    module_dir, module_file = os.path.split(__file__)
    language_dir = os.path.join(module_dir, "patterns", language)
    for word_length in patterns.keys():
        word_length_dir = os.path.join(language_dir, str(word_length))
        for word_unique in patterns[word_length].keys():
            with open(os.path.join(word_length_dir, str(word_unique) + ".json"), "w", encoding="utf-8") as outfile:
                json.dump(patterns[word_length][word_unique], outfile, ensure_ascii=False, indent=4)


def generate_pattern_map(language):
    """Sets up the project with a pattern map for the specified language.

    :param language: the desired language
    :return:

    The dictionary is divided in buckets based on each word's length.
    Each bucket is further divided in sub-buckets based on the number of unique letters.
    Each sub-bucket is a json file that maps each pattern to the words in that pattern.
    Another file is used to map each bucket (length and unique letters) to its file.

    Patterns should be compiled by assigning "a" to the first letter, "b" to the second, and so on.
    For example, "ancillary" would have the pattern "abcdeeafg"."""
    if language not in __dictionary__.keys():
        raise ValueError("Unknown language code: " + language)
    __remove_pattern_dir__(language)  # remove any previous pattern map
    patterns = __build_pattern_map__(language)
    __build_pattern_map_directories__(language, patterns)
    __save_pattern_map__(language, patterns)


def lookup_pattern(pattern, language):
    """Looks up a specific pattern and returns all matching words.

    :param pattern: the desired word or pattern (the pattern is recreated to ensure consistency)
    :param language: the desired language
    :return: a list of all words matching the pattern in the specified language

    If the language does not exist, it throws an error.
    If the pattern map does not exist, it creates it.
    It looks up the pattern in the pattern_map and returns a list of all matching words.
    """
    if language not in __dictionary__.keys():
        raise ValueError("Unknown language code: " + language)
    pattern_map = {}
    module_dir, module_file = os.path.split(__file__)
    patterns_dir = os.path.join(module_dir, "patterns")
    language_dir = os.path.join(patterns_dir, language)
    if not os.path.exists(patterns_dir) or not os.path.isdir(patterns_dir) or not os.path.exists(language_dir):
        generate_pattern_map(language)
    word_pattern, word_unique = build_word_pattern(pattern, language)
    length_dir = os.path.join(language_dir, str(len(pattern)))
    map_file = os.path.join(length_dir, str(word_unique) + ".json")
    if os.path.exists(length_dir) and os.path.isdir(length_dir):
        if os.path.exists(map_file) and os.path.isfile(map_file):
            with open(map_file, "r") as infile:
                pattern_map = json.load(infile)
    if word_pattern in pattern_map.keys():
        return pattern_map[word_pattern]
    return []


__dictionary__ = {
    "en": "english.txt"
}

__alphabet__ = {
    "en": "abcdefghijklmnopqrstuvwxyz"
}