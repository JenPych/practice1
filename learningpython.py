""" Learning how to define a function, add attributes to it and calling the function below. """

# defining an anagram

def anagram(word1, word2):
    word1: str = word1.lower()
    word2: str = word2.lower()

    return sorted(word1) == sorted(word2)

# A1 = ('cinema', 'iceman')
# A2 = ('ice', 'cei')

# print(anagram(A1[0], A1[1]))
# print(anagram(A2[0], A2[1]))

# taking user input
A3: str = input("Enter a word: ").replace(' ', '')
A4: str = input("Enter another word with same letter as above: ").replace(' ', '')

# checking input by calling the function in if else condition
if anagram(A3, A4):
    print(f"The words {A3.upper()} and {A4.upper()} are anagrams.")
else:
    print(f"The words {A3.upper()} and {A4.upper()} are NOT anagrams." )



