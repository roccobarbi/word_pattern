from dictionaries import dictionary
import sys


def parse_arguments(arguments):
    configuration = {
        "language": ""
    }
    err = None
    return configuration, err


def generate_pattern(pattern, config, wordlist):
    # translate
    return ""


def lookup_pattern(pattern, config, wordlist):
    # translate
    pass


def main():
    arguments = sys.argv[1:]
    config, err = parse_arguments(arguments)
    if err is not None:
        sys.exit(1)
    wordlist = dictionary.get_dictionary(config["language"])
    if wordlist is None:
        sys.exit(1)
    pattern = generate_pattern(config)  # Generate a pattern in the right format
    return lookup_pattern(pattern, config, wordlist)


if __name__ == "__main__":
    main()