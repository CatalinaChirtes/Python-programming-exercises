from itertools import permutations


# reading the data from the dictionary and returning a set with the words from it
def load_dictionary(file_name):
    with open(file_name, 'r') as file:
        return set(word.strip() for word in file)


# creating the permutations needed in building the anagrams
def generate_anagrams(word):
    word_permutations = permutations(word)
    anagrams = {"".join(permutation) for permutation in word_permutations}
    return anagrams


# filtering only the anagrams that exist in our dictionary file
def find_meaningful_anagrams(anagrams, word, dictionary):
    meaningful_anagrams = [anagram for anagram in anagrams if anagram in dictionary and anagram != word]
    return meaningful_anagrams


def display_anagrams(meaningful_anagrams, word):
    if meaningful_anagrams:
        print(f"Meaningful anagrams of '{word}':")
        for anagram in meaningful_anagrams:
            print(anagram)
    else:
        print(f"No meaningful anagrams found for '{word}'.")


def main():
    dictionary = load_dictionary('dictionary.txt')
    # read word from keyboard
    input_word = input("Enter a word: ").strip().lower()
    word_anagrams = generate_anagrams(input_word)
    meaningful_anagrams = find_meaningful_anagrams(word_anagrams, input_word, dictionary)
    display_anagrams(meaningful_anagrams, input_word)


if __name__ == "__main__":
    main()
