# Contributing to word_pattern

:+1::tada: First off, thanks for taking the time to contribute! :tada::+1:

The following is a set of guidelines for contributing to word_pattern.

## How Can I Contribute?

### Reporting Bugs and Feature Requests

If you believe something is not working as expected, or that a new feature should be added to word_pattern, feel free to
[open an issue here](https://github.com/roccobarbi/word_pattern/issues). Before opening an issue, read through the
existing open issues to check if someone already asked for what you desire. If you find either the same request, or a
very similar one, please do not open a duplicate issue, but rather comment the existing one to either show your support
or (preferably) add some new input to improve it.

### Adding or improving a dictionary

The quality of the output for this program depends mostly on the quantity and quality of its dictionaries.

Adding a dictionary is a straightforward process, but it requires a few, small changes to dictionaries/dictionary.py.
A complete guide to this process will be added soon. It goes without saying that adding support for a new language is
extremely useful to this project.

Editing a dictionary is a much simpler process. You only need to find the .txt file for the desired language under
dictionaries/, and to make the necessary changes. For example, you may want to add some conjugated form that may have
been omitted, or a list of proper names.

Please note that edits to dictionaries should be treated with a branch and a pull request like edits to the code.

### Contributing code WIP

In order to contribute to the project, please fork the project and create a new branch with a descriptive name. The
branch name must be all lowercase, underscore-separated text and it must begin with a letter.

Once you're done with your changes, please bring your branch up to date with main. Then submit a pull request, which
should detail at minimum:
- what the changes are about;
- a brief description of how they work;
- why it should be accepted.

Since all changes must be tracked using issues, the pull request must also include a reference to an issue (generally
using the "closes" keyword).