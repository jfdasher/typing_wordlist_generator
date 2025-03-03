import argparse
import re
import random
from json_import_list_util import load_wordlist


left_lower = list("zxvc")
left_lower_no_index = list("zx")
left_home = list("asdfg")
left_upper = list("qwert")
right_lower = list("bnm")
right_home = list("yhjlkl")
right_upper = list("uiop")

left = left_lower + left_home + left_upper
right = right_lower + right_home + right_upper

def contains_consecutive_chars(s, char_list, repeats=True):
    for i in range(len(s) - 1):
        if s[i] in char_list and s[i + 1] in char_list and (repeats or s[i] != s[i + 1]):
            return True
    return False


def contains_successive_chars(s, char_list, succeeding_char_list, repeats=True):
    for i in range(len(s) - 1):
        if s[i] in char_list and s[i + 1] in succeeding_char_list and (repeats or s[i] != s[i + 1]):
            return True
    return False



def contains_any(s, char_list):
    for char in char_list:
        if char in s:
            return True
    return False

def endswith_any(s, str_list):
    for end_str in str_list:
        if s.endswith(end_str):
            return True
    return False

def contains_c_and_successive_chars(s, list1, list2):
    for i in range(len(s) - 2):
        if s[i] == 'c' and (s[i + 1] not in list1 or  s[i + 2] not in list2):
            return True
    return False
def matches_patterns (text, patterns):
    for pattern in patterns:
        if re.search(pattern, text):
            return True
    return False



parser = argparse.ArgumentParser(description='Load a wordlist from a JSON file.')
parser.add_argument('file_path', type=str, help='The path to the wordlist JSON file')
parser.add_argument('--patterns', type=str, nargs='+', help='List of patterns to match')
parser.add_argument('--min_word_length', type=int, default=-1, help='Minimum word length (default: -1)')
parser.add_argument('--max_word_length', type=int, default=-1, help='Maximum word length (default: -1)')
parser.add_argument('--sample_size', type=int, default=-1, help='Sample size (default: -1)')

args = parser.parse_args()

with open(args.file_path, encoding="utf-8") as x: 
    words = [line.rstrip() for line in x.readlines()]

patterns = [r"cr"]

subset = [word for word in words if (patterns and matches_patterns(word, patterns))]

if args.min_word_length > -1:
    print("Filtering words shorter than {}".format(args.min_word_length))
    subset = [word for word in subset if len(word) >= args.min_word_length]
if args.max_word_length > -1:
    print("Filtering words larger than {}".format(args.max_word_length))
    subset = [word for word in subset if len(word) <= args.max_word_length]

print ("Found {} words total".format(len(subset)))

# Create a random sample if sample_size is specified and less than the number of entries in subset
if args.sample_size > -1 and args.sample_size < len(subset):
    subset = random.sample(subset, args.sample_size)
    print ("Sampling {} words".format(len(subset)))

print(" ".join(subset))     
