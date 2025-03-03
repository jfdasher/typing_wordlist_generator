# typing_wordlist_generator
Wordlist generator for typing practice.

Keeps me from repeatedly looking up the abstruse grep syntax for minimum and maximum lengths.  Equivalent:
```shell
$grep -E 'cr' wordlist.txt | grep -E '^.{3,10}$' | shuf -n 10 | paste -s -d" "
```