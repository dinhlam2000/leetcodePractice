def trim(word):
    previous = None
    current = 0
    word = list(word)
    while current < len(word):
        if word[current] == '$':
            # trimming down the word
            if previous != None:
                word.pop(current)
                word.pop(previous)
                current = current - 1
                previous = previous - 1
            else:
                word.pop(current)
        else:
            previous = current
            current = current + 1
    return "".join(word)


# f$ec
# current = 1
# previous = 0
# word = [e,c]
# len(word) = 2
def is_dollar_delete_equal(arr):
    # fill in
    # arr contain no $
    for index, word in enumerate(arr):
        import pdb; pdb.set_trace()
        new_word = trim(word)
        print(new_word)
        arr[index] = new_word

    return arr

is_dollar_delete_equal(['b$$p', '$b$p'])