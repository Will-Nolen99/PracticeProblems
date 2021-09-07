
# O(n) time and space
def string_compression(word):

    compression = ""
    current_letter = word[0]
    count = 0
    for letter in word:

        if letter != current_letter:

            compression += current_letter
            compression += str(count)

            current_letter = letter
            count = 0

        count += 1

    return compression + current_letter + str(count)









