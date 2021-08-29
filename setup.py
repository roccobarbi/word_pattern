"""Sets up the program with a precalculated set of patterns and words.

Unless new language are added, or existing ones are updated, setup needs to be run only once.
Setting up the program before using it will greatly improve its running time the first time it is used.
Subsequent executions for the same language should not be affected, since the same set of patterns and words that is
defined by the setup, is also defined when the program runs for the first time against a language that has not been set
up."""


from dictionaries import dictionary


def main():
    for language in dictionary.list_dictionaries():
        dictionary.generate_pattern_map(language)


if __name__ == "__main__":
    main()
