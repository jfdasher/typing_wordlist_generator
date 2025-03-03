"""
This script loads a wordlist from a JSON file (https://github.com/aparrish/wordfreq-en-25000)
and writes the words to an output text file, one word per line.
If no output file is specified, the words are printed to the system output.

Functions:
    load_wordlist(file_path): Loads a wordlist from a JSON file and returns a list of words.
    load_wordlist_from_json(file): Loads a wordlist from a JSON file object and returns a list of words.

Usage:
    python json_word_freq_to_word_list.py <input_file> [output_file]

Arguments:
    input_file: The path to the wordlist JSON file.
    output_file: The path to the output text file (optional).
"""

import json
import argparse

def load_wordlist(file_path):
    with open(file_path, 'r') as file:
        return load_wordlist_from_json(file)


def load_wordlist_from_json(file):
    return [k[0] for k in json.load(file)]

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Load a wordlist from a JSON file.')
    parser.add_argument('input_file', type=str, help='The path to the wordlist JSON file')
    parser.add_argument('output_file', type=str, nargs='?', help='The path to the output text file (optional)')
    args = parser.parse_args()

    # Load the wordlist using the provided file path
    wordlist = load_wordlist(args.input_file)
        
    # Write the words to the output file if specified, otherwise print to system output
    if args.output_file:
        with open(args.output_file, 'w', encoding='utf-8') as output_file:
            for word in wordlist:
                output_file.write(word + '\n')
        print(f"Words have been written to {args.output_file}")
    else:
        for word in wordlist:
            print(word + "\n")