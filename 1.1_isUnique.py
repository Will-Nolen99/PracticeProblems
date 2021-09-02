
# O(n) where n is the length of word.
def is_unique(word):
    letters = {}

    for letter in word:  # iterate through letters in word this is where linear time comes from
        if letter in letters:  # letters is a dict so it has constant access time
            return False
        else:
            letters[letter] = 1

    return True


# O(n) where n is length of word
def is_unique_no_dict(word):
    ASCII_LIMIT = 128 # number of total ascii values
    possible_chars = [False for _ in range(ASCII_LIMIT)]  # each index in array will represent a single ascii value

    for letter in word:  # Iterate through word
        value = ord(letter)
        if not possible_chars[value]:
            possible_chars[value] = True
        else:
            return False

    return True


print("dict")
words = ["hello", "world", "push", "pop"]

for w in words:
    print(is_unique(w))

print("No dict")
for w in words:
    print(is_unique_no_dict(w))
