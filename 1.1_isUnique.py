
# O(n) where n is the length of word.
def is_unique(word):
    letters = {}

    for letter in word:  # iterate through letters in word this is where linear time comes from
        if letter in letters:  # letters is a dict so it has constant access time
            return False
        else:
            letters[letter] = 1

    return True




words = ["hello", "world", "push", "pop"]

for w in words:
    print(is_unique(w))

