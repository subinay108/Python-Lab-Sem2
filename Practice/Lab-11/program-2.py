# WAP that accepts a hyphen-separated sequence of words as input and call a function convert()
# which converts it into a hyphen-separated sequence after sorting then alphabetically.

words = input('Enter a hyphen-separated sequence of words: ').split('-')

def convert(words):
    return '-'.join(sorted(words))

converted_words = convert(words)

print(converted_words)

