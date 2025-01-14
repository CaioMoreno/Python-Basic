from string import ascii_letters, punctuation

def separate_characters(my_string: str):
    # Initialize lists to store characters
    letters = []    # For ASCII letters
    punctuations = []  # For punctuation characters
    others = []     # For all other characters (including spaces)
    
    # Iterate over each character in the input string
    for char in my_string:
        if char in ascii_letters:
            letters.append(char)  # Add ASCII letters to the list
        elif char in punctuation:
            punctuations.append(char)  # Add punctuation to the list
        else:
            others.append(char)  # Add all other characters (e.g., spaces, accented chars)

    # Convert lists to strings
    letters_str = "".join(letters)
    punctuations_str = "".join(punctuations)
    others_str = "".join(others)

    # Return a tuple with all three strings
    return (letters_str, punctuations_str, others_str)
