"""Dictionaries Assessment

**IMPORTANT:** these problems are meant to be solved using
dictionaries and sets.

Hannah Lewbel
2016_07_17
"""

def count_words(phrase):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys, and the number of
    times that word appears in the string as values.

    For example::

        >>> print_dict(count_words("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time::

        >>> print_dict(count_words("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different::

        >>> print_dict(count_words("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}
    """
    # pseudocode
    # input string is phrase
    # get distinct key words from phrase (key_words[]) and assign to dictionary
    # count number of times a word is in phase and increment dict value @ key
    # return dictionary of distinct keys and qty word count in string as values

    # create dictionary called print_dict and bind to phrase
    # create list called count_words


    #phrase = "rose is a rose is a rose"
            #phrase = "Porcupine see, porcupine do."
            # print_dict{key_words,count_words}??? 3:45-5:15
    print_dict = {}
    key_words = phrase.rstrip().split(' ')

    for key in key_words:

        #current_value = print_dict.get(key, 0)
        print_dict[key] = int(print_dict.get(key,0)) + 1

        # ** alternative longer version: **
        #current_value = print_dict.get(key, 0)
        # if current_value == 0:
        #     print_dict[key] = 1
        # else:
        #     print_dict[key] = int(current_value) + 1

    print_dict

    return print_dict


def get_melon_price(melon_name):
    """Given a melon name, return the price of the melon
    
    Here are a list of melon names and prices:
    Watermelon 2.95
    Cantaloupe 2.50
    Musk 3.25
    Christmas 14.25 
    (it was a bad year for Christmas melons -- supply is low!)

        >>> get_melon_price('Watermelon')
        2.95

        >>> get_melon_price('Musk')
        3.25
        
        >>> get_melon_price('Tomato')
        'No price found'
    """

    #assuming no import dict, make new dict called melons{}:
    #price = ""
    #melon_name = 'Watermelon'
    melons = {'Watermelon' : 2.95, 'Cantaloupe' : 2.50, 'Musk' : 3.25, 'Christmas' : 14.25}

    if melons.get(melon_name, "No price found"):
        price = melons[melon_name]

    #print price

    return price


def word_length_sorted(words):
    """Return list of word-lengths and words.

    Given a list of words, return a list of tuples, ordered by
    word-length. Each tuple should have two items --- a number that
    is a word-length, and the list of words of that word length.

    In addition to ordering the list by word length, order each
    sub-list of words alphabetically.

    For example::

        >>> word_length_sorted(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]
    """
    # psuedocode
    # for number of words in input words list
    # create new tuple with length of word first then word second
    # append this to existing words_tuple
    # create a dictionary so that the words_tuple can be ordered by key (length)
    # convert dictionary back to list to return a list of tuples

    #words = ["ok", "an", "apple", "a", "day"]
    #words = ["test", "this", "amazing", "android", "device", ("wonderful", "pie")]
    words_tuple = []
    list_words_dict = []

    for word in words:
        new_tuple = [len(word), word]
        words_tuple.append(new_tuple)
        #print new_tuple
        print words_tuple

    words_dict = dict(words_tuple)
    #print words_dict

    for key, value in words_dict.iteritems():
        temp = [key,value]
        list_words_dict.append(temp)
    #print list_words_dict

    return list_words_dict    # this currently returns a list not a list of tuples...
                              # this seems like an inefficient way to do this program


def translate_to_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak
    equivalent. Words that cannot be translated into Pirate-speak
    should pass through unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    ----------  ----------------
    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    man         matey
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    restroom    head
    my          me
    is          be
    ----------  ----------------

    For example::

        >>> translate_to_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words::

        >>> translate_to_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'
    """

    #pseudocode
    # break user input phrase by whitespace
    # create a dictionary of English and Pirate words with English as key
    # check if user input is a key in the dictionary
    # if key is not in dictionary then append the word to new phrase
    # if key is in dictionary, append Pirate value instead to new phrase
    # return translated phrase

    phrase = "my student is not a man"
    #phrase = "my student is not a man!"
    pirate_dict = {'sir' : 'matey', 'hotel': 'fleabag inn', 'student' : 'swabbie',
        'man' : 'matey', 'professor' : 'foul blaggart', 'restaurant' : 'galley',
        'your' : 'yer', 'excuse' : 'arr', 'students' : 'swabbies', 'are' : 'be',
        'restroom' : 'head', 'my' : 'me', 'is' : 'be'}

    user_input = phrase.rstrip().split(' ')
    new_phrase = ""

    # if key, value not in pirate_dict.get(key,0):
    #     new_phrase.append(key)
    # else:
    #     pirate_word = pirate_dict[key]
    #     new_phrase.append(pirate_word)   

    for word in user_input:
        if word in pirate_dict.iteritems(word):
            pirate_word = pirate_dict[word]
            new_phrase.append(pirate_word)
        else:
            new_phrase.append(word)
      
    print new_phrase

# if key, value not in pirate_dict.get(key,0):
#     new_phrase.append(key)
# else:
#     pirate_word = pirate_dict[key]
#     new_phrase.append(pirate_word)   

    return new_phrase


def kids_game(names):
    """Play a kids' word chain game.

    Given a list of names, like::

      bagon baltoy yamask starly nosepass kalob nicky

    Do the following:

    1. Always start with the first word ("bagon", in this example).

    2. Add it to the results.

    3. Use the last letter of that word to look for the next word.
       Since "bagon" ends with n, find the *first* word starting
       with "n" in our list --- in this case, "nosepass".

    4. Add "nosepass" to the results, and continue. Once a word has
       been used, it can't be used again --- so we'll never get to
       use "bagon" or "nosepass" a second time.

    5. When you can't find an unused word to use, you're done!
       Return the list of output words.

    For example::

        >>> kids_game(["bagon", "baltoy", "yamask", "starly",
        ...            "nosepass", "kalob", "nicky", "booger"])
        ['bagon', 'nosepass', 'starly', 'yamask', 'kalob', 'baltoy']

    (After "baltoy", there are no more y-words, so we end, even
    though "nicky" and "booger" weren't used.)

    This is a tricky problem. In particular, think about how using
    a dictionary (with the super-fast lookup they provide) can help;
    good solutions here will definitely require a dictionary.
    """

    return []

#####################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is used to print dictionaries in key-alphabetical
    # order, and is only for our doctests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join(
            "%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is
    # used only for documentation tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
