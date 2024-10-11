def reverse_string(string):
    reversed_string = string[::-1]
    return f"The string reversed is: '{reversed_string}'."

def capitalize_string(string):
    capitalized_string = ""
    for word in string.split():
        capitalized_word = word.capitalize()
        capitalized_string += f"{capitalized_word} " 

    return f"the capitalized string is: '{capitalized_string[:-1]}'"
