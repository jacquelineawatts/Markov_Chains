from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    file_text = open(file_path).read()

    return file_text


def make_chains(text_string):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    chains = {}

    words = text_string.split()

    key_item1 = 0
    key_item2 = 1
    value_item = 2

    while key_item2 < (len(words) - 1):

        key = (words[key_item1], words[key_item2])

        if key in chains:
            chains[key].append(words[value_item])
        else:
            chains[key] = [words[value_item]]
        
        key_item1 += 1
        key_item2 += 1
        value_item += 1


    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""
    # 1. Pick a random key from our dictionary
    # 2. Put randomly generated key into our string
    # 3. Select at random a word from our values list thats associated with our key 
    # 4. Add that word to the string
    # 5. Shift frame to new key set which is second word from previous key + new word from value list
    # 6. Start over from step2


    #  While key in dictionary:

    current_key = choice(chains.keys())
    print current_key
    value = choice(chains[current_key])

    for word in current_key:
        text += word + " "
    text += value + " "

    new_key = (current_key[1], value)

    print new_key
    return text


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

# print random_text
