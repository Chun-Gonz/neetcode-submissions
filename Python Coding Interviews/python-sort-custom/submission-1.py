from typing import List

def wordLength(words):
    return len(words)


def sort_words(words: List[str]) -> List[str]:
    
    words.sort(key=wordLength, reverse=True)
    sorted_words = words
    return sorted_words


def sort_numbers(numbers: List[int]) -> List[int]:

    numbers.sort(key=abs)
    sorted_numbers=numbers
    return sorted_numbers


# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))
