def helper_capitalize(char, rotation_factor, capitalize):
    if capitalize == 1:
        z = ord('Z')
        a = ord('A')
    else:
        z = ord('z')
        a = ord('a')
    current_char_ascii = ord(char)
    new_char_ascii = current_char_ascii + rotation_factor
    if new_char_ascii > z:
        wrap_around_ascii = new_char_ascii % z + a
        new_char_ascii = wrap_around_ascii

    return chr(new_char_ascii)


def rotationalCipher(input, rotation_factor):
    # Write your code here
    if input == "":
        return ""
    result = ""
    for char in input:
        if char == 'C':
            import pdb; pdb.set_trace()
        if char.isalnum():
            capitalize = 0
            if char.upper() == char:
                capitalize = 1
            result = result + helper_capitalize(char, rotation_factor, capitalize)
        else:
            result = result + char

    return result

rotationalCipher("All-convoYs-9-be:Alert1.", 4)
