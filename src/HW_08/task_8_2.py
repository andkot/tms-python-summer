# Даны три слова. Выяснить, является ли хоть одно из них палиндромом
# ("перевертышем"), т. е. таким, которое читается одинаково слева направо и
# справа налево. Определить функцию, позволяющую распознавать слова
# палиндромы.

def is_palindrome(word: str) -> bool:
    """
    return true if 'word' is a palindrome or empty and false when 'word' isn't a palindrome;
    :param word: string
    :return: bool
    """

    word_len = len(word)
    if word_len == 0:
        return True
    elif word_len % 2 == 0:
        half = int(word_len / 2)
        right_part = word[:half]
        left_part = word[:half-1:-1]

        return right_part == left_part
    else:
        half = int(word_len / 2)
        right_part = word[:half]
        left_part = word[:half:-1]

        return right_part == left_part

# testing

print(f'\'aabaa\' - {is_palindrome("aabaa")}')
print(f'\'aabbaa\' - {is_palindrome("aabbaa")}')
print(f'\'asdabbadsa\' - {is_palindrome("asdabbadsa")}')
