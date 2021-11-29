def trim_word(word):
    previous = -1
    current = 0
    word_list = list(word)
    while current < len(word_list):
        if word_list[current] == "$":
            if previous < 0:
                word_list.pop(current)
            else:
                word_list.pop(current)

                word_list.pop(previous)
                current = current - 1
                previous = current - 1
        else:
            current = current + 1
            previous = previous + 1
    return "".join(word_list)


# ['f$ec', 'ec']
# new_word = trim("f$ec')
# --> [e,c]
# previous = -1
# current = 0
# return ec


def is_dollar_delete_equal(arr):
    # fill in
    # ARR CONTAIN no inputs? --> return True
    # $$$ delete dollar sign if there's no previous
    # capitalizied letter and lowercase considered the same?
    # a$EC ec --> return False

    # scanning through the array
    # for each word, trim down the dollar sign and the letter before it
    # previous and a current
    # current = dollarsign --> pop previous
    # pop current
    # current += 1 , previous += 1
    # decrease previous by 1 and current by 1
    # import pdb; pdb.set_trace()
    for index, word in enumerate(arr):
        new_word = trim_word(word)
        arr[index] = new_word

    return len(set(arr)) == 1

is_dollar_delete_equal(['f$ec', 'ec'])