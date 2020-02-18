search_word = 'incomprehensiveness'

dictionary = [
    'lion',
    'cheetah',
    'elephant',
    'tiger',
    'wasp',
    'hare',
    'hear',
    'silent',
    'listen',
    'eighths', 'heights', 'highest'
]


def main(search_word):
    # Load words
    words = dictionary
    words = load_words()
    search_word_len = len(search_word)
    words_with_same_len = filter_dict(search_word_len, words)
    anagrams = map_dict(words_with_same_len, search_word)
    # print(anagrams)
    # for item in words_with_same_len:
    #     print(len(item))


def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = list(word_file.read().split())

    return valid_words


# Find words with that length in the dictionary
def filter_dict(length, dictionary):
    print(len(dictionary))
    word_arr = []
    for word in dictionary:
        if (len(word) == length):
            word_arr.append(word)
        else:
            pass

    print(word_arr)
    return word_arr


# map function
# def map_func(word):
#     word_arr = []
#     for letter in search_word:
#         if letter not in word:
#             print('letter {} not found in {}'.format(letter, search_word))
#             # print('Not found in {}'.format(word))
#             print('Breaking {}'.format(word))
#             break
#         return word
#     # word_arr.append(word)


# Find the words with the same characters
def map_dict(arr, search_word):
    word_arr = arr
    for word in arr:
        print(word)
        for letter in word:
            if letter not in search_word:
                print('letter {} not found in {}'.format(letter, search_word))
                # print('Not found in {}'.format(word))
                print('Breaking {}'.format(word))
                arr.remove(word)
                break
            # print(word)
    print(word_arr)
    print(len(word_arr))
    return word_arr


if __name__ == "__main__":
    # breakdown('lion')
    # find_length(breakdown('lion'))
    # english_words = load_words()
    # length = 0
    # for word in english_words:
    #     if len(word) > length:
    #         length = len(word)
    #         print(len(word))
            # print(word)

    # demo print
    # print(english_words)
    # map_dict(filter_dict(find_length(breakdown(search_word)), english_words))
    main('listen')
