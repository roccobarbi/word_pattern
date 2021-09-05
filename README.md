# word_pattern

word_pattern is a python utility that helps you solve cryptograms by looking up word patterns in a dictionary.

## Why you should use word_pattern

There are many tools, online and offline, that help you solve cryptograms. One notable example being cryptools 2.

The main reasons why I build word_patterns, instead of using existing tools, are as follow:

- it is lightweight and easy to use from the command line;
- it is extremely easy to expand with custom dictionaries;
- it makes it easy to add constraints to the pattern lookup (e.g. certain letters in known positions, other letters
  known to be absent from the word you're looking for).
  
The ability to add constraints to the pattern lookup, in particular, can save a cryptogram solver a lot of time sifting
through long lists of words.

## How to use word_pattern

All commands in word_pattern have been set up to reference project files relative to the project path, so they can be
run safely from any path in your computer. All examples are written assuming you're in the project's root directory, but
this is not necessary for word_pattern to behave as expected.

Before the first use, I strongly recommend you to run `python3 setup.py`. This will go through all available
dictionaries, chunking them in a way that makes all subsequent executions more efficient. If you forget about this step,
the first execution in any language will take care of it for you (for that specific language only).

The basic syntax is: `python3 word_pattern.py -l {language} [options] {pattern}`

The {language} should be substituted with the 2-letter code for one of the supported languages, for example `-l en` and
it is mandatory.

The pattern can take any form. It can be encrypted in a simple substitution cypher (e.g. jrnxw) or plain (e.g. honey).
Whatever the form, the program will handle it as an unknown pattern.

### Options

| Option | Value |
|--------|-------|
|l       |Language code (e.g. en for english).|
|k       |Known characters in the form `{char},{position}`. For example, the letter "e" in the second position will be passed as `e,2`. Multiple characters and/or multiple positions require a separate option.|
|i       |Illegal characters in the form `{char}[{char}]`. Any number of characters can be passed to the -i option.|

Known characters are characters that you have already decrypted and CAN be found in the pattern. For example, in the
cryptogram `ijvxgydga qt d` you may have already decrypted the letters G=C, D=A. If you're looking up the pattern
`ijvxgydga`, you will use the command `python word_pattern.py -l en -k c,5 -k c,8 -k a,7 ijvxgydga`.

Illegal characters are characthers that you have already decrypted and can NOT be found in the pattern. For example, in
the cryptogram `ijvxgydga qt d` you may have already decrypted the letters G=C, D=A, Q=I, T=S. If you're looking up the
pattern `ijvxgydga`, you will use the command `python word_pattern.py -l en -k c,5 -k c,8 -k a,7 -I is ijvxgydga`.

As a result, a list of all words from the specified dictionary that follow the pattern and constraints will be printed
on screen.

## Contributing to this project

Please have a look at the [contributing guide](contributing.md).

You can also support this project [with a donation through Patreon](https://www.patreon.com/roccobarbi).