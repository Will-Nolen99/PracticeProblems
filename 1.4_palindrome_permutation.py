

#  Time O(n)
#  Space O(n)
def palindrome_perm(word):

    count = {}

    word = word.strip()

    # O(n)
    for letter in word:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    # O(n)
    odd_count = 0
    for k, v in count.items():
        if v % 2 != 0:
            odd_count += 1


    return odd_count <= 1


print(palindrome_perm("rraacce"))




