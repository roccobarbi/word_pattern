# Source: https://github.com/dwyl/english-words


def get_dictionary(language):
    if language in __dictionary__.keys():
        output = []
        with open(__dictionary__[language], "r") as infile:
            for line in infile:
                output.append(line.rstrip("\n"))
        return output
    return None


__dictionary__ = {
    "en": "english.txt"
}