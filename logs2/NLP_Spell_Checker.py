#c. Spell Checker
import re
from collections import Counter


# Simulated corpus for the purpose of spelling correction
CORPUS_TEXT = """
Normally people are serious and pure in their intent. They note everything and contain all
the necessary documents.
An accident dose can change someone's life. The result is purely unexpected, even if
everything seems ordinary.
END-OF-CORPUS
"""


def load_corpus(text):
    word_freq = Counter()
    for line in text.splitlines():
        if line.strip() == "END-OF-CORPUS":
            break
        words = re.findall(r"[a-zA-Z'-]+", line.lower())
        word_freq.update(words)
    return word_freq


def edits1(word):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]


    deletes = [L + R[1:] for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
    replaces = [L + c + R[1:] for L, R in splits if R for c in letters]
    inserts = [L + c + R for L, R in splits for c in letters]


    return set(deletes + transposes + replaces + inserts)


def correct(word, word_freq):
    word = word.lower()
    if word in word_freq:
        return word


    candidates = edits1(word)
    valid_candidates = [w for w in candidates if w in word_freq]


    if not valid_candidates:
        return word


    return max(valid_candidates, key=lambda w: (word_freq[w], -len(w)))  # Prefer higher freq, shorter word


def main():
    word_freq = load_corpus(CORPUS_TEXT)


    try:
        N = int(input("Enter number of words to correct: "))
        for _ in range(N):
            word = input("Enter word: ").strip()
            print("Corrected:", correct(word, word_freq))
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
   
