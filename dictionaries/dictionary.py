# Source: https://github.com/dwyl/english-words


def get_dictionary(language):
    if language in __dictionary__.keys():
        output = []
        with open(__dictionary__[language], "r") as infile:
            for line in infile:
                output.append(line.rstrip("\n"))
        return output
    return None


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
    pass


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