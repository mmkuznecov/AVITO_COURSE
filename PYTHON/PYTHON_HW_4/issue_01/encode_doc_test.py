from morse import LETTER_TO_MORSE


def encode(message: str) -> str:
    """
    Encode a string in accordance with the Morse code table

    >>> encode('SOS')
    '... --- ...'
    >>> encode('SOS SOS')
    '... --- ...   ... --- ...'
    >>> encode('A')
    '.-'
    >>> encode('HELLO WORLD')
    '.... . .-.. .-.. ---   .-- --- .-. .-.. -..'
    >>> encode('example')
    Traceback (most recent call last):
        ...
    KeyError: 'e'
    >>> encode('SOS!')
    Traceback (most recent call last):
        ...
    KeyError: '!'
    >>> encode('PRETTY LONG MESSAGE') # doctest: +ELLIPSIS
    '.--. .-. . - - -.--   .-.. --- -. --.   -- . ... ... .- --. .'
    """
    encoded_signs = [
        LETTER_TO_MORSE[letter] for letter in message
    ]

    return ' '.join(encoded_signs)


if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.ELLIPSIS)
