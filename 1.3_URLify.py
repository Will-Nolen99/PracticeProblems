
# Time O(n) where n is length of word
# Space O(n)
def urlify(word):
    spaces = []

    #  Iterate through entire word O(n)
    for i, char in enumerate(word):
        if char == " ":
            spaces.append(i)

    builder = ""
    prev_space = 0

    #  Iterate through number of spaces. # spaces < length of word so it is not dominate term
    for i in spaces:
        builder += word[prev_space:i]
        builder += "%20"
        prev_space = i + 1  # This + 1 effectively removes the space



    return builder + word[prev_space:]


w = "Hello World"

print(urlify(w))