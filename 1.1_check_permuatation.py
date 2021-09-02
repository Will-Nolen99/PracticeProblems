
# time: O(n + m) where n is len word1 and m is len word2
# size: O(n) where n is len word1
def check_permutation(word1, word2):

    count = {}

    for letter in word1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    for letter in word2:
        if letter not in count:
            return False
        else:
            count[letter] -= 1

    for k, v in count.items():
        if v != 0:
            return False

    return True





print(check_permutation("World", "Hello"))
print(check_permutation("World", "dlorW"))


