CARD = """\
┌─────────┐
│{rank}       │
│         │
│         │
│    {suite}    │
│         │
│         │
│       {rank}│
└─────────┘
"""

HIDDEN_CARD = """\
┌─────────┐
│░░░░░░░░░│
│░░░░░░░░░│
│░░░░░░░░░│
│░░░░░░░░░│
│░░░░░░░░░│
│░░░░░░░░░│
│░░░░░░░░░│
└─────────┘
"""

def join_lines(strings):
    """
    Stack strings horizontally.
    This doesn't keep lines aligned unless the preceding lines have the same length.
    :param strings: Strings to stack
    :return: String consisting of the horizontally stacked input
    """
    liness = [string.splitlines() for string in strings]
    return '\n'.join(''.join(lines) for lines in zip(*liness))


def card_to_string(card):
    if not card.faceup:
        return HIDDEN_CARD

    # 10 is the only card with a 2-char rank abbreviation
    # rank = card.rank
    rank = '? '

    # we will use the Enum values to print the symbol for each suite
    if card.rank.value < 10 and card.rank.value > 1:
        rank = str(card.rank.value) + " "
    elif card.rank.value == 1:
        rank = 'A '
    elif card.rank.value == 13:
        rank = 'K '
    elif card.rank.value == 12:
        rank = 'Q '
    elif card.rank.value == 11:
        rank = 'J '
    elif card.rank.value == 10:
        rank = '10'
    else:
        raise RuntimeError("Invalid card in deck")

    # add the individual card on a line by line basis
    return CARD.format(rank=rank, suite=card.suite.value)

def ascii_version_of_cards(cards):
    """
    Instead of a boring text version of the card we render an ASCII image of the card.
    :param cards: One or more card objects
    :return: A string, the nice ascii version of cards
    """
    return join_lines(map(card_to_string, cards))
