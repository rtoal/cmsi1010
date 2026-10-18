import random
import re

templates = [
    {
        "text": "A :adjective ghost is behind you!",
        "author": "rtoal"
    },
    {
        "text": "Some :adjective :creature with a :weapon is eating :dessert.",
        "author": "rtoal"
    },
    {
        "text": "Look! There is a :adverb :adjective :verb a :noun in :place.",
        "author": "The whole class"
    },
    {
        "text": "My :animal wore a :color :hat and danced with :number :nouns.",
        "author": "rtoal"
    },
    {
        "text": "In the :place, a :adjective :animal decided to :verb before lunch.",
        "author": "rtoal"
    },
    {
        "text": "Please do not :verb the :adjective :noun near my :noun.",
        "author": "rtoal"
    },
    {
        "text": "The :color :creature of :place loves :plural_noun and :adjective soup.",
        "author": "The whole class"
    },
    {
        "text": "Yesterday, I :past_tense_verb a :adjective :noun with my :body_part.",
        "author": "rtoal"
    },
    {
        "text": "Every :time_unit, the :adjective :animal sings to the :noun.",
        "author": "rtoal"
    },
    {
        "text": "Our :adjective :noun finally :past_tense_verb after :number hours.",
        "author": "The whole class"
    },
    {
        "text": "A :adjective :noun from :place wanted to :verb the :adjective moon.",
        "author": "rtoal"
    }
]

yes_answers = {"yes", "sí", "oui", "yup", "bet", "yep", "Y"}


def get_placeholder_words(template_text):
    placeholders = re.findall(r":([A-Za-z_]+)", template_text)
    answers = {}

    for placeholder in placeholders:
        if placeholder not in answers:
            while True:
                word = input(f"Enter a {placeholder}: ").strip()
                if 1 <= len(word) <= 30:
                    answers[placeholder] = word
                    break
                print("Please enter between 1 and 30 characters.")

    return answers


def fill_template(template_text, answers):
    def replace(match):
        return answers[match.group(1)]

    return re.sub(r":([A-Za-z_]+)", replace, template_text)


def play_round():
    template = random.choice(templates)
    answers = get_placeholder_words(template["text"])
    print(fill_template(template["text"], answers))
    print()
    print(f"Author: {template['author']}")


while True:
    play_round()
    print()
    print()
    if input("Play again? ").strip() not in yes_answers:
        print("Thanks for playing!")
        break
