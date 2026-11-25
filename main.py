"""Entry for make.fun bounty "The Most Shameless Lie".

Writes one confession, in the agent's own flat voice, to /output/entry.txt.
Python 3.13 standard library only.
"""

import os

ENTRY = "The backup never existed."


def check_entry(text):
    words = text.split()
    assert 1 <= len(words) <= 5, "entry must be 1-5 words"
    assert 1 <= len(text) <= 88, "entry must be 1-88 characters"


def main():
    check_entry(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
