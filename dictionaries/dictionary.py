# Source: https://github.com/dwyl/english-words
import os
import shutil
import json


def get_dictionary(language):
    if language in __dictionary__.keys():
        output = []
        with open(__dictionary__[language], "r") as infile:
            for line in infile:
                output.append(line.rstrip("\n"))
        return output
    return None


def list_dictionaries():
    return __dictionary__.keys()


def __remove_pattern_dir__(language):
    patterns_dir = os.path.join(".", "patterns")
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
        if char not in char_map.keys():
            char_map[char] = unique
            unique += 1
        pattern += __alphabet__[language][char_map[char]]
    return pattern, unique


def __build_pattern_map__(language):
    patterns = {}
    wordlist = get_dictionary(language)
    for word in wordlist:
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
    language_dir = os.path.join(".", "patterns", language)
    os.mkdir(language_dir)
    for word_length in patterns.keys():
        os.mkdir(os.path.join(language_dir, word_length))


def __save_pattern_map__(language, patterns):
    language_dir = os.path.join(".", "patterns", language)
    for word_length in patterns.keys():
        word_length_dir = os.path.join(language_dir, word_length)
        for word_unique in patterns[word_length].keys:
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
    __remove_pattern_dir__(language) # remove any previous pattern map
    patterns = __build_pattern_map__(language)
    __build_pattern_map_directories__(language, patterns)
    __save_pattern_map__(language, patterns)


def get_pattern_map(language):
    """Reads the file that maps each bucket of a language's patterns to the bucket file.

    :param language: the desired language
    :return: a dictionary that can be navigated to reach the right bucket file

    If the language is not available, an error should be thrown.

    If the language is available, but no map is available, a map should be generated.

    If the language and the map are available, the map should be retrieved and returned."""
    return {}


def lookup_pattern(pattern, language):
    """Looks up a specific pattern and returns all matching words.

    :param pattern: the desired pattern
    :param language: the desired language
    :return: a list of all words matching the pattern in the specified language
    """
    return []


__dictionary__ = {
    "en": "english.txt"
}

__alphabet__ = {
    "en": "abcdefghijklmnopqrstuvwxyz"
}