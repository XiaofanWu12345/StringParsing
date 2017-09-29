# Xiaofan Wu 903152422

from string import punctuation

def normalize_text(text):
    """Return copy of text in lowercase with punctuation removed.

    Parameters:
    text: str - text to normalize

    Return: str which is copy of text converted to lowercase with
    punctuation (the chars in string.punctuation) removed.

    Usage Examples:
    >>> normalize_text("Numchuk skills, bow hunting skills, computer hacking skills...")
    'numchuk skills bow hunting skills computer hacking skills'
    """
    alist = list(text)
    return ''.join([i.lower() for i in alist if i not in punctuation])


def mk_word2count(text):
    """Return a dictionary mapping words in text to their count in text.

    Parameters:
    text: str - string containing words separated by spaces

    Return: char_dict: dict - dictionary whose keys are words and
    associated values are the number of times the word appears in text

    Usage Examples: (Note technique for testing dict equality.)

    >>> mk_word2count('the butcher the baker the candlestick maker') == {'butcher': 1, 'baker': 1, 'candlestick': 1, 'the': 3, 'maker': 1}
    True
    """
    alist = text.split()
    adict = {}
    for i in alist:
        num = len([a for a in alist if a == i])
        adict[i]=num
    return adict


def dict2tuples(word_dict, key=None):
    """Convert a str:int dictionary to a sorted list of (str, int) tuples, optionally with a key

    Parameters:
    word_dict: dict[str -> int]
    key: (optional) a key function to extract the element of the tuples by which to sort

    Return: a list[(str, int)], sorted in descending order, optionally by a key

    Usage Examples:
    >>> dict2tuples({'a': 2, 'b': 5, 'c': 1}, key=lambda t: t[1])
    [('b', 5), ('a', 2), ('c', 1)]
    """
    return sorted([(k, v) for k, v in word_dict.items()], key=key, reverse=True)


def normalize_counts(tuples, max_value=100):
    """Normalize the second values in tuples.

    Parameters:
    tuples: Sequence[(str, int)] - (word, count) tuples
    max_value: int - the max value of the normalized counts (min value is 0)

    Return: Sequence[(str, int)] with same first elements as tuples
    but whose second elements are normalized to the range 0 to
    max_value.

    Usage Examples:
    >>> wctups = [('a', 200), ('the', 180), ('an', 160), ('shenannigans', 50)]
    >>> normalize_counts(wctups, 100)
    [('a', 100), ('the', 90), ('an', 80), ('shenannigans', 25)]
    """
    st = sorted(tuples, key = lambda x:x[1], reverse = True )
    scale = max_value/st[0][1]
    nst = []
    for item in st:
        new = list(item)
        new[1] = int(new[1]*scale)
        newt = tuple(new)
        nst.append(newt)
    return nst


def word_hist(bar_list):
    """Create a text-based bar chart from bar_list.

    Parameters:
    bar_list: Sequence[(str, int)] - (label, length) tuples

    Return: list[str] with one line per tuple in bar_list. Each line --
    a str in the returned list -- has the right-aligned label, a |
    character, then length Xs

    Usage Examples:
    >>> from pprint import pprint
    >>> pprint(word_hist([('a', 10),('the', 9),('an', 8),('shenannigans', 2)]))
    ['           a | XXXXXXXXXX',
     '         the | XXXXXXXXX',
     '          an | XXXXXXXX',
     'shenannigans | XX']
    """
    max_len = len(max(bar_list, key=lambda t: len(t[0]))[0])
    return ["{word} | {bars}".format(word=w.rjust(max_len), bars="X"*length)
            for w, length in bar_list]

import os.path
def main(args):
    # code intended to be executed when run as a script
    try:
        if not os.path.exists(args[1]):
            print(args[1] + " was not found.")
            return
    except:
        args.append(input("Please enter the file name."))
        while not os.path.exists(args[1]):
            print(args[1] + " doesn't exist.")            
            args[1] = input("Please renter the file name.")
    infile = open(args[1],'r')
    text = infile.read()
    infile.close()
    text = normalize_text(text)
    word_dict = mk_word2count(text)
    tuples = dict2tuples(word_dict, lambda t: t[1])
    bar_list = normalize_counts(tuples,100 if len(args)<3 else int(args[2]))
    histogram = word_hist(bar_list)
    num_lines = len(histogram) if len(args)<4 else int(args[3])
    from pprint import pprint
    pprint(histogram[:num_lines])

if __name__=="__main__":
   import sys
   main(sys.argv)