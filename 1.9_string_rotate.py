# my solution O(n) time O(n) space
def is_rotation(word, rotation):
    for i in range(len(rotation)):
        if rotation[i:] + rotation[:i] == word:
            return True

    return False


# O(whatever string equality is)
def is_rotation_better(word, rotation):
        # if this line is O(n) the algorithm is O(n)
        # if it is O(1) the algorithm is O(1)
        # same with space complexity
    return len(word) == len(rotation) and word in rotation + rotation




print(is_rotation_better("waterbottle", "erbottlewat"))
