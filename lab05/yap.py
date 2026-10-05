import random

words = {
    "noun": ["dog", "carrot", "chair", "toy", "rice cake"],
    "verb": ["ran", "barked", "squeaked", "flew", "fell", "whistled"],
    "adjective": ["small", "great", "fuzzy", "funny", "light"],
    "preposition": ["through", "over", "under", "beyond", "across"],
    "adverb": ["barely", "mostly", "easily", "already", "just"],
    "color": ["pink", "blue", "mauve", "red", "transparent"]
}

templates = [
    """
    Yesterday the color noun
    verb preposition the coach’s
    adjective color noun that was
    adverb adjective before
    """,
    """
    Oh, no! The adjective adjective adjective
    noun verb despite our adverb adjective efforts
    """,
    """
    I could not find the color adjective noun
    """
]


def random_sentence():
    sentence = []
    for token in random.choice(templates).split():
        if token in words:
            sentence.append(random.choice(words[token]))
        else:
            sentence.append(token)
    return " ".join(sentence) + "."


for _ in range(10):
    print(random_sentence())
